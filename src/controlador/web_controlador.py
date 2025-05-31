from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from pydantic import BaseModel
from src.model.aplicacion import Aplicacion
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones


class UsuarioWeb(BaseModel):
    nombre: str
    tipo_documento: str
    numero_documento: int
    contrasena: str
    correo: str
    fecha_nacimiento: str

class IniciarSesionWeb(BaseModel):
    nombre: str
    contrasena: str

class TransaccionWeb(BaseModel):
    cantidad_dinero: float
    categoria: str
    fecha: str
    hora: str

class ActualizarTransaccionWeb(BaseModel):
    id: int
    campo: str
    nuevo_valor: str

class ContrasenaNuevaWeb(BaseModel):
    nueva_contrasena: str

class FechaTransaccionesWeb(BaseModel):
    fecha_inicial: str
    fecha_final: str

class WebControlador:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1")
        self.aplicacion = Aplicacion(Usuario)
        self.__registrar_rutas()
        self.contador_id = 0

    def __registrar_rutas(self):
        @self.router.post("/crear_cuenta")
        def crear_cuenta(usuario: UsuarioWeb):

            usuario=Usuario(
                nombre=usuario.nombre,
                tipo_documento=usuario.tipo_documento,
                numero_de_documento=usuario.numero_documento,
                contrasena=usuario.contrasena,
                correo=usuario.correo,
                fecha_nacimiento=usuario.fecha_nacimiento

            )
            return {"crear_cuenta": self.aplicacion.crear_cuenta(usuario)}
        
        @self.router.post("/iniciar_sesion")
        def iniciar_sesion(usuario: IniciarSesionWeb):
            return {"iniciar_sesion": self.aplicacion.iniciar_sesion(usuario.nombre, usuario.contrasena)}
        
        @self.router.post("/realizar_transaccion")
        def realizar_transaccion(transaccion: TransaccionWeb):
            self.contador_id += 1
            transaccion = Transacciones(
                id = self.contador_id,
                cantidad_dinero=transaccion.cantidad_dinero,
                categoria=transaccion.categoria,
                fecha=transaccion.fecha,
                hora=transaccion.hora
            )
            return {"realizar_transaccion": self.aplicacion.realizar_transaccion(transaccion)}
        
        @self.router.post("/actualizar_transaccion")
        def actualizar_transaccion(nueva_transaccion: ActualizarTransaccionWeb):
            usuario = self.aplicacion.obtener_usuario_logueado()
            transacciones = usuario.obtener_transacciones()
            transaccion = next((t for t in transacciones if t.obtener_id() == nueva_transaccion.id), None)

            if transaccion is None:
                raise HTTPException(status_code=404, detail="Transacción no encontrada")

            if nueva_transaccion.campo == "Cantidad de dinero":
                try:
                    transaccion.actualizar_cantidad_dinero(float(nueva_transaccion.nuevo_valor))
                except ValueError:
                    raise HTTPException(status_code=400, detail="Valor inválido para cantidad.")
            elif nueva_transaccion.campo == "Categoría":
                transaccion.actualizar_categoria(nueva_transaccion.nuevo_valor)
            elif nueva_transaccion.campo == "Fecha":
                transaccion.actualizar_fecha(nueva_transaccion.nuevo_valor)
            elif nueva_transaccion.campo == "Hora":
                transaccion.actualizar_hora(nueva_transaccion.nuevo_valor)
            
        @self.router.post("/visualizar_transaccion")
        def visualizar_transaccion(fechas: FechaTransaccionesWeb):
            try:
                transacciones = self.aplicacion.visualizar_transacciones(fechas.fecha_inicial, fechas.fecha_final)
                
                if not transacciones:
                    raise HTTPException(status_code=404, detail="No se encontraron transacciones en ese rango de fechas.")
                
                return {"transacciones": transacciones}
            
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
            
        
        @self.router.post("/cambiar_contrasena")
        def cambiar_contrasena(usuario: ContrasenaNuevaWeb):
            return {"cambiar_contrasena": self.aplicacion.cambiar_contrasena(usuario.nueva_contrasena)}
        
        @self.router.post("/cerrar_sesion")
        def cerrar_sesion():
            return {"cerrar_sesion": self.aplicacion.cerrar_sesion()}

        @self.router.post("/validar_usuario_logueado")
        def validar_usuario_logueado():
            return {"validar_usuario_logueado": self.aplicacion.validar_usuario_logueado()}
        

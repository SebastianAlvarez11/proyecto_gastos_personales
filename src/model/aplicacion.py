from src.model.usuario import Usuario
from src.model.exception import (ErrorInicioSesionUsuarioNoExistente, ErrorInicioSesionContrasenaIncorrecta, ErrorInicioSesionActivo, ErrorUsuarioExistente,
                                 ErrorContrasenaIgual, ErrorIniciarSesionSinNombre, ErrorMuchosIntentosFallidos, ErrorSistemaCaido, ErrorContrasenaIntentosFallidos,
                                 ErrorTransaccionSinLoguearse, ErrorVisualizarSinLoguearse)

class Aplicacion:

    MAX_INTENTOS = 3 #CAMBIAR A 3 INTENTOS
    TIEMPO_BLOQUEO = 300
    def __init__(self):
        self.usuarios: list[Usuario] = []
        self.intentos_fallidos = {}
        self.tiempos_bloqueo = {}
        self.usuario_logueado: Usuario = None
    
    def crear_cuenta(self, usuario: Usuario):
        usuario.validar_tipo_documento(usuario.tipo_documento)
        usuario.validar_fecha_nacimiento(usuario.fecha_nacimiento)
        usuario.validar_correo(usuario.correo)
        for usuario_existe in self.usuarios:
            if usuario_existe.correo == usuario.correo:
                raise ErrorUsuarioExistente()
        self.usuarios.append(usuario)  

    def iniciar_sesion(self, nombre: str, contrasena: str):
        if not nombre and not contrasena:
            raise ErrorSistemaCaido()

        if self.intentos_fallidos.get(nombre, 0) >= Aplicacion.MAX_INTENTOS:
            raise ErrorMuchosIntentosFallidos()

        if not nombre:
            raise ErrorIniciarSesionSinNombre()

        if self.usuario_logueado:
            raise ErrorInicioSesionActivo()
        
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.contrasena == contrasena:
                    self.usuario_logueado = usuario
                    self.intentos_fallidos[self.usuario_logueado.nombre] = 0
                    return True
                else:
                    self.intentos_fallidos[nombre] = self.intentos_fallidos.get(nombre, 0)+ 1
                    raise ErrorInicioSesionContrasenaIncorrecta()
        raise ErrorInicioSesionUsuarioNoExistente()

    def cambiar_contrasena(self, nueva_contrasena):
        if self.usuario_logueado.contrasena == nueva_contrasena:
            self.intentos_fallidos[self.usuario_logueado.nombre] += 1
            raise ErrorContrasenaIgual()
        try:
            self.usuario_logueado.validar_contrasena(nueva_contrasena)
        except Exception as exception:
            self.intentos_fallidos[self.usuario_logueado.nombre] += 1
            raise exception

        
        if self.intentos_fallidos.get(self.usuario_logueado.nombre) >= Aplicacion.MAX_INTENTOS:
            raise ErrorContrasenaIntentosFallidos()
            #if self.tiempos_bloqueo.get(self.usuario_logueado.nombre) and time.time() - self.tiempos_bloqueo[self.usuario_logueado.nombre] < Aplicacion.TIEMPO_BLOQUEO:
            #    raise ErrorContrasenaIntentosFallidos()
            #else:
            #    self.intentos_fallidos[self.usuario_logueado.nombre] = 0
        
        if self.usuario_logueado:
            self.usuario_logueado.contrasena = nueva_contrasena
            return True  
        
        self.intentos_fallidos[self.usuario_logueado.nombre] = 0

        if self.usuario_logueado.nombre in self.tiempos_bloqueo:
            del self.tiempos_bloqueo[self.usuario_logueado.nombre]


    def validar_usuario_logueado(self):
        return self.usuario_logueado is not None
        
    def visualizar_transacciones(self, fecha_inicial, fecha_final):
        if not self.validar_usuario_logueado():
            raise ErrorVisualizarSinLoguearse()  
        self.usuario_logueado.visualizar_transacciones()

    def actualizar_transaccion(self, nueva_transaccion):
        if not self.validar_usuario_logueado():
            raise ErrorTransaccionSinLoguearse()
        self.usuario_logueado.actualizar_transaccion()
        
    def cerrar_sesion(self):
        self.usuario_logueado = None
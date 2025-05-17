from src.model.aplicacion import Aplicacion
from src.model.usuario_db import UsuarioDB
from src.model.usuario import Usuario

class AppControlador:
    def __init__(self):
        #self.aplicacion = Aplicacion(Usuario())
        self.aplicacion = Aplicacion(UsuarioDB())

    def crear_cuenta(self, usuario):
        return self.aplicacion.crear_cuenta(usuario)

    def iniciar_sesion(self, nombre, contrasena):
        return self.aplicacion.iniciar_sesion(nombre, contrasena)
    
    def realizar_transaccion(self, transaccion):
        return self.aplicacion.realizar_transaccion(transaccion)
    
    def cambiar_contrasena(self, nueva_contrasena):
        return self.aplicacion.cambiar_contrasena(nueva_contrasena)
    
    def visualizar_transaccion(self, fecha_inicial, fecha_final):
        return self.aplicacion.visualizar_transacciones(fecha_inicial, fecha_final)
    
    def actualizar_transaccion(self, nueva_transaccion):
        return self.aplicacion.actualizar_transaccion(nueva_transaccion)
    
    def cerrar_sesion(self):
        return self.aplicacion.cerrar_sesion()
    
    def validar_usuario_logueado(self):
        return self.aplicacion.validar_usuario_logueado()
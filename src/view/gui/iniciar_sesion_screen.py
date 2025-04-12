from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.usuario import Usuario

Builder.load_file("src/view/gui/kv/iniciar_sesion_screen.kv")

class IniciarSesionScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def iniciar_sesion(self):
        nombre_usuario = self.ids.nombre_input.text.strip()
        contrasena_usuario = self.ids.contrasena_input.text.strip()

        if self.controlador.iniciar_sesion(nombre_usuario, contrasena_usuario):
            self.manager.current = "Menu2Screen"
            
    def registrarse(self):
        self.manager.current = "CrearCuentaScreen"

    def cerrar_sesion(self):
        self.manager.current = "MainScreen"

    def salir(self):
        exit()
from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/main_screen.kv")

class MainScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador

    
    def abrir_pantalla_crear_cuenta(self):
        self.manager.current ="CrearCuentaScreen"

    def abrir_pantalla_iniciar_sesion(self):
        self.manager.current ="IniciarSesionScreen"

    def cambiar_mensaje_de_registro_confirmado(self, nuevo_mensaje):
        self.ids.mensaje.text = nuevo_mensaje

    def cambiar_mensaje_cerrar_sesion(self, nuevo_mensaje):
        self.ids.mensaje.text = nuevo_mensaje

    def salir(self):
        exit()


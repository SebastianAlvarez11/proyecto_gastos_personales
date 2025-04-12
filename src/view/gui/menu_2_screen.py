from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/menu_2_screen.kv")

class Menu2Screen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def realizar_transaccion(self):
        self.manager.current = "RealizarTransaccionScreen"

    def actualizar_transaccion(self):
        self.manager.current = "ActualizarTransaccionScreen"

    def ver_transacciones(self):
        self.manager.current = "VisualizarTransaccionesScreen"


    def cambiar_contrasena(self):
        self.manager.current = "CambiarContrasenaScreen"


    def cerrar_sesion(self):
        main_screen = self.manager.get_screen("MainScreen")
        main_screen.cambiar_mensaje_cerrar_sesion("Bienvenido, seleccione una opción: ")

        self.manager.current = "MainScreen"


    def salir(self):
        exit()

    def cambiar_mensaje_de_realizar_transaccion(self, nuevo_mensaje):
        self.ids.mensaje_menu_2.text = nuevo_mensaje

    def cambiar_mensaje_de_cambio_de_contrasena(self, nuevo_mensaje):
        self.ids.mensaje_menu_2.text = nuevo_mensaje

    
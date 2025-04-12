from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.transacciones import Transacciones

Builder.load_file("src/view/gui/kv/realizar_transaccion_screen.kv")

class RealizarTransaccionScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def crear_transaccion(self):
        transaccion = Transacciones(
            id = len(self.controlador.aplicacion.usuario_logueado.transacciones) + 1,
            cantidad_dinero = float(self.ids.cantidad_dinero_input.text),
            categoria = self.ids.categoria_input.text,
            fecha = self.ids.fecha_input.text,
            hora = self.ids.hora_input.text,
        )

        self.controlador.realizar_transaccion(transaccion)

        menu_2_screen = self.manager.get_screen("Menu2Screen")
        menu_2_screen.cambiar_mensaje_de_realizar_transaccion("Has creado una transacción exitosamente.")

        self.manager.current = "Menu2Screen"

    def volver(self):
        self.manager.current = "Menu2Screen"


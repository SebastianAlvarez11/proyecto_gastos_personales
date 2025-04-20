from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.transacciones import Transacciones

Builder.load_file("src/view/gui/kv/realizar_transaccion_screen.kv")

class RealizarTransaccionScreen(Screen):
    """
     Representa la pantalla realizar transacción utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """
    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa la pantalla realizar transacción con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def crear_transaccion(self):
        """
        Crea una transacción del usuario.
        Returns:
            Se cambia el mensaje y se devuelve a la pantalla menú 2.
        """
        transaccion = Transacciones(
            id = len(self.controlador.aplicacion.obtener_usuario_logueado().obtener_transacciones()) + 1,
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
        """
        Cambia a la pantalla menú 2.
        """
        self.manager.current = "Menu2Screen"


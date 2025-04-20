from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/main_screen.kv")

class MainScreen(Screen):
    """
     Representa la pantalla principal utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """

    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa la pantalla principal con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador

    
    def abrir_pantalla_crear_cuenta(self):
        """
        Cambia a la pantalla crear cuenta.
        """
        self.manager.current ="CrearCuentaScreen"

    def abrir_pantalla_iniciar_sesion(self):
        """
        Cambia a la pantalla iniciar sesión.
        """
        self.manager.current ="IniciarSesionScreen"

    def cambiar_mensaje_de_registro_confirmado(self, nuevo_mensaje):
        """
        Cambia el mensaje cuando el usuario se registra.
        Args:
            nuevo_mensaje: el nuevo mensaje.
        """
        self.ids.mensaje.text = nuevo_mensaje

    def cambiar_mensaje_cerrar_sesion(self, nuevo_mensaje):
        """
        Cambia el mensaje cuando el usuario cierra sesión.
        Args:
            nuevo_mensaje: el nuevo mensaje.
        """
        self.ids.mensaje.text = nuevo_mensaje

    def salir(self):
        """
        Cierra la aplicación.
        """
        exit()


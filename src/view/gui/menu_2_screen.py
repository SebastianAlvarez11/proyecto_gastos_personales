from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/menu_2_screen.kv")

class Menu2Screen(Screen):
    """
     Representa el menú 2 utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """
    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa el menú 2 con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def realizar_transaccion(self):
        """
        Cambia a la pantalla realizar transacción.
        """
        self.manager.current = "RealizarTransaccionScreen"

    def actualizar_transaccion(self):
        """
        Cambia a la pantalla actualizar transacción.
        """
        self.manager.current = "ActualizarTransaccionScreen"

    def ver_transacciones(self):
        """
        Cambia a la pantalla visualizar transacciones.
        """
        self.manager.current = "VisualizarTransaccionesScreen"


    def cambiar_contrasena(self):
        """
        Cambia a la pantalla cambiar contraseña.
        """
        self.manager.current = "CambiarContrasenaScreen"


    def cerrar_sesion(self):
        """
        Cambia a la pantalla main screen.
        Se cambia el mensaje al cerrar sesión.
        """
        main_screen = self.manager.get_screen("MainScreen")
        main_screen.cambiar_mensaje_cerrar_sesion("Bienvenido, seleccione una opción: ")

        self.manager.current = "MainScreen"


    def salir(self):
        """
        Cierra la aplicación.
        """
        exit()

    def cambiar_mensaje_de_realizar_transaccion(self, nuevo_mensaje):
        """
        Cambia el mensaje cuando el usuario realiza una transacción.
        Args:
            nuevo_mensaje: el nuevo mensaje.
        """
        self.ids.mensaje_menu_2.text = nuevo_mensaje

    def cambiar_mensaje_de_cambio_de_contrasena(self, nuevo_mensaje):
        """
        Cambia el mensaje cuando el usuario cambia la contraseña.
        Args:
            nuevo_mensaje: el nuevo mensaje.
        """
        self.ids.mensaje_menu_2.text = nuevo_mensaje

    
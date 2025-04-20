from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.usuario import Usuario

Builder.load_file("src/view/gui/kv/iniciar_sesion_screen.kv")

class IniciarSesionScreen(Screen):
    """
     Representa la pantalla iniciar sesión utilizando Kivy.

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

    def iniciar_sesion(self):
        """
        El usuario inicia sesión con los datos registrados.
        """
        nombre_usuario = self.ids.nombre_input.text.strip()
        contrasena_usuario = self.ids.contrasena_input.text.strip()

        if self.controlador.iniciar_sesion(nombre_usuario, contrasena_usuario):
            self.manager.current = "Menu2Screen"
            
    def registrarse(self):
        """
        Cambia a la pantalla crear cuenta.
        """
        self.manager.current = "CrearCuentaScreen"

    def cerrar_sesion(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"

    def salir(self):
        """
        Cierra la aplicación.
        """
        exit()
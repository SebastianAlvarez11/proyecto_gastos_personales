from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/cambiar_contrasena_screen.kv")

class CambiarContrasenaScreen(Screen):
    """
     Representa la pantalla cambiar contraseña utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """
    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa la pantalla cambiar contraseña con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador

    def cambiar_contrasena(self):
        """
        El usuario cambia la contraseña.
        """
        nueva_contrasena = self.ids.nueva_contrasena_input.text.strip()
        self.controlador.cambiar_contrasena(nueva_contrasena)
        self.ids.mensaje_label.text = "Has cambiado la contraseña exitosamente."

    def volver(self):
        """
        Cambia a la pantalla menú 2.
        """
        self.manager.current = "Menu2Screen"


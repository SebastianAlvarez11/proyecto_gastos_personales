from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder
from src.model.usuario import Usuario

Builder.load_file("src/view/gui/kv/crear_cuenta_screen.kv")

class CrearCuentaScreen(Screen):
    """
     Representa la pantalla crear cuenta utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """
    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa la pantalla crear cuenta con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador
        self.mensaje = None

    def crear_cuenta(self):
        """
        El usuario crea una cuenta.
        Returns:
            Se cambia el mensaje y se cambia a la pantalla principal.
        """
        usuario = Usuario(
            nombre = self.ids.nombre_input.text.strip(),
            tipo_documento = self.ids.tipo_documento_input.text.strip(),
            numero_de_documento = self.ids.numero_de_documento_input.text.strip(),
            contrasena = self.ids.contrasena_input.text.strip(),
            correo = self.ids.correo_input.text.strip(),
            fecha_nacimiento = self.ids.fecha_nacimiento_input.text.strip(),
        )
        self.controlador.crear_cuenta(usuario)

        main_screen = self.manager.get_screen("MainScreen")
        main_screen.cambiar_mensaje_de_registro_confirmado("Te has registrado exitosamente! Inicia Sesión.")

        self.manager.current = "MainScreen"

    def volver(self):
        """
        Cambia a la pantalla principal.
        """
        self.manager.current = "MainScreen"
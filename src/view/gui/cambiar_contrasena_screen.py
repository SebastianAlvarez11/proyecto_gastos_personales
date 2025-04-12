from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/cambiar_contrasena_screen.kv")

class CambiarContrasenaScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador

    def cambiar_contrasena(self):
        nueva_contrasena = self.ids.nueva_contrasena_input.text.strip()
        self.controlador.cambiar_contrasena(nueva_contrasena)
        self.ids.mensaje_label.text = "Has cambiado la contraseña exitosamente."
        
        #menu_2_screen = self.manager.get_screen("Menu2Screen")
        #menu_2_screen.cambiar_mensaje_de_cambio_de_contrasena("Has cambiado la contraseña exitosamente.")

        #self.manager.current = "Menu2Screen"

    def volver(self):
        self.manager.current = "Menu2Screen"


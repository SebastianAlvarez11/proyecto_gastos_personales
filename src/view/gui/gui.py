from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.controlador.app_controlador import AppControlador
from src.view.gui.main_screen import MainScreen
from src.view.gui.crear_cuenta_screen import CrearCuentaScreen
from src.view.gui.iniciar_sesion_screen import IniciarSesionScreen
from src.view.gui.menu_2_screen import Menu2Screen
from src.view.gui.realizar_transaccion_screen import RealizarTransaccionScreen
from src.view.gui.cambiar_contrasena_screen import CambiarContrasenaScreen
from src.view.gui.actualizar_transaccion_screen import ActualizarTransaccionScreen
from src.view.gui.visualizar_transacciones_screen import VisualizarTransaccionesScreen


class GastosPersonalesApp(App):
    def __init__(self, controlador: AppControlador , **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="MainScreen", controlador=self.controlador))
        screen_manager.add_widget(CrearCuentaScreen(name="CrearCuentaScreen", controlador=self.controlador))
        screen_manager.add_widget(IniciarSesionScreen(name="IniciarSesionScreen", controlador=self.controlador))
        screen_manager.add_widget(Menu2Screen(name="Menu2Screen", controlador=self.controlador))
        screen_manager.add_widget(RealizarTransaccionScreen(name="RealizarTransaccionScreen", controlador=self.controlador))
        screen_manager.add_widget(CambiarContrasenaScreen(name="CambiarContrasenaScreen", controlador=self.controlador))
        screen_manager.add_widget(ActualizarTransaccionScreen(name="ActualizarTransaccionScreen", controlador=self.controlador))
        screen_manager.add_widget(VisualizarTransaccionesScreen(name="VisualizarTransaccionesScreen", controlador=self.controlador))
        
        return screen_manager
    

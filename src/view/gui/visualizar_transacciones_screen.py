from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/visualizar_transacciones_screen.kv")

class VisualizarTransaccionesScreen(Screen):
    """
     Representa la pantalla visualizar transacciones utilizando Kivy.

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

    
    def visualizar_transacciones(self):
        """
        El usuario puede visualizar las transacciones realizadas.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            self.ids.mensaje_label.text = "No has iniciado sesión."
            return
        
        fecha_inicial = self.ids.fecha_inicial_input.text.strip()
        fecha_final = self.ids.fecha_final_input.text.strip()

        try:
            transacciones = self.controlador.aplicacion.obtener_usuario_logueado().visualizar_transacciones(fecha_inicial, fecha_final)
            if transacciones:
                resultado = "\n".join(
                    f"{t.fecha} - {t.categoria}: ${t.cantidad_dinero}" for t in transacciones
                )
                self.ids.mensaje_label.text = resultado
            else:
                self.ids.mensaje_label.text = "No hay transacciones en ese rango de fechas."
        except Exception as e:
            self.ids.mensaje_label.text = f"Error: {str(e)}"



    def volver(self):
        """
        Cambia a la pantalla menú 2.
        """
        self.manager.current = "Menu2Screen"
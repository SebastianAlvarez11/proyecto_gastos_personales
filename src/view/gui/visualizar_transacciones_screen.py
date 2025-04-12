from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/visualizar_transacciones_screen.kv")

class VisualizarTransaccionesScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador

    
    def visualizar_transacciones(self):
        if not self.controlador.aplicacion.validar_usuario_logueado():
            self.ids.mensaje_label.text = "No has iniciado sesión."
            return
        
        fecha_inicial = self.ids.fecha_inicial_input.text.strip()
        fecha_final = self.ids.fecha_final_input.text.strip()

        try:
            transacciones = self.controlador.aplicacion.usuario_logueado.visualizar_transacciones(fecha_inicial, fecha_final)
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
        self.manager.current = "Menu2Screen"
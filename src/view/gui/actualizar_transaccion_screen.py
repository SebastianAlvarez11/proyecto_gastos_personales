from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/actualizar_transaccion_screen.kv")

class ActualizarTransaccionScreen(Screen):
    def __init__(self, controlador: AppControlador, **kw):
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def cargar_transacciones(self):
        self.ids.transacciones_spinner.values = self.obtener_lista_de_transacciones()

    def obtener_lista_de_transacciones(self):
        if not self.controlador.aplicacion.validar_usuario_logueado():
            return []

        transacciones = self.controlador.aplicacion.usuario_logueado.transacciones
        return [f"{i+1}. {t.fecha} - {t.categoria}: ${t.cantidad_dinero}" for i, t in enumerate(transacciones)]


    def actualizar_transaccion(self):
        seleccion_index = self.ids.transacciones_spinner.text.split('.')[0]
        if not seleccion_index.isdigit():
            self.ids.mensaje_label.text = "Selecciona una transacción válida."
            return

        seleccion = int(seleccion_index) - 1
        transacciones = self.controlador.aplicacion.usuario_logueado.transacciones

        if seleccion < 0 or seleccion >= len(transacciones):
            self.ids.mensaje_label.text = "Índice fuera de rango."
            return

        transaccion = transacciones[seleccion]
        campo = self.ids.campo_spinner.text
        nuevo_valor = self.ids.nuevo_valor_input.text.strip()

        if campo == "Cantidad de dinero":
            try:
                transaccion.cantidad_dinero = float(nuevo_valor)
                self.ids.mensaje_label.text = f"Cantidad actualizada a ${nuevo_valor}"
            except ValueError:
                self.ids.mensaje_label.text = "Valor inválido para cantidad."
        elif campo == "Categoría":
            transaccion.categoria = nuevo_valor
            self.ids.mensaje_label.text = f"Categoría actualizada a {nuevo_valor}"
        elif campo == "Fecha":
            transaccion.fecha = nuevo_valor
            self.ids.mensaje_label.text = f"Fecha actualizada a {nuevo_valor}"
        elif campo == "Hora":
            transaccion.hora = nuevo_valor
            self.ids.mensaje_label.text = f"Hora actualizada a {nuevo_valor}"
        else:
            self.ids.mensaje_label.text = "Campo no válido."


    def volver(self):
        self.manager.current = "Menu2Screen"
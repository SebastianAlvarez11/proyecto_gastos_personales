from kivy.uix.screenmanager import Screen
from src.controlador.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/actualizar_transaccion_screen.kv")

class ActualizarTransaccionScreen(Screen):
    """
     Representa la pantalla actualizar transacción utilizando Kivy.

     Attributes:
         controlador (AppControlador): Instancia del controlador que gestiona la comunicación entre la vista y el modelo.
     """
    def __init__(self, controlador: AppControlador, **kw):
        """
        Inicializa la pantalla actualizar transacción con una instancia del controlador.

        Args:
            controlador (AppControlador): Objeto que contiene el controlador.
            **kwargs: Argumentos adicionales para la inicialización de la clase base App.
        """
        super().__init__(**kw)
        self.controlador: AppControlador = controlador 

    def cargar_transacciones(self):
        """
        Carga las transacciones realizadas.
        """
        self.ids.transacciones_spinner.values = self.obtener_lista_de_transacciones()

    def obtener_lista_de_transacciones(self):
        """
        Obtiene las transacciones realizadas por el usuario.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            return []

        transacciones = self.controlador.aplicacion.obtener_usuario_logueado().obtener_transacciones()
        return [f"{i+1}. {t.obtener_fecha()} - {t.obtener_categoria()}: ${t.obtener_cantidad_dinero()}" for i, t in enumerate(transacciones)]


    def actualizar_transaccion(self):
        """
        Actualiza las transacciones del usuario.
        """
        seleccion_index = self.ids.transacciones_spinner.text.split('.')[0]
        if not seleccion_index.isdigit():
            self.ids.mensaje_label.text = "Selecciona una transacción válida."
            return

        seleccion = int(seleccion_index) - 1
        transacciones = self.controlador.aplicacion.obtener_usuario_logueado().obtener_transacciones()

        if seleccion < 0 or seleccion >= len(transacciones):
            self.ids.mensaje_label.text = "Índice fuera de rango."
            return

        transaccion = transacciones[seleccion]
        campo = self.ids.campo_spinner.text
        nuevo_valor = self.ids.nuevo_valor_input.text.strip()

        if campo == "Cantidad de dinero":
            try:
                transaccion.actualizar_cantidad_dinero(float(nuevo_valor))
                self.ids.mensaje_label.text = f"Cantidad actualizada a ${nuevo_valor}"
            except ValueError:
                self.ids.mensaje_label.text = "Valor inválido para cantidad."
        elif campo == "Categoría":
            transaccion.actualizar_categoria(nuevo_valor)
            self.ids.mensaje_label.text = f"Categoría actualizada a {nuevo_valor}"
        elif campo == "Fecha":
            transaccion.actualizar_fecha(nuevo_valor)
            self.ids.mensaje_label.text = f"Fecha actualizada a {nuevo_valor}"
        elif campo == "Hora":
            transaccion.actualizar_hora(nuevo_valor)
            self.ids.mensaje_label.text = f"Hora actualizada a {nuevo_valor}"
        else:
            self.ids.mensaje_label.text = "Campo no válido."


    def volver(self):
        """
        Cambia a la pantalla menú 2.
        """
        self.manager.current = "Menu2Screen"
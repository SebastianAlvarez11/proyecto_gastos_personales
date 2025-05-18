from abc import ABC

class IUsuario(ABC):
    def obtener_transacciones(self):
        pass

    def obtener_nombre(self):
        pass

    def obtener_tipo_documento(self):
        pass

    def obtener_numero_documento(self):
        pass

    def obtener_contrasena(self):
        pass

    def obtener_correo(self):
        pass

    def obtener_fecha_nacimiento(self):
        pass

    def realizar_transaccion(self, transaccion):
        pass

    def actualizar_transaccion(self, nueva_transaccion):
        pass

    def visualizar_transacciones(self, fecha_inicial, fecha_final):
        pass

    def graficar_transaccion(self, transacciones, fecha_inicial, fecha_final):
        pass

    def cambiar_contrasena(self, nueva_contrasena):
        pass
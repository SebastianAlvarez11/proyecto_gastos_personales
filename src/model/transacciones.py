from datetime import datetime
from src.model.exception import (ErrorFechaTransaccion, ErrorHoraTransaccion, ErrorTransaccionCantidaConLetras)

class Transacciones:
    """
    Representa las transacciones.
    """
    def __init__(self,id: int, cantidad_dinero: float, categoria: str, fecha: str, hora: str):
        """
        Inicializa una instancia de Transacciones.

        Args:
            id (int): La id de la transacción.
            cantidad_dinero (float): La cantidad de dinero de la transacción.
            categoria (int): La categoria a la que pertenece la transacción.
            fecha (str): La fecha de la transacción.
            hora (str): La hora de la transacción.
        """
        self.id = id
        self.cantidad_dinero = cantidad_dinero
        self.categoria = categoria
        self.fecha = fecha
        self.hora = hora

    def validar_fecha(self):
        """
        Se válida que la fecha de la transacción sea correcta.

        Return:
            True
        """
        self.validar_fecha_de_transaccion()
        if isinstance(self.fecha, datetime):
            return True

    def validar_hora(self):
        """
        Se válida que la hora de la transacción sea correcta.

        Return:
            True
        """
        self.validar_hora_de_transaccion()
        if isinstance(self.hora, datetime):
            return True         
    
    def validar_cantidad_dinero(self):
        """
        Se válida la cantidad de dinero.

        Return:
            True
        """
        self.validar_cantidad_dinero_sin_letras()

    def validar_fecha_de_transaccion(self):
        """
        Se válida que la fecha de la transacción sea correcta.

        Return:
            Error, la fecha de la transacción no es válida.
        """
        try:
            fecha = datetime.strptime(self.fecha, "%d/%m/%Y")
        except ValueError:
            raise ErrorFechaTransaccion()
        if fecha.year > 2026 or fecha.year < 1910:
            raise ErrorFechaTransaccion()      
        
    def validar_hora_de_transaccion(self):
        """
        Se válida que la hora de la transacción sea correcta.

        Return:
            Error, la hora de la transacción no es válida.
        """
        try:
            self.hora = datetime.strptime(self.hora, "%H:%M")
        except ValueError:
            raise ErrorHoraTransaccion()
           
    def validar_cantidad_dinero_sin_letras(self):
        """
        Se válida que la cantidad de dinero de la transacción sea correcta.

        Return:
            Error, la cantidad de dinero no debe contener letras.
        """
        try:
            float(self.cantidad_dinero)
        except ValueError:
            raise ErrorTransaccionCantidaConLetras()
    



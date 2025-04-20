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
        self.__id = id
        self.__cantidad_dinero = cantidad_dinero
        self.__categoria = categoria
        self.__fecha = fecha
        self.__hora = hora

    def obtener_id(self):
        """
        Obtiene el id de la transacción.

        Returns:
            El id de la transacción.
        """
        return self.__id
    
    def obtener_cantidad_dinero(self):
        """
        Obtiene la cantidad de dinero de la transacción.

        Returns:
            La cantidad de dinero de la transacción.
        """
        return self.__cantidad_dinero
    
    def obtener_categoria(self):
        """
        Obtiene la categoria de la transacción.

        Returns:
            La categoria de la transacción.
        """
        return self.__categoria
    
    def obtener_fecha(self):
        """
        Obtiene la fecha de la transacción.

        Returns:
            La fecha de la transacción.
        """
        return self.__fecha

    def obtener_hora(self):
        """
        Obtiene la hora de la transacción.

        Returns:
            La hora de la transacción.
        """
        return self.__hora


    def validar_fecha(self):
        """
        Se válida que la fecha de la transacción sea correcta.

        Return:
            True
        """
        self.validar_fecha_de_transaccion()
        if isinstance(self.__fecha, datetime):
            return True

    def validar_hora(self):
        """
        Se válida que la hora de la transacción sea correcta.

        Return:
            True
        """
        self.validar_hora_de_transaccion()
        if isinstance(self.__hora, datetime):
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
            fecha = datetime.strptime(self.__fecha, "%d/%m/%Y")
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
            self.__hora = datetime.strptime(self.__hora, "%H:%M")
        except ValueError:
            raise ErrorHoraTransaccion()
           
    def validar_cantidad_dinero_sin_letras(self):
        """
        Se válida que la cantidad de dinero de la transacción sea correcta.

        Return:
            Error, la cantidad de dinero no debe contener letras.
        """
        try:
            float(self.__cantidad_dinero)
        except ValueError:
            raise ErrorTransaccionCantidaConLetras()
    

    def actualizar_cantidad_dinero(self, nueva_cantidad_dinero):
        """
        Se actualiza la cantidad de dinero.

        Return:
            La nueva cantidad de dinero.
        """
        self.__cantidad_dinero = nueva_cantidad_dinero

    def actualizar_categoria(self, nueva_categoria):
        """
        Se actualiza la categoria.

        Return:
            La nueva categoria.
        """
        self.__categoria = nueva_categoria

    def actualizar_fecha(self, nueva_fecha):
        """
        Se actualiza la fecha.

        Return:
            La nueva fecha.
        """
        self.__fecha = nueva_fecha

    def actualizar_hora(self, nueva_hora):
        """
        Se actualiza la hora.

        Return:
            La nueva hora.
        """
        self.__hora = nueva_hora

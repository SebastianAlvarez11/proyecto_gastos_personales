from datetime import datetime
from src.model.exception import (ErrorFechaTransaccion, ErrorHoraTransaccion, ErrorTransaccionCantidaConLetras)

class Transacciones:
    def __init__(self,id: int, cantidad_dinero: float, categoria: str, fecha: str, hora: str):
        self.id = id
        self.cantidad_dinero = cantidad_dinero
        self.categoria = categoria
        self.fecha = fecha
        self.hora = hora
        
    def validar_fecha(self):
        if isinstance(self.fecha, datetime):
            return True       
        try:
            fecha = datetime.strptime(self.fecha, "%d/%m/%Y")
        except ValueError:
            raise ErrorFechaTransaccion()
        if fecha.year > 2026 or fecha.year < 1910:
            raise ErrorFechaTransaccion()
        
    def validar_hora(self):
        if isinstance(self.hora, datetime):
            return True
        try:
            self.hora = datetime.strptime(self.hora, "%H:%M")
        except ValueError:
            raise ErrorHoraTransaccion()
        return True
    
    def validar_dinero(self):
        try:
            float(self.cantidad_dinero)
        except ValueError:
            raise ErrorTransaccionCantidaConLetras()
        return True

    def filtrar_fechas(self, fecha_inicial, fecha_final):
        fecha_inicial = datetime.strptime(fecha_inicial, "%d/%m/%Y")
        fecha_final = datetime.strptime(fecha_final, "%d/%m/%Y")

        if fecha_inicial <= self.fecha <= fecha_final:
            return True
        return False

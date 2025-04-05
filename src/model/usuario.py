import matplotlib.pyplot as plt
import pandas as pd
import string
from datetime import datetime, timedelta
from src.model.transacciones import Transacciones
from src.model.exception import (ErrorTipoDocConNumeros, ErrorTipoDocConEspeciales, ErrorContrasenaCorta, ErrorContrasenaVacia,
                                 ErrorTransaccionNoExistente, ErrorTransaccionSinCambios, ErrorVisualizarFechaInicialPosterior,
                                 ErrorVisualizarFechasFormato, ErrorTransaccionCantidadCero, ErrorCrearTransaccionSinDatos, ErrorFechaNoValida,
                                 ErrorCorreoNoValido, ErrorContrasenaNoSegura, ErrorVisualizarSinFechas, ErrorVisualizarSinFechaInicial, ErrorVisualizarSinFechaFinal)
"""
El módulo se encarga de el usuario.
"""
class Usuario:
    """
    Representa al Usuario.
    """
    def __init__(self, nombre: str, tipo_documento: str, numero_de_documento: int, contrasena: str, correo: str, fecha_nacimiento):
        """
        Inicializa una instancia de Usuario.

        Args:
            nombre (str): El nombre de l usuario.
            tipo_de_documento (str): El tipo de documento del usuario.
            numero_de_documento (int): El número de documento del usuario.
            contrasena (str): La contraseña del usuario.
            correo (str): El correo del usuario.
            fecha_nacimiento (str): La fecha de nacimiento del usuario.
        """
        self.transacciones:list[Transacciones] = []
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_de_documento
        self.contrasena = contrasena
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento

    def realizar_transaccion(self, transaccion: Transacciones):
        """
        El usuario realiza una transacción.

        Args:
            transaccion (Transacciones): El usuario realiza una transacción.

        Return:
            Se añade la transacción del usuario.
        """

        self.validar_realizar_transaccion_cantidad_cero(transaccion)
        self.validar_realizar_transaccion_sin_datos(transaccion)
        transaccion.validar_fecha()
        transaccion.validar_hora()
        transaccion.validar_cantidad_dinero()
        self.transacciones.append(transaccion)

    def actualizar_transaccion(self, nueva_transaccion: Transacciones):
        """
        El usuario actualiza una transacción existente.

        Args:
            nueva_transaccion(Transacciones): El usuario realiza la nueva transacción.

        Return:
            Se actualiza la transacción nueva por la transacción anterior.
        """
        self.validar_actualizar_transaccion_cantidad_cero(nueva_transaccion)
        nueva_transaccion.validar_fecha()
        nueva_transaccion.validar_hora()

        for i in range(len(self.transacciones)):
            transaccion_actual = self.transacciones[i]
            if (transaccion_actual.categoria == nueva_transaccion.categoria and
                transaccion_actual.fecha == nueva_transaccion.fecha and
                transaccion_actual.hora == nueva_transaccion.hora):
                if (transaccion_actual.cantidad_dinero == nueva_transaccion.cantidad_dinero):
                    raise ErrorTransaccionSinCambios() 
                
            for transaccion in self.transacciones:
                if transaccion.id == nueva_transaccion.id:
                    transaccion.cantidad_dinero = nueva_transaccion.cantidad_dinero
                    transaccion.categoria = nueva_transaccion.categoria
                    transaccion.fecha = nueva_transaccion.fecha
                    transaccion.hora = nueva_transaccion.hora 
                    return True
            
        raise ErrorTransaccionNoExistente()
    
    def visualizar_transacciones(self, fecha_inicial, fecha_final):
        """
        El usuario puede visualizar las transacciones dentro de unas fechas específicas.

        Args:
            fecha_inicial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.
            
        Return:
            El usuario puede visualizar sus transacciones en las fechas dadas.
        """
        self.validar_visualizar_transacciones_sin_fechas(fecha_inicial, fecha_final)
        self.validar_visualizar_transacciones_sin_fecha_inicial(fecha_inicial, fecha_final)
        self.validar_visualizar_transacciones_sin_fecha_final(fecha_inicial, fecha_final)
        self.validar_visualizar_transacciones_fecha_inicial_posterior(fecha_inicial, fecha_final)
        self.validar_visualizar_transaccion_formato_de_fechas(fecha_inicial, fecha_final)
        
        if isinstance(fecha_inicial, str):
                fecha_inicial = datetime.strptime(fecha_inicial, "%d/%m/%Y")
        if isinstance(fecha_final, str): 
                fecha_final = datetime.strptime(fecha_final, "%d/%m/%Y")

        transacciones_filtradas = [
            t for t in self.transacciones if fecha_inicial <= datetime.strptime(t.fecha, "%d/%m/%Y") <= fecha_final
        ]
        return transacciones_filtradas
    
    def graficar_transacciones(self, fecha_inicial, fecha_final):
        """
        El usuario puede graficar las transacciones dentro de unas fechas específicas.

        Args:
            fecha_inicial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.
            
        Return:
            Se muestra una gráfica al usuario de sus transacciones en las fecha dadas.
        """
        transacciones_filtradas = self.visualizar_transacciones(fecha_inicial, fecha_final)
        
        data = {'Categoria': [], 'Cantidad de dinero': []}
        
        for trans in transacciones_filtradas:
            tipo = 'Ingreso' if trans.cantidad_dinero > 0 else 'Gasto'
            data['Categoria'].append(f"{trans.categoria} - {tipo}")
            data['Cantidad de dinero'].append(trans.cantidad_dinero)

        df = pd.DataFrame(data)

        df_agrupado = df.groupby(['Categoria']).sum().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.bar(df_agrupado['Categoria'], df_agrupado['Cantidad de dinero'], color=['green' if x > 0 else 'red' for x in df_agrupado['Cantidad de dinero']])

        ax.set_title(f'Transacciones de {self.nombre} entre {fecha_inicial} y {fecha_final}', fontsize=14)
        ax.set_xlabel('Categoría', fontsize=12)
        ax.set_ylabel('Cantidad de dinero ($)', fontsize=12)

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def validar_realizar_transaccion_cantidad_cero(self, transaccion):
        """
        Se válida que la cantidad de dinero no sea 0.

        Args:
            transaccion: La transacción de el usuario.

        Return:
            Error, la cantidad de dinero debe ser diferente a 0.
        """
        if transaccion.cantidad_dinero == 0:
            raise ErrorTransaccionCantidadCero()
        
    def validar_realizar_transaccion_sin_datos(self, transaccion):
        """
        Se válida que la transacción no este vacía.

        Args:
            transaccion: La transacción de el usuario.

        Return:
            Error al crear transacción, faltan datos.
        """
        if not transaccion.cantidad_dinero or not transaccion.categoria or not transaccion.fecha or not transaccion.hora:
            raise ErrorCrearTransaccionSinDatos()        
    
    def validar_actualizar_transaccion_cantidad_cero(self, nueva_transaccion):
        """
        Se válida que la cantidad de dinero no sea 0.

        Args:
            nueva_transaccion: La nueva transacción de el usuario.

        Return:
            Error, la cantidad de dinero debe ser diferente a 0.
        """
        if nueva_transaccion.cantidad_dinero == 0:
            raise ErrorTransaccionCantidadCero()

    def validar_visualizar_transacciones_sin_fechas(self, fecha_inicial, fecha_final):
        """
        Se válida que las fechas no esten vacías.

        Args:
            fecha_inial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.

        Return:
            Error, no se pueden visualizar transacciones sin unas fechas específicas.
        """
        if fecha_inicial == "" and fecha_final == "":
            raise ErrorVisualizarSinFechas()
        
    def validar_visualizar_transacciones_sin_fecha_inicial(self, fecha_inicial, fecha_final):
        """
        Se válida que la fecha inicial no este vacía.

        Args:
            fecha_inial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.

        Return:
            Error, no se pueden visualizar transacciones sin una fecha inicial.
        """
        if not fecha_inicial:
            raise ErrorVisualizarSinFechaInicial()
        
    def validar_visualizar_transacciones_sin_fecha_final(self, fecha_inicial, fecha_final):
        """
        Se válida que la fecha final no este vacía.

        Args:
            fecha_inial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.

        Return:
            Error, no se pueden visualizar transacciones sin una fecha final.
        """
        if not fecha_final:
            raise ErrorVisualizarSinFechaFinal()
        
    def validar_visualizar_transacciones_fecha_inicial_posterior(self, fecha_inicial, fecha_final):
        """
        Se válida que la fecha inicial no sea posterior a la fecha final.

        Args:
            fecha_inial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.

        Return:
            Error, la fecha inicial debe ser antes de la fecha final.
        """
        if fecha_inicial > fecha_final:
            raise ErrorVisualizarFechaInicialPosterior()
        
    def validar_visualizar_transaccion_formato_de_fechas(self, fecha_inicial, fecha_final):
        """
        Se válida que el formato de las fechas se correcto.

        Args:
            fecha_inial: Desde la fecha inicial.
            fecha_final: Hasta la fecha final.

        Return:
            Error, las fechas deben ir en un formato válido.
        """
        try:
            if isinstance(fecha_inicial, str):
                fecha_inicial = datetime.strptime(fecha_inicial, "%d/%m/%Y")
            if isinstance(fecha_final, str): 
                fecha_final = datetime.strptime(fecha_final, "%d/%m/%Y")
        except:
            raise ErrorVisualizarFechasFormato()

    def validar_tipo_documento(self, tipo_documento):
        """
        Se válida el tipo de documento sea correcto.

        Args:
            tipo_documento: El tipo de documento del usuario.

        Return:
            Error, no pueden haber números en el tipo de documento.
            Error, no pueden haber letras especiales en el tipo de documento. 
        """
        if any(char.isdigit() for char in tipo_documento):
            raise ErrorTipoDocConNumeros()
        if any(char in string.punctuation for char in tipo_documento):
            raise ErrorTipoDocConEspeciales()

    def validar_contrasena(self, contrasena):
        """
        Se válida que la contraseña.

        Args:
            contraseña: La contraseña del usuario.
        """
        self.validar_contrasena_vacia(contrasena)
        self.validar_contrasena_corta(contrasena)
        self.validar_contrasena_no_segura(contrasena)
    
    def validar_contrasena_vacia(self, contrasena):
        """
        Se válida que la contraseña no este vacía.

        Args:
            contraseña: La contraseña del usuario.

        Return:
            Error, no se puede cambiar la contraseña por una contraseña vacía.\nIntentelo nuevamente.
        """
        if contrasena == "":
            raise ErrorContrasenaVacia()
    
    def validar_contrasena_corta(self, contrasena):
        """
        Se válida que la contraseña no sea muy corta.

        Args:
            contraseña: La contraseña del usuario.

        Return:
            Error, la contraseña es muy corta.\nIntentelo nuevamente.
        """
        if len(contrasena) < 8:
            raise ErrorContrasenaCorta()
        
    def validar_contrasena_no_segura(self, contrasena):
        """
        Se válida que la contraseña sea segura.

        Args:
            contraseña: La contraseña del usuario.

        Return:
            Error, la contraseña debe contener al menos un número, una letra mayúscula y una letra especial.
        """
        if not any(char.isdigit() for char in contrasena):
            raise ErrorContrasenaNoSegura()
        if not any(char.isupper() for char in contrasena):
            raise ErrorContrasenaNoSegura()
        if not any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`' for char in contrasena):
            raise ErrorContrasenaNoSegura()

    def validar_correo(self, correo):
        """
        Se válida el correo.

        Args:
            correo: El correo del usuario.

        Return:
            Error, el correo debe contener @.
        """
        if '@' not in correo or '.' not in correo.split('@')[-1]:
            raise ErrorCorreoNoValido()

    def validar_fecha_nacimiento(self, fecha_nacimiento):
        """
        Se válida la fecha de nacimiento.

        Args:
            fecha_nacimiento: La fecha de nacimiento del usuario.

        Return:
            Error, fecha no válida.
        """
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            if fecha_nacimiento > datetime.now():
                raise ErrorFechaNoValida()
            
            edad = datetime.now() - fecha_nacimiento
            if edad > timedelta(days=100 * 365):
                raise ErrorFechaNoValida()
            return True
        except:
            raise ErrorFechaNoValida()
        

        



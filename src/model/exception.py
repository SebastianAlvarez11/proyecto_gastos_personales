class ErrorInicioSesionContrasenaIncorrecta(Exception):
    def __init__(self):
        super().__init__(f"Error, contraseña incorrecta.")

class ErrorInicioSesionUsuarioNoExistente(Exception):
    def __init__(self):
        super().__init__(f"Error, no existe un usuario registrado.")

class ErrorInicioSesionActivo(Exception):
    def __init__(self):
        super().__init__(f"Error, el usuario ya está autenticado.")

class ErrorUsuarioExistente(Exception):
    def __init__(self):
        super().__init__(f"Error, el usuario ya existe.")

class ErrorTipoDocConNumeros(Exception):
    def __init__(self):
        super().__init__(f"Error, no pueden haber números en el tipo de documento.")

class ErrorTipoDocConEspeciales(Exception):
    def __init__(self):
        super().__init__(f"Error, no pueden haber letras especiales en el tipo de documento.")
    
class ErrorFechaTransaccion(Exception):
    def __init__(self):
        super().__init__(f"Error, la fecha de la transacción no es válida.")
    
class ErrorCrearTransaccionSinDatos(Exception):
    def __init__(self):
        super().__init__(f"Error al crear transacción, faltan datos.")

class ErrorHoraTransaccion(Exception):
    def __init__(self):
        super().__init__(f"Error, la hora de la transacción no es válida.")

class ErrorContrasenaCorta(Exception):
    def __init__(self):
        super().__init__(f"Error, la contraseña es muy corta.\nIntentelo nuevamente.")

class ErrorContrasenaIgual(Exception):
    def __init__(self):
        super().__init__(f"Error, no se puede cambiar la contraseña ya que es igual a la contraseña antigua.\nIntentelo nuevamente")

class ErrorContrasenaVacia(Exception):
    def __init__(self):
        super().__init__(f"Error, no se puede cambiar la contraseña por una contraseña vacía.\nIntentelo nuevamente.")

class ErrorTransaccionSinLoguearse(Exception):
    def __init__(self):
        super().__init__(f"Error, debe iniciar sesión para poder actualizar una transacción.")

class ErrorTransaccionNoExistente(Exception):
    def __init__(self):
        super().__init__(f"Error, no existe una transacción.")

class ErrorTransaccionSinCambios(Exception):
    def __init__(self):
        super().__init__(f"Error, la transacción nueva no tiene cambios.")

class ErrorVisualizarSinLoguearse(Exception):
    def __init__(self):
        super().__init__(f"Error, debe iniciar sesión para poder visualizar las transacciones.")

class ErrorVisualizarFechaInicialPosterior(Exception):
    def __init__(self):
        super().__init__(f"Error, la fecha inicial debe ser antes de la fecha final.")

class ErrorVisualizarFechasFormato(Exception):
    def __init__(self):
        super().__init__(f"Error, las fechas deben ir en un formato válido.")

class ErrorTransaccionCantidadCero(Exception):
    def __init__(self):
        super().__init__(f"Error, la cantidad de dinero debe ser diferente a 0.")

class ErrorTransaccionCantidaConLetras(Exception):
    def __init__(self):
        super().__init__(f"Error, la cantidad de dinero no debe contener letras.")

class ErrorVisualizarSinFechas(Exception):
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin unas fechas específicas.")

class ErrorVisualizarSinFechaInicial(Exception):
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin una fecha inicial.")

class ErrorVisualizarSinFechaFinal(Exception):
    def __init__(self):
        super().__init__(f"Error, no se pueden visualizar transacciones sin una fecha final.")

class ErrorIniciarSesionSinNombre(Exception):
    def __init__(self):
        super().__init__(f"Error, no se puede iniciar sesión sin un nombre.")

class ErrorMuchosIntentosFallidos(Exception):
    def __init__(self):
        super().__init__(f"Error, demasiados intentos fallidos, usuario bloqueado.")

class ErrorSistemaCaido(Exception):
    def __init__(self):
        super().__init__(f"Error, por favor intente más tarde.")

class ErrorFechaNoValida(Exception):
    def __init__(self):
        super().__init__(f"Error, la edad es demasiado avanzada.")

class ErrorCorreoNoValido(Exception):
    def __init__(self):
        super().__init__(f"Error, el correo debe contener @.")

class ErrorContrasenaNoSegura(Exception):
    def __init__(self):
        super().__init__(f"Error, la contraseña debe contener al menos un número, una letra y una letra especial.")

class ErrorContrasenaIntentosFallidos(Exception):
    def __init__(self):
        super().__init__(f"Error, demasiados intentos fallidos, intente más tarde.")



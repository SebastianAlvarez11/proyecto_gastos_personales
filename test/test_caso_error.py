import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion
from src.model.exception import (ErrorUsuarioExistente, ErrorTipoDocConNumeros, ErrorTipoDocConEspeciales, ErrorFechaTransaccion, ErrorHoraTransaccion,ErrorInicioSesionContrasenaIncorrecta, ErrorTransaccionCantidaConLetras, 
                                ErrorInicioSesionUsuarioNoExistente, ErrorInicioSesionActivo, ErrorContrasenaCorta, ErrorContrasenaIgual, ErrorContrasenaVacia,ErrorTransaccionSinLoguearse, ErrorTransaccionNoExistente, 
                                ErrorTransaccionSinCambios, ErrorVisualizarSinLoguearse, ErrorVisualizarFechaInicialPosterior, ErrorVisualizarFechasFormato)


def test_caso_error_1():
    app: Aplicacion = Aplicacion()
    with pytest.raises(ErrorInicioSesionUsuarioNoExistente):
        app.iniciar_sesion("Luis", "43Ffrf2")

def test_caso_error_2():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de identidad", 239324221, "43Ffrf26_", "luish123@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    contraseña_incorrecta = "134ferr_"
    with pytest.raises(ErrorInicioSesionContrasenaIncorrecta):
        app.iniciar_sesion("Luis", contraseña_incorrecta)
        
def test_caso_error_3():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de identidad", 239324221, "43Ffrf2.", "luish123@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luis", "43Ffrf2.")
    with pytest.raises(ErrorInicioSesionActivo):
        app.iniciar_sesion("Luis", "43Ffrf2.") 

def test_caso_error_4():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "43Ffrf2.", "carlossht09@gmail.com", "09/05/1989")
    app.crear_cuenta(usuario)
    with pytest.raises(ErrorUsuarioExistente):
        app.crear_cuenta(usuario)
        
def test_caso_error_5():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "c34dul", 12323, "43Ffrf2.", "juann_123@gmail.com", "09/05/1988")
    with pytest.raises(ErrorTipoDocConNumeros):
        app.crear_cuenta(usuario)
        
def test_caso_error_6():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "c*+--ss", 154432, "43Ffrf2.","juann_123@gmail.com", "09/05/1978")
    with pytest.raises(ErrorTipoDocConEspeciales):
        app.crear_cuenta(usuario)

def test_caso_error_7():
    app:Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de identidad", 239324221, "43Ffrf2.", "luish123@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luis", "43Ffrf2.")
    transaccion: Transacciones = Transacciones(1, 20000, "pago", "34/15/1900", "9:30")
    with pytest.raises(ErrorFechaTransaccion):
        usuario.realizar_transaccion(transaccion)

def test_caso_error_8():
    app:Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de identidad", 239324221, "43Ffrf2.", "luish123@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luis", "43Ffrf2.")
    transaccion: Transacciones = Transacciones(1, 20000, "pago", "20/08/2024", "28:62")
    with pytest.raises(ErrorHoraTransaccion):
        usuario.realizar_transaccion(transaccion)

def test_caso_error_9():
    app:Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de identidad", 239324221, "43Ffrf2.", "luish123@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luis", "43Ffrf2.")
    transaccion: Transacciones = Transacciones(1, "20000mil", "pago", "20/08/2024", "10:00")
    with pytest.raises(ErrorTransaccionCantidaConLetras):
        usuario.realizar_transaccion(transaccion)

def test_caso_error_10():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    nueva_contrasena = "1234"
    with pytest.raises(ErrorContrasenaCorta):
        app.cambiar_contrasena(nueva_contrasena)

def test_caso_error_11():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    nueva_contrasena = "Qwer1234."
    with pytest.raises(ErrorContrasenaIgual):
        app.cambiar_contrasena(nueva_contrasena)

def test_caso_error_12():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    nueva_contrasena = ""
    with pytest.raises(ErrorContrasenaVacia):
        app.cambiar_contrasena(nueva_contrasena)

def test_caso_error_13():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    transaccion: Transacciones = Transacciones(1, "-20000", "comida", "6/03/2025", "11:40")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, "-10000", "comida", "6/03/2025", "11:40")
    with pytest.raises(ErrorTransaccionSinLoguearse):
        app.actualizar_transaccion(nueva_transaccion)

def test_caso_error_14():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos","Qwer1234.")
    nueva_transaccion: Transacciones = Transacciones(1, "-20000", "comida", "6/03/2025", "11:40")
    with pytest.raises(ErrorTransaccionNoExistente):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_caso_error_15():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, "-20000", "comida", "6/03/2025", "11:40")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, "-20000", "comida", "6/03/2025", "11:40")
    with pytest.raises(ErrorTransaccionSinCambios):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_caso_error_16():
    app:Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    with pytest.raises(ErrorVisualizarSinLoguearse):
        app.visualizar_transacciones("05/01/2025", "05/02/2025")

def test_caso_error_17():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    with pytest.raises(ErrorVisualizarFechaInicialPosterior):
        usuario.visualizar_transacciones("01/03/2025", "01/02/2025")

def test_caso_error_18():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cédula", 23434, "Qwer1234.", "carlossht09@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, "-20000", "comida", "6/02/2025", "11:40")
    usuario.realizar_transaccion(transaccion)
    with pytest.raises(ErrorVisualizarFechasFormato):
        usuario.visualizar_transacciones("01-02-2025", "01-03-2025")
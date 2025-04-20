import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion
from src.model.exception import (ErrorTransaccionCantidadCero, ErrorCrearTransaccionSinDatos, ErrorFechaTransaccion, ErrorHoraTransaccion,
                                 ErrorVisualizarSinFechas, ErrorIniciarSesionSinNombre, ErrorMuchosIntentosFallidos, ErrorSistemaCaido,
                                 ErrorFechaNoValida, ErrorCorreoNoValido, ErrorContrasenaNoSegura, ErrorContrasenaIntentosFallidos,
                                 ErrorVisualizarSinFechaInicial, ErrorVisualizarSinFechaFinal)

def test_transaccion_gran_cantidad_de_dinero_1():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Pepe", "cedula", 220091, "Qwer1234.", "pepe_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Pepe", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, 1000000000, "salario", "30/01/2025", "10:00")
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.obtener_transacciones()) == 1

def test_transaccion_cero_cantidad_2():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Pepe", "cedula", 220091, "Qwer1234.", "pepe_103@gmail.com","09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Pepe", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, 0, "salario", "30/01/2025", "10:00")
    with pytest.raises(ErrorTransaccionCantidadCero):
        usuario.realizar_transaccion(transaccion)

def test_transaccion_sin_datos_3():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com","09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones("","","","","")
    with pytest.raises(ErrorCrearTransaccionSinDatos):
        usuario.realizar_transaccion(transaccion)

def test_actualizar_cero_cantidad_4():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(2, 0,"comida","03/02/2025","9:45")
    with pytest.raises(ErrorTransaccionCantidadCero):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_actualizar_fecha_no_valida_5():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -7000,"comida","03/10/2039","9:45")
    with pytest.raises(ErrorFechaTransaccion):
        usuario.actualizar_transaccion(nueva_transaccion)
    
def test_actualizar_hora_no_valida_6():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(2, -7000,"comida","03/02/2025","39:70")
    with pytest.raises(ErrorHoraTransaccion):
        usuario.actualizar_transaccion(nueva_transaccion)

def test_visualizar_sin_fechas_7():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    with pytest.raises(ErrorVisualizarSinFechas):
        usuario.visualizar_transacciones("","")

def test_visualizar_sin_fecha_inicial_8():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    with pytest.raises(ErrorVisualizarSinFechaInicial):
        usuario.visualizar_transacciones("","03/27/2025")

def test_visualizar_sin_fecha_final_9():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Rio", "Qwer1234.")
    transaccion: Transacciones = Transacciones(1, -10000,"comida","03/02/2025","9:45")
    usuario.realizar_transaccion(transaccion)
    with pytest.raises(ErrorVisualizarSinFechaFinal):
        usuario.visualizar_transacciones("03/02/2025","")

def test_iniciar_sesion_sin_nombre_10():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Qwer1234.", "rrio_103@gmail.com", "09/05/1998")
    app.crear_cuenta(usuario)
    with pytest.raises(ErrorIniciarSesionSinNombre):
        app.iniciar_sesion("", "Qwer1234.")

def test_iniciar_sesion_muchas_veces_fallidas_11():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "Carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.crear_cuenta(usuario)
    for i in range(4):
        try:
            app.iniciar_sesion("Carlos", "402390Ad_")
        except:
            pass
    
    with pytest.raises(ErrorMuchosIntentosFallidos):
        app.iniciar_sesion("Carlos", "Carlitos2_")

def test_iniciar_sesion_sistema_caido_12():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "Carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.crear_cuenta(usuario)
    with pytest.raises(ErrorSistemaCaido):
        app.iniciar_sesion("","")

def test__crear_cuenta_contrasena_muy_larga_13():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345678900qwertyuiopasdfghjklñzxcvbnM.", "fredd1995@gmail.com", "09/05/1998")
    lon = len(app.obtener_usuarios())
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Fred", "12345678900qwertyuiopasdfghjklñzxcvbnM.")
    assert len(app.obtener_usuarios()) == lon+1

def test_crear_cuenta_fecha_muy_antigua_14():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345tY.", "fredd1995@gmail.com", "09/05/1900")
    with pytest.raises(ErrorFechaNoValida):
        app.crear_cuenta(usuario)

def test_crear_cuenta_correo_no_valido_15():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Fred", "cedula", 16564532, "12345tY.", "fredd1995gmail.com", "09/05/1990")
    with pytest.raises(ErrorCorreoNoValido):
        app.crear_cuenta(usuario)

def test_cambiar_contrasena_no_segura_16():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "Carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Carlitos1_")
    nueva_contrasena = "carlos1_"
    with pytest.raises(ErrorContrasenaNoSegura):
        app.cambiar_contrasena(nueva_contrasena)

def test_cambiar_contrasena_demasiados_intentos_fallidos_17():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "Carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Carlitos1_")
    for i in range(4):
        try:
            app.cambiar_contrasena("carlitos1_")
        except:
            pass

    with pytest.raises(ErrorContrasenaIntentosFallidos):      
        app.cambiar_contrasena("Carloss_10")       

def test_cambiar_contrasena_solo_un_numero_18():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 100043134, "Carlitos1_", "carloss130@gmail.com", "10/12/2001")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Carlos", "Carlitos1_")
    nueva_contrasena = "00000000000000000"
    with pytest.raises(ErrorContrasenaNoSegura):
        app.cambiar_contrasena(nueva_contrasena)
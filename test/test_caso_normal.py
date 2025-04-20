import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion

def test_caso_normal_1():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, 50000, "venta", "05/03/2025", "5:40")
    lon = len(usuario.obtener_transacciones())
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.obtener_transacciones()) == lon+1

def test_caso_normal_2():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, -15000, "comida", "05/03/2025", "10:30")
    lon = len(usuario.obtener_transacciones())
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.obtener_transacciones()) == lon+1

def test_caso_normal_3():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, -3400, "transporte", "01/03/2025", "8:30")
    lon = len(usuario.obtener_transacciones())
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.obtener_transacciones()) == lon+1
        
def test_caso_normal_4():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, -3400, "transporte", "01/03/2025", "8:30")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -4000, "transporte", "01/03/2025", "8:30")
    lon = len(usuario.obtener_transacciones())
    usuario.actualizar_transaccion(nueva_transaccion)
    assert len(usuario.obtener_transacciones()) == lon
    
def test_caso_normal_5():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, -8000, "comida", "07/03/2025", "12:30")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -5000, "comida", "07/03/2025", "12:30")
    lon = len(usuario.obtener_transacciones())
    usuario.actualizar_transaccion(nueva_transaccion)
    assert len(usuario.obtener_transacciones()) == lon

def test_caso_normal_6():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "Mdsse12.")
    transaccion: Transacciones = Transacciones(1, 100000, "pago", "05/03/2025", "1:00")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -5000, "comida", "07/03/2025", "12:30")
    lon = len(usuario.obtener_transacciones())
    usuario.actualizar_transaccion(nueva_transaccion)
    assert len(usuario.obtener_transacciones()) == lon

def test_caso_normal_7():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "Mdsse12.", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan","Mdsse12.")
    transaccion: Transacciones = Transacciones(1, -10000, "desayuno", "20/02/2025", "9:00")
    usuario.realizar_transaccion(transaccion)
    transacciones_filtradas = usuario.visualizar_transacciones("10/02/2025", "28/02/2025")
    assert len(transacciones_filtradas) == 1

def test_caso_normal_8():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Mina", "cedula", "123378", "Mdsse12.", "minart001@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Mina","Mdsse12.")
    transaccion1: Transacciones = Transacciones(1, -10000, "desayuno", "20/02/2025", "9:00")
    usuario.realizar_transaccion(transaccion1)
    transaccion2: Transacciones = Transacciones(2, -5000, "transporte", "21/02/2025", "12:00")
    usuario.realizar_transaccion(transaccion2)
    transacciones_filtradas = usuario.visualizar_transacciones("10/02/2025", "28/02/2025")
    assert transacciones_filtradas == [transaccion1, transaccion2]

def test_caso_normal_9():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Mina", "cedula", "123378", "Mdsse12.", "minart001@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Mina","Mdsse12.")
    transaccion1: Transacciones = Transacciones(1, -10000, "desayuno", "20/02/2025", "9:00")
    usuario.realizar_transaccion(transaccion1)
    transaccion2: Transacciones = Transacciones(2, -5000, "transporte", "21/02/2025", "12:00")
    usuario.realizar_transaccion(transaccion2)
    transaccion3: Transacciones = Transacciones(3, 1500000, "salario", "23/02/2025", "10:00")
    usuario.realizar_transaccion(transaccion3)
    transaccion4: Transacciones = Transacciones(4, 50000, "ropa", "26/02/2025", "3:00")
    usuario.realizar_transaccion(transaccion4)
    transacciones_filtradas = usuario.visualizar_transacciones("10/02/2025", "28/02/2025")
    assert len(transacciones_filtradas) == 4
 
def test_caso_normal_10():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Mdsse12.", "carlossht09@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    resultado = app.iniciar_sesion("Carlos", "Mdsse12.")
    if resultado == None:
        assert False

def test_caso_normal_11():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 234341, "Mdsse12.", "carlossht09@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    resultado = app.iniciar_sesion("Carlos","Mdsse12.")
    if resultado  == None:
        assert False
    assert True

def test_caso_normal_12():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "Mdsse12.", "rrio_103@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    nombre_usuario = "Rio"
    contrasena = "Mdsse12."
    resultado = app.iniciar_sesion(nombre_usuario, contrasena)
    assert resultado == True

def test_caso_normal_13():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Mdsse12.", "carlossht09@gmail.com", "11/09/2000")
    lon = len(app.obtener_usuarios())
    app.crear_cuenta(usuario)
    assert len(app.obtener_usuarios()) == lon +1
    
def test_caso_normal_14():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de indentidad", 123499, "Mdsse12.", "luish123@gmail.com", "11/09/2000")
    lon = len(app.obtener_usuarios())
    app.crear_cuenta(usuario)
    assert len(app.obtener_usuarios()) == lon +1

def test_caso_normal_15():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Bon", "cedula", 3788933, "Mdsse12.", "bonn_0101@gmail.com", "11/09/2000")
    lon = len(app.obtener_usuarios())
    app.crear_cuenta(usuario)
    assert len(app.obtener_usuarios()) == lon +1

def test_caso_normal_16():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Bon", "cedula", 3788933, "Mdsse12.", "bonn_0101@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Bon", "Mdsse12.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    if resultado == None:
        assert False
    assert True

def test_caso_normal_17():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Lupe", "cedula", 788931, "Mdsse12.", "luppe_11@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Lupe", "Mdsse12.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    if resultado == None:
        assert False
    assert True
    
def test_caso_normal_18():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luz", "cedula", 708931, "Mdsse12.", "luuzp123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luz", "Mdsse12.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    assert resultado is True



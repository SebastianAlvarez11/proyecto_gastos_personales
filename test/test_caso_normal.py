import pytest
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.model.aplicacion import Aplicacion

def test_caso_normal_1():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, 50000, "venta", "05/03/2025", "5:40")
    lon = len(usuario.transacciones)
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.transacciones) == lon+1

def test_caso_normal_2():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, -15000, "comida", "05/03/2025", "10:30")
    lon = len(usuario.transacciones)
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.transacciones) == lon+1

def test_caso_normal_3():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, -3400, "transporte", "01/03/2025", "8:30")
    lon = len(usuario.transacciones)
    usuario.realizar_transaccion(transaccion)
    assert len(usuario.transacciones) == lon+1
        
def test_caso_normal_4():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, -3400, "transporte", "01/03/2025", "8:30")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -4000, "transporte", "01/03/2025", "8:30")
    usuario.actualizar_transaccion(nueva_transaccion)
    assert usuario.transacciones == [nueva_transaccion]
    

def test_caso_normal_5():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, -8000, "comida", "07/03/2025", "12:30")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -5000, "comida", "07/03/2025", "12:30")
    usuario.actualizar_transaccion(nueva_transaccion)
    assert nueva_transaccion in usuario.transacciones

def test_caso_normal_6():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan", "mdsse")
    transaccion: Transacciones = Transacciones(1, 100000, "pago", "05/03/2025", "1:00")
    usuario.realizar_transaccion(transaccion)
    nueva_transaccion: Transacciones = Transacciones(1, -5000, "comida", "07/03/2025", "12:30")
    usuario.actualizar_transaccion(nueva_transaccion)
    assert len(usuario.transacciones) == 1

def test_caso_normal_7():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Juan", "cedula", "123323", "mdsse", "juann_123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Juan","mdsse")
    transaccion: Transacciones = Transacciones(1, -10000, "desayuno", "20/02/2025", "9:00")
    usuario.realizar_transaccion(transaccion)
    transacciones_filtradas = usuario.visualizar_transacciones("10/02/2025", "28/02/2025")
    assert len(transacciones_filtradas) == 1

def test_caso_normal_8():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Mina", "cedula", "123378", "mdsse", "minart001@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Mina","mdsse")
    transaccion1: Transacciones = Transacciones(1, -10000, "desayuno", "20/02/2025", "9:00")
    usuario.realizar_transaccion(transaccion1)
    transaccion2: Transacciones = Transacciones(2, -5000, "transporte", "21/02/2025", "12:00")
    usuario.realizar_transaccion(transaccion2)
    transacciones_filtradas = usuario.visualizar_transacciones("10/02/2025", "28/02/2025")
    assert transacciones_filtradas == [transaccion1, transaccion2]

def test_caso_normal_9():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Mina", "cedula", "123378", "mdsse", "minart001@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Mina","mdsse")
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
    usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Hola", "carlossht09@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    resultado = app.iniciar_sesion("Carlos", "Hola")
    if resultado == None:
        assert False

def test_caso_normal_11():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 234341, "Hola", "carlossht09@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    resultado = app.iniciar_sesion("Carlos","Hola")
    if resultado  == None:
        assert False
    assert True

def test_caso_normal_12():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Rio", "cédula", 545463777, "023pp", "rrio_103@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    nombre_usuario = "Rio"
    contrasena = "023pp"
    resultado = app.iniciar_sesion(nombre_usuario, contrasena)
    assert resultado == True

def test_caso_normal_13():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Carlos", "cedula", 23434, "Hola", "carlossht09@gmail.com", "11/09/2000")
    lon = len(app.usuarios)
    app.crear_cuenta(usuario)
    assert len(app.usuarios) == lon +1
    
def test_caso_normal_14():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luis", "documento de indentidad", 123499, "Hal123", "luish123@gmail.com", "11/09/2000")
    lon = len(app.usuarios)
    app.crear_cuenta(usuario)
    assert len(app.usuarios) == lon +1

def test_caso_normal_15():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Bon", "cedula", 3788933, "pl0000", "bonn_0101@gmail.com", "11/09/2000")
    lon = len(app.usuarios)
    app.crear_cuenta(usuario)
    assert len(app.usuarios) == lon +1

def test_caso_normal_16():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Bon", "cedula", 3788933, "pl000021.", "bonn_0101@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Bon", "pl000021.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    if resultado == None:
        assert False
    assert True

def test_caso_normal_17():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Lupe", "cedula", 788931, "pl000021.", "luppe_11@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Lupe", "pl000021.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    if resultado == None:
        assert False
    assert True
    
def test_caso_normal_18():
    app: Aplicacion = Aplicacion()
    usuario: Usuario = Usuario("Luz", "cedula", 708931, "pl000021.", "luuzp123@gmail.com", "11/09/2000")
    app.crear_cuenta(usuario)
    app.iniciar_sesion("Luz", "pl000021.")
    nueva_contraseña = "Poll10000."
    resultado = app.cambiar_contrasena(nueva_contraseña)
    assert resultado is True



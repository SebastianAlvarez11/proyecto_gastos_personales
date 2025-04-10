import matplotlib.pyplot as plt
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from controlador.app_controlador import AppControlador

class ConsolaPrueba:
    def __init__(self, controlador: AppControlador):
        self.controlador: AppControlador = controlador 
    
    def mostrar_menu_1(self):
        print("\n--- Menú Principal ---")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")

    def mostrar_menu_2(self):
        print("\n--- Menú del Usuario ---")
        print("1. Realizar transacción")
        print("2. Actualizar transacción")
        print("3. Ver transacciones")
        print("4. Graficar transacciones")
        print("5. Cambiar contraseña")
        print("6. Cerrar sesión")
        print("7. Salir")

    def crear_cuenta(self):
        nombre = input("Nombre del usuario: ")
        tipo_documento = input("Tipo de documento: ")
        numero_documento = int(input("Número de documento: "))
        print("La contraseña debe contener al menos un número, una letra mayúscula y una letra especial.")
        contrasena = input("Contraseña: ")
        correo = input("Correo: ")
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/yyyy): ")
        
        usuario: Usuario = Usuario(nombre, tipo_documento, numero_documento, contrasena, correo, fecha_nacimiento)
        self.controlador.crear_cuenta(usuario)
        print(f"La cuenta se ha creado exitosamente!\nInicie sesión para ver el menú")

    def iniciar_sesion(self):
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        if self.controlador.iniciar_sesion(nombre, contrasena):
            print(f"Ingreso exitoso. Bienvenido!")
        else:
            print("Error al iniciar sesión.")

    def realizar_transaccion(self):
        if not self.controlador.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return


        cantidad_dinero = float(input("Cantidad de dinero (positiva para ingresos, negativa para gastos): "))
        categoria = input("Categoría (por ejemplo, 'Alimentos', 'Transporte'): ")
        fecha = input("Fecha (dd/mm/yyyy): ")
        hora = input("Hora (hh:mm): ")

        transaccion = Transacciones(
            id = len(self.controlador.aplicacion.usuario_logueado.transacciones) + 1,
            cantidad_dinero = cantidad_dinero,
            categoria = categoria,
            fecha = fecha,
            hora = hora
        )

        self.controlador.realizar_transaccion()
        print(f"Transacción de {cantidad_dinero} registrada en la categoría {categoria}.")
    

    def ejecutar(self):
        while True:
            self.mostrar_menu_1()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.controlador.crear_cuenta()
            elif opcion == "2":
                self.controlador.iniciar_sesion()
            elif opcion == "3":
                print("Gracias por usar la aplicacion. Hasta luego!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


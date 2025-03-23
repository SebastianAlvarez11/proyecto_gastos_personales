import matplotlib.pyplot as plt
from src.model.usuario import Usuario
from src.model.transacciones import Transacciones


class Consola:
    def __init__(self, aplicacion):
        self.aplicacion = aplicacion
    
    def mostrar_menu_1(self):
        print("\n--- Menú Principal ---")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")

    def mostrar_menu_2(self):
        print("\n--- Menú de Usuario ---")
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
        contrasena = input("Contraseña: ")
        correo = input("Correo: ")
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/yyyy): ")
        
        usuario: Usuario = Usuario(nombre, tipo_documento, numero_documento, contrasena, correo, fecha_nacimiento)
        self.aplicacion.crear_cuenta(usuario)
    print(f"La cuenta se ha creado exitosamente!\nInicie sesión para ver el menú")
    
    def iniciar_sesion(self):
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        if self.aplicacion.iniciar_sesion(nombre, contrasena):
            print(f"Ingreso exitoso. Bienvenido!")
        else:
            print("Error al iniciar sesión.")

    def realizar_transaccion(self):
        if not self.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
        
        cantidad_dinero = float(input("Cantidad de dinero (positiva para ingresos, negativa para gastos): "))
        categoria = input("Categoría (por ejemplo, 'Alimentos', 'Transporte'): ")
        fecha = input("Fecha (dd/mm/yyyy): ")
        hora = input("Hora (hh:mm): ")

        transaccion = Transacciones(
            id = len(self.aplicacion.usuario_logueado.transacciones) + 1,
            cantidad_dinero = cantidad_dinero,
            categoria = categoria,
            fecha = fecha,
            hora = hora
        )

        self.aplicacion.usuario_logueado.realizar_transaccion(transaccion)
        print(f"Transacción de {cantidad_dinero} registrada en la categoría {categoria}.")


    def actualizar_transaccion(self):
        if not self.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return

        print("--- Transacciones disponibles para actualizar ---")
        transacciones = self.aplicacion.usuario_logueado.transacciones
        if not transacciones:
            print("No tienes transacciones registradas.")
            return

        for i, transaccion in enumerate(transacciones, start=1):
            print(f"{i}. {transaccion.fecha} - {transaccion.categoria}: ${transaccion.cantidad_dinero}")

        try:
            seleccion = int(input("Selecciona el número de la transacción que deseas actualizar: "))
            if seleccion < 1 or seleccion > len(transacciones):
                print("Selección inválida.")
                return

            transaccion_a_actualizar = transacciones[seleccion - 1]

            print(f"Transacción seleccionada: {transaccion_a_actualizar.fecha} - {transaccion_a_actualizar.categoria}: ${transaccion_a_actualizar.cantidad_dinero}")
            
            print("¿Qué deseas actualizar?")
            print("1. Cantidad de dinero")
            print("2. Categoría")
            print("3. Fecha")
            print("4. Hora")
            campo_seleccionado = input("Selecciona el número del campo a actualizar: ")

            if campo_seleccionado == "1":
                nueva_cantidad = float(input("Introduce la nueva cantidad de dinero (positiva para ingresos, negativa para gastos): "))
                transaccion_a_actualizar.cantidad_dinero = nueva_cantidad
                print(f"Cantidad de dinero actualizada a ${nueva_cantidad}")

            elif campo_seleccionado == "2":
                nueva_categoria = input("Introduce la nueva categoría: ")
                transaccion_a_actualizar.categoria = nueva_categoria
                print(f"Categoría actualizada a '{nueva_categoria}'")

            elif campo_seleccionado == "3":
                nueva_fecha = input("Introduce la nueva fecha (dd/mm/yyyy): ")
                transaccion_a_actualizar.fecha = nueva_fecha
                print(f"Fecha actualizada a {nueva_fecha}")

            elif campo_seleccionado == "4":
                nueva_hora = input("Introduce la nueva hora (hh:mm): ")
                transaccion_a_actualizar.hora = nueva_hora
                print(f"Hora actualizada a {nueva_hora}")

            else:
                print("Selección no válida.")

        except ValueError:
            print("Error: Debes ingresar un número válido.")

    
    def ver_transacciones(self):
        if not self.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
        
        fecha_inicial = input("Fecha inicial (dd/mm/yyyy): ")
        fecha_final = input("Fecha final (dd/mm/yyyy): ")
        print("--- Historial de transacciones: ---")
        
        try:
            transacciones = self.aplicacion.usuario_logueado.visualizar_transacciones(fecha_inicial, fecha_final)
            if transacciones:
                for transaccion in transacciones:
                    print(f"{transaccion.fecha} - {transaccion.categoria}: ${transaccion.cantidad_dinero}")
            else:
                print("No hay transacciones en ese rango de fechas.")
        except Exception as e:
            print(f"Error: {str(e)}")
    
    def graficar_transacciones(self):
        if not self.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
        
        fecha_inicial = input("Fecha inicial (dd/mm/yyyy): ")
        fecha_final = input("Fecha final (dd/mm/yyyy): ")

        try:
            transacciones = self.aplicacion.usuario_logueado.visualizar_transacciones(fecha_inicial, fecha_final)
            ingresos = sum(t.cantidad_dinero for t in transacciones if t.cantidad_dinero > 0)
            gastos = sum(t.cantidad_dinero for t in transacciones if t.cantidad_dinero < 0)

            categorias = set(t.categoria for t in transacciones)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.pie([ingresos, abs(gastos)], labels=["Ingresos", "Gastos"], autopct='%1.1f%%', startangle=90)

            ax.axis('equal')  # Para asegurar que sea un gráfico circular
            plt.title(f"Ingresos y Gastos de {fecha_inicial} a {fecha_final}")
            plt.show()
        except Exception as e:
            print(f"Error: {str(e)}")

    def cambiar_contrasena(self):
        if not self.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
        
        nueva_contrasena = input("Introduce la nueva contraseña: ")
        try:
            self.aplicacion.usuario_logueado.validar_contrasena(nueva_contrasena)
            self.aplicacion.usuario_logueado.contrasena = nueva_contrasena
            print("Contraseña cambiada exitosamente.")
        except Exception as e:
            print(f"Error: {str(e)}")


    def cerrar_sesion(self):
        self.aplicacion.cerrar_sesion()
        print("Sesión cerrada.")
    
    def ejecutar(self):
        while True:
            if not self.aplicacion.validar_usuario_logueado():
                self.mostrar_menu_1()
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self.crear_cuenta()
                elif opcion == "2":
                    self.iniciar_sesion()
                elif opcion == "3":
                    print("Gracias por usar la aplicación.")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            else:
                self.mostrar_menu_2()
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    self.realizar_transaccion()
                elif opcion == "2":
                    self.actualizar_transaccion()
                elif opcion == "3":
                    self.ver_transacciones()
                elif opcion == "4":
                    self.graficar_transacciones()
                elif opcion == "5":
                    self.cambiar_contrasena()
                elif opcion == "6":
                    self.cerrar_sesion()
                elif opcion == "7":
                    print("Gracias por usar la aplicación.")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
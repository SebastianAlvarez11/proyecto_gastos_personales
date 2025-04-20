from src.model.usuario import Usuario
from src.model.transacciones import Transacciones
from src.controlador.app_controlador import AppControlador

class Consola:
    """
    Representa el menú principal de la aplicación.

    Attributes:
        controlador (AppControlador): Instancia de la aplicación.
    """

    def __init__(self, controlador: AppControlador):
        """
        Inicializa la aplicación.

        Args:
            controlador (AppControlador): Objeto que contiene la lógica del juego.
        """
        self.controlador: AppControlador = controlador 
    
    def mostrar_menu_1(self):
        """
        Muestra el primer menú al usuario.
        """
        print("\n--- Menú Principal ---")
        print("1. Crear cuenta")
        print("2. Iniciar sesión")
        print("3. Salir")

    def mostrar_menu_2(self):
        """
        Muestra el segundo menú al usuario.
        """
        print("\n--- Menú del Usuario ---")
        print("1. Realizar transacción")
        print("2. Actualizar transacción")
        print("3. Ver transacciones")
        print("4. Cambiar contraseña")
        print("5. Cerrar sesión")
        print("6. Salir")

    def crear_cuenta(self):
        """
        El usuario crea una cuenta.
        """
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
        """
        El usuario inicia sesión con los datos creados.
        """
        nombre = input("Nombre de usuario: ")
        contrasena = input("Contraseña: ")
        if self.controlador.iniciar_sesion(nombre, contrasena):
            print(f"Ingreso exitoso. Bienvenido!")
        else:
            print("Error al iniciar sesión. Nombre o contraseña incorrectos.")

    def realizar_transaccion(self):
        """
        El usuario realiza una transacción.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return


        cantidad_dinero = float(input("Cantidad de dinero (positiva para ingresos, negativa para gastos): "))
        categoria = input("Categoría (por ejemplo, 'Alimentos', 'Transporte'): ")
        fecha = input("Fecha (dd/mm/yyyy): ")
        hora = input("Hora (hh:mm): ")

        transaccion = Transacciones(
            id = len(self.controlador.aplicacion.obtener_usuario_logueado().obtener_transacciones()) + 1,
            cantidad_dinero = cantidad_dinero,
            categoria = categoria,
            fecha = fecha,
            hora = hora
        )

        self.controlador.realizar_transaccion(transaccion)
        print(f"Transacción de {cantidad_dinero} registrada en la categoría {categoria}.")
    

    def actualizar_transaccion(self):
        """
        El usuario actualiza una transacción.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return

        print("--- Transacciones disponibles para actualizar ---")
        transacciones = self.controlador.aplicacion.obtener_usuario_logueado().obtener_transacciones()
        if not transacciones:
            print("No tienes transacciones registradas.")
            return

        for i, transaccion in enumerate(transacciones, start=1):
            print(f"{i}. {transaccion.obtener_fecha()} - {transaccion.obtener_categoria()}: ${transaccion.obtener_cantidad_dinero()}")

        try:
            seleccion = int(input("Selecciona el número de la transacción que deseas actualizar: "))
            if seleccion < 1 or seleccion > len(transacciones):
                print("Selección inválida.")
                return

            transaccion_a_actualizar = transacciones[seleccion - 1]

            print(f"Transacción seleccionada: {transaccion_a_actualizar.obtener_fecha()} - {transaccion_a_actualizar.obtener_categoria()}: ${transaccion_a_actualizar.obtener_cantidad_dinero()}")
            
            print("¿Qué deseas actualizar?")
            print("1. Cantidad de dinero")
            print("2. Categoría")
            print("3. Fecha")
            print("4. Hora")
            campo_seleccionado = input("Selecciona el número del campo a actualizar: ")

            if campo_seleccionado == "1":
                nueva_cantidad = float(input("Introduce la nueva cantidad de dinero (positiva para ingresos, negativa para gastos): "))
                transaccion_a_actualizar.actualizar_cantidad_dinero(nueva_cantidad)
                print(f"Cantidad de dinero actualizada a ${nueva_cantidad}")

            elif campo_seleccionado == "2":
                nueva_categoria = input("Introduce la nueva categoría: ")
                transaccion_a_actualizar.actualizar_categoria(nueva_categoria)
                print(f"Categoría actualizada a '{nueva_categoria}'")

            elif campo_seleccionado == "3":
                nueva_fecha = input("Introduce la nueva fecha (dd/mm/yyyy): ")
                transaccion_a_actualizar.obtener_fecha(nueva_fecha)
                print(f"Fecha actualizada a {nueva_fecha}")

            elif campo_seleccionado == "4":
                nueva_hora = input("Introduce la nueva hora (hh:mm): ")
                transaccion_a_actualizar.obtener_hora(nueva_hora)
                print(f"Hora actualizada a {nueva_hora}")

            else:
                print("Selección no válida.")

        except ValueError:
            print("Error: Debes ingresar un número válido.")

    def ver_transacciones(self):
        """
        El usuario puede ver sus transacciones.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
        
        fecha_inicial = input("Fecha inicial (dd/mm/yyyy): ")
        fecha_final = input("Fecha final (dd/mm/yyyy): ")
        print("--- Historial de transacciones: ---")
        
        try:
            usuario_logueado = self.controlador.aplicacion.obtener_usuario_logueado()
            transacciones = usuario_logueado.visualizar_transacciones(fecha_inicial, fecha_final)
            
            if transacciones:
                for transaccion in transacciones:
                    print(f"{transaccion.obtener_fecha()} - {transaccion.obtener_categoria()}: ${transaccion.obtener_cantidad_dinero()}")
            else:
                print("No hay transacciones en ese rango de fechas.")
        except Exception as e:
            print(f"Error: {str(e)}")

    def cambiar_contrasena(self):
        """
        El usuario puede cambiar la contraseña.
        """
        if not self.controlador.aplicacion.validar_usuario_logueado():
            print("No has iniciado sesión.")
            return
    
        print("La nueva contraseña debe contener al menos un número, una letra mayúscula y una letra especial.")
        nueva_contrasena = input("Introduce la nueva contraseña: ")
        
        try:
            usuario_logueado = self.controlador.aplicacion.obtener_usuario_logueado()
            usuario_logueado.validar_contrasena(nueva_contrasena)
            usuario_logueado.cambiar_contrasena(nueva_contrasena)
            print("Contraseña cambiada exitosamente.")
        except Exception as e:
            print(f"Error: {str(e)}")


    def cerrar_sesion(self):
        """
        El usuario cierra sesión.
        """
        self.controlador.aplicacion.cerrar_sesion()
        print("Sesión cerrada.")
    
    def ejecutar(self):
        """
        Inicia la aplicación y gestiona las opciones seleccionadas por el usuario.
        """
        while True:
            if not self.controlador.validar_usuario_logueado():
                self.mostrar_menu_1()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    self.crear_cuenta()
                elif opcion == "2":
                    self.iniciar_sesion()
                elif opcion == "3":
                    print("Gracias por usar la aplicacion. Hasta luego!")
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
                    self.cambiar_contrasena()
                elif opcion == "5":
                    self.cerrar_sesion()
                elif opcion == "6":
                    print("Gracias por usar la aplicacion. Hasta luego!")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

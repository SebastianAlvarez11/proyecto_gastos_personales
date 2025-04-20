from src.model.usuario import Usuario
from src.model.exception import (ErrorInicioSesionUsuarioNoExistente, ErrorInicioSesionContrasenaIncorrecta, ErrorInicioSesionActivo, ErrorUsuarioExistente,
                                 ErrorContrasenaIgual, ErrorIniciarSesionSinNombre, ErrorMuchosIntentosFallidos, ErrorSistemaCaido, ErrorContrasenaIntentosFallidos,
                                 ErrorTransaccionSinLoguearse, ErrorVisualizarSinLoguearse)

class Aplicacion:
    """
    Representa la Aplicación.
    """
    Maximos_intentos = 3
    Tiempo_de_bloqueo = 300 

    def __init__(self):
        """
        Inicializa una instancia de Aplicacion.
        """
        self.__usuarios: list[Usuario] = []
        self.__intentos_fallidos = {}
        self.__tiempos_de_bloqueo = {}
        self.__usuario_logueado: Usuario = None


    def obtener_usuarios(self):
        """
        Obtiene la lista de usuarios.

        Returns:
            Usuario: objeto que representa al usuario.
        """
        return self.__usuarios
    
    def obtener_intentos_fallidos(self):
        """
        Obtiene la cantidad de intentos fallidos.

        Returns:
            int: Número de intentos fallidos.
        """
        return self.__intentos_fallidos
    
    def obtener_usuario_logueado(self):
        """
        Obtiene si el usuario esta logueado.

        Returns:
            El usuario logueado.
        """
        return self.__usuario_logueado
    
    def crear_cuenta(self, usuario: Usuario):
        """
        Se crea una cuenta en la aplicación.

        Args:
            usuario(Usuario): Los datos del usuario.

        Return:
            El usuario se añade a la lista de usuarios de la aplicación.
        """
        usuario.validar_tipo_documento(usuario.obtener_tipo_documento())
        usuario.validar_fecha_nacimiento(usuario.obtener_fecha_nacimiento())
        usuario.validar_correo(usuario.obtener_correo())
        usuario.validar_contrasena(usuario.obtener_contrasena())
        self.validar_crear_cuenta_usuario_existente(usuario)
        self.__usuarios.append(usuario)

    def iniciar_sesion(self, nombre: str, contrasena: str):
        """
        Se inicia sesión en la aplicación con los datos del usuario.

        Args:
            nombre(str): El nombre del usuario.
            contrasena(str): La contraseña del usuario.

        Return:
            Se inicia sesión en la aplicación.
        """
        self.validar_sistema_funciona(nombre, contrasena)
        self.validar__iniciar_sesion_intentos_fallidos(nombre)
        self.validar_iniciar_sesion_sin_nombre(nombre)
        self.validar_inicio_sesion_activo()

        for usuario in self.__usuarios:
            if usuario.obtener_nombre() == nombre:
                if usuario.obtener_contrasena() == contrasena:
                    self.__usuario_logueado = usuario
                    self.__intentos_fallidos[self.__usuario_logueado.obtener_nombre()] = 0
                    return True
                else:
                    self.__intentos_fallidos[nombre] = self.__intentos_fallidos.get(nombre, 0)+ 1
                    raise ErrorInicioSesionContrasenaIncorrecta()
        raise ErrorInicioSesionUsuarioNoExistente()  
    
    def realizar_transaccion(self, transaccion):
        """
        El usuario realiza una transacción.

        Args:
            transaccion(Transacciones): La transacción del usuario.

        Return:
            Se agrega la transacción a las transacciones del usuario.
        """
        self.validar_usuario_logueado()
        self.obtener_usuario_logueado().realizar_transaccion(transaccion)

    def cambiar_contrasena(self, nueva_contrasena):
        """
        Se cambia la contraseña del usuario.

        Args:
            nueva_contrasena(str): La nueva contraseña del usuario.

        Return:
            Se cambia la nueva contraseña por la antigua.
        """
        self.validar_contrasena_es_igual_a_la_anterior(nueva_contrasena)
        self.validar_intentos_fallidos_cambiar_contrasena()

        try:
            usuario_logueado = self.obtener_usuario_logueado()
            usuario_logueado.validar_contrasena(nueva_contrasena)
        except Exception as exception:
            self.__intentos_fallidos[self.__usuario_logueado.obtener_nombre()] += 1
            raise exception
        
            #if self.tiempos_bloqueo.get(self.usuario_logueado.nombre) and time.time() - self.tiempos_bloqueo[self.usuario_logueado.nombre] < Aplicacion.TIEMPO_BLOQUEO:
            #    raise ErrorContrasenaIntentosFallidos()
            #else:
            #    self.intentos_fallidos[self.usuario_logueado.nombre] = 0
        
        if self.__usuario_logueado:
            self.__usuario_logueado.cambiar_contrasena(nueva_contrasena)
            return True  
        
        self.__intentos_fallidos[self.__usuario_logueado.obtener_nombre()] = 0

        if self.__usuario_logueado.obtener_nombre() in self.tiempos_bloqueo:
            del self.tiempos_bloqueo[self.__usuario_logueado.obtener_nombre()]

    def visualizar_transacciones(self, fecha_inicial, fecha_final):
        """
        El usuario puede visualizar sus transacciones en unas fechas dadas.

        Args:
            fecha_inicial: El usuario da la fecha inicial para ver las transacciones.
            fecha_final: El usuario da la fecha final para ver las transacciones.
            
        Return:
            Se muestran las transacciones en las fechas determinadas.
        """
        if not self.validar_usuario_logueado():
            raise ErrorVisualizarSinLoguearse()  
        self.__usuario_logueado.visualizar_transacciones(fecha_inicial, fecha_final)

    def actualizar_transaccion(self, nueva_transaccion):
        """
        El usuario puede actualizar una transacción.

        Args:
            nueva_transaccion: La nueva transacción del usuario.
            
        Return:
            Se actualiza una transacción antigua por la nueva transacción.
        """
        if not self.validar_usuario_logueado():
            raise ErrorTransaccionSinLoguearse()
        self.__usuario_logueado.actualizar_transaccion(nueva_transaccion)

    def cerrar_sesion(self):
        """
        El usuario cierra sesión de la aplicación.
            
        Return:
            Se cierra la sesión.
        """
        self.__usuario_logueado = None

    def validar_crear_cuenta_usuario_existente(self, usuario):
        """
        Se válida que no exista un usuario existente con esos datos.

        Args:
            usuario: El usuario creado.
            
        Return:
            Error, el usuario ya existe.
        """
        for usuario_existe in self.__usuarios:
            if usuario_existe.obtener_correo() == usuario.obtener_correo():
                raise ErrorUsuarioExistente()

    def validar_sistema_funciona(self, nombre: str, contrasena:str):
        """
        Se válida que el sistema funciones.

        Args:
            nombre: El nombre del usuario.
            contrasena: La contraseña del usuario.
            
        Return:
            Error, por favor intente más tarde.
        """
        if not nombre and not contrasena:
            raise ErrorSistemaCaido()
        
    def validar__iniciar_sesion_intentos_fallidos(self, nombre):
        """
        Se válida los intentos del usuario al iniciar sesión.

        Args:
            nombre: El nombre del usuario.
            
        Return:
            Error, demasiados intentos fallidos, usuario bloqueado.
        """
        if self.__intentos_fallidos.get(nombre, 0) >= Aplicacion.Maximos_intentos:
            raise ErrorMuchosIntentosFallidos()
        
    def validar_iniciar_sesion_sin_nombre(self, nombre):
        """
        Se válida que el usuario escriba su nombre al iniciar sesión.

        Args:
            nombre: El nombre del usuario.
            
        Return:
            Error, no se puede iniciar sesión sin un nombre.
        """
        if not nombre:
            raise ErrorIniciarSesionSinNombre()
        
    def validar_inicio_sesion_activo(self):
        """
        Se válida que el usuario no este logueado.
            
        Return:
            Error, el usuario ya está autenticado.
        """
        if self.__usuario_logueado:
            raise ErrorInicioSesionActivo()

    def validar_contrasena_es_igual_a_la_anterior(self, nueva_contrasena):
        """
        Se válida que la nueva contraseña sea diferente a la antigua contraseña.

        Args:
            nueva_contraseña(str): La nueva contraseña del usuario.
            
        Return:
            Error, no se puede cambiar la contraseña ya que es igual a la contraseña antigua.\nIntentelo nuevamente.
        """
        if self.__usuario_logueado.obtener_contrasena() == nueva_contrasena:
            self.__intentos_fallidos[self.__usuario_logueado.obtener_nombre()] += 1
            raise ErrorContrasenaIgual()
        
    def validar_intentos_fallidos_cambiar_contrasena(self):
        """
        Se válida los intentos del usuario al intentar cambiar la contraseña.
            
        Return:
            Error, no se puede cambiar la contraseña ya que es igual a la contraseña antigua.\nIntentelo nuevamente.
        """
        if self.__intentos_fallidos.get(self.__usuario_logueado.obtener_nombre()) >= Aplicacion.Maximos_intentos:
            raise ErrorContrasenaIntentosFallidos()

    def validar_usuario_logueado(self):
        """
        Se válida que el usuario no este logueado.
            
        Return:
            Se devuelve el usuario logueado.
        """
        return self.__usuario_logueado is not None

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.model.db import Usuarios, Transacciones
from src.model.i_usuario import IUsuario

class UsuarioDB(IUsuario):
    """
        Representa usuario que pueden ser utilizadas en la aplicación.

        Attributes:
            usuarios (list[str]): Lista de usuarios.
    """
    def __init__(self):
        """
            Inicializa una instancia de la clase Usuario, cargando los usuarios desde un archivo.
        """
        url_conexion = "postgresql://alvar:@localhost:5432/proyecto_gastos_personales"
        engine = create_engine(url_conexion, echo=True)
        session = sessionmaker(bind=engine)
        self.data_base_session = session()

    def obtener_usuarios(self, transacciones):
        usuario_seleccionado = self.data_base_session.query(Usuarios).filter(
            Usuarios.transacciones == transacciones).all()

        return usuario_seleccionado
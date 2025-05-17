from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(Text)
    tipo_documento = Column(Text)
    numero_documento = Column(Integer, unique=True)
    contrasena = Column(Text)
    correo = Column(Text)
    fecha_nacimiento = Column(DateTime)
    
    transacciones = relationship('Transacciones', backref='usuarios')


class Transacciones(Base):
    __tablename__ = 'transacciones'

    id = Column(Integer, primary_key=True)
    cantidad_dinero = Column(Float)
    categoria = Column(Text)
    fecha = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey('usuarios.id'))

    usuarios = relationship('Usuarios', backref='transacciones')
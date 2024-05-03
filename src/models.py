import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Empresa(Base):
    __tablename__ = 'empresa'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    ciudad = Column(String(250), nullable=False)
    slogan = Column(String(250), nullable=False)


class Videojuego(Base):
    __tablename__ = 'videojuego'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    precio = Column(Integer, nullable=False)
    empresa_id = Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship(Empresa)


class Plataforma(Base):
    __tablename__ = 'plataforma'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    precio = Column(Integer, nullable=False)


class PlataformaVideojuego(Base):
    __tablename__ = 'plataforma_videojuego'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    plataforma_id = Column(Integer, ForeignKey('plataforma.id'))
    plataforma = relationship(Plataforma)
    videojuego_id = Column(Integer, ForeignKey('videojuego.id'))
    videojuego = relationship(Videojuego)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

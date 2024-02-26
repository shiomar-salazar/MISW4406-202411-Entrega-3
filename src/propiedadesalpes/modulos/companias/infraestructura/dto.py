"""DTOs para la capa de infrastructura del dominio de Companias

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de Companias

"""

from propiedadesalpes.config.db import db


import uuid

Base = db.declarative_base()

# Tabla compania
class Compania(db.Model):
    __tablename__ = "compania"
    id = db.Column(db.String, primary_key=True, nullable=False)
    nombre_compania = db.Column(db.String, nullable=False)
    representante_legal = db.Column(db.String, nullable=False)
    email_contacto = db.Column(db.String, nullable=False)
    telefono_contacto = db.Column(db.String, nullable=False)
    estado = db.Column(db.Enum('Registrado', 'Procesado', name="estado"))
    documento_identidad_id = db.Column(db.Integer, db.ForeignKey('documento_identidad.id'), unique=True)
    documento_identidad = db.relationship('DocumentoIdentidad', back_populates='compania')
    tipo_industria_id = db.Column(db.Integer, db.ForeignKey('tipo_industria.id'), unique=True)
    tipo_industria = db.relationship('TipoIndustria', back_populates='compania')
    
    # Método para convertir objeto SQLAlchemy a diccionario
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    
    
# Tabla documento identidad
class DocumentoIdentidad(db.Model):
    __tablename__ = 'documento_identidad'
    id = db.Column(db.Integer, primary_key=True)
    numero_documento = db.Column(db.String, nullable=False)
    tipo_documento = db.Column(db.String, nullable=False)
    compania = db.relationship('Compania', uselist=False, back_populates='documento_identidad')
    
    # Método para convertir objeto SQLAlchemy a diccionario
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Tabla tipo industria    
class TipoIndustria(db.Model):
    __tablename__ = 'tipo_industria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)  
    compania = db.relationship('Compania', uselist=False, back_populates='tipo_industria')
    
    # Método para convertir objeto SQLAlchemy a diccionario
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
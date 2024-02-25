"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

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
    estado = db.Column(db.Enum('Registrado', 'Procesado'), nullable=False)
    documento_identidad_id = db.Column(db.Integer, db.ForeignKey('documento_identidad.id'), unique=True)
    documento_identidad = db.relationship('DocumentoIdentidad', back_populates='compania')
    tipo_industria_id = db.Column(db.Integer, db.ForeignKey('tipo_industria.id'), unique=True)
    tipo_industria = db.relationship('TipoIndustria', back_populates='compania')
    
# Tabla documento identidad
class DocumentoIdentidad(db.Model):
    __tablename__ = 'documento_identidad'
    id = db.Column(db.Integer, primary_key=True)
    numero_documento = db.Column(db.String, nullable=False)
    tipo_documento = db.Column(db.String, nullable=False)
    compania = db.relationship('Compania', uselist=False, back_populates='documento_identidad')

# Tabla tipo industria    
class TipoIndustria(db.Model):
    __tablename__ = 'tipo_industria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)  
    compania = db.relationship('Compania', uselist=False, back_populates='tipo_industria')
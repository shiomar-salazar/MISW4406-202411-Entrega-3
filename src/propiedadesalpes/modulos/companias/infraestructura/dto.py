from config.db import db
Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla companias e itinerarios
class Compania(db.Model):
    __tablename__ = "compania"
    id = db.Column(db.String, primary_key=True, nullable=False)
    nombre_compania = db.Column(db.String, nullable=True)
    representante_legal = db.Column(db.String, nullable=True)
    email_contacto = db.Column(db.String, nullable=True)
    telefono_contacto = db.Column(db.String, nullable=True)
    estado = db.Column(db.String, nullable=True)
    documento_identidad_numero_identificacion = db.Column(db.String, nullable=True)
    documento_identidad_tipo = db.Column(db.String, nullable=True)
    tipo_industria = db.Column(db.String, nullable=True)
    direccion = db.Column(db.String, nullable=True)
    latitud = db.Column(db.String, nullable=True)
    longitud = db.Column(db.String, nullable=True)
    ciudad = db.Column(db.String, nullable=True)
    pais = db.Column(db.String, nullable=True)

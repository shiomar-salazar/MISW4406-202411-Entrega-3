from config.db import db
Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla companias e itinerarios
class Compania(db.Model):
    __tablename__ = "compania"
    id = db.Column(db.String, primary_key=True, nullable=False)
    nombre_compania = db.Column(db.String, nullable=False)
    representante_legal = db.Column(db.String, nullable=False)
    email_contacto = db.Column(db.String, nullable=False)
    telefono_contacto = db.Column(db.String, nullable=False)
    estado = db.Column(db.Enum('Registrado', 'Procesado', name="estado"))
    documento_identidad_numero_identificacion = db.Column(db.String, nullable=False)
    documento_identidad_tipo = db.Column(db.String, nullable=False)
    tipo_industria = db.Column(db.String, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    latitud = db.Column(db.String, nullable=False)
    longitud = db.Column(db.String, nullable=False)
    ciudad = db.Column(db.String, nullable=False)
    pais = db.Column(db.String, nullable=False)

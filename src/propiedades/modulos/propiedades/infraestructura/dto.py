from config.db import db
Base = db.declarative_base()

# Tabla propiedad
class Propiedad(db.Model):
    __tablename__ = "propiedad"
    id = db.Column(db.String, primary_key=True, nullable=False)
    nombre_propiedad = db.Column(db.String, nullable=True)
    tipo_propiedad = db.Column(db.String, nullable=True)
    pais = db.Column(db.String, nullable=True)
    departamento = db.Column(db.String, nullable=True)
    ciudad = db.Column(db.String, nullable=True)
    direccion = db.Column(db.String, nullable=True)
    latitud = db.Column(db.String, nullable=True)
    longitud = db.Column(db.String, nullable=True)
    codigo_postal = db.Column(db.String, nullable=True)
    area_lote = db.Column(db.DECIMAL, nullable=True)
    estrato_socioeconomico = db.Column(db.String, nullable=True)
    valor_venta = db.Column(db.DECIMAL, nullable=True)
    valor_arriendo_mensual = db.Column(db.DECIMAL, nullable=True)
    moneda = db.Column(db.String, nullable=True)
    propietario = db.Column(db.String, nullable=True)
    arrendatario = db.Column(db.String, nullable=True)
    fecha_ultimo_contrato = db.Column(db.DateTime, nullable=True)
    fecha_expiracion_contrato_actual = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String, nullable=True)
    id_compania = db.Column(db.String, nullable=True)
    id_contrato = db.Column(db.String, nullable=True)
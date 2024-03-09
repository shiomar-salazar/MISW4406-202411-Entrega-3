from config.db import db
Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contrato"
    id = db.Column(db.String, primary_key=True, nullable=False)
    id_propiedad = db.Column(db.String, nullable=False)
    id_compania = db.Column(db.String, nullable=False)
    fecha_inicio = db.Column(db.String, nullable=True)
    fecha_fin = db.Column(db.String, nullable=True)
    fecha_ejecucion = db.Column(db.String, nullable=True)
    monto = db.Column(db.DECIMAL, nullable=True)
    tipo = db.Column(db.String, nullable=True)

    # Indices de la tabla
    idx_id_propiedad = db.Index('idx_id_propiedad', 'id_propiedad')
    idx_id_compania = db.Index('idx_id_compania', 'id_compania')
    idx_propiedad_compania = db.Index('idx_propiedad_compania', 'id_propiedad', 'id_compania')

class Saga_Log(db.Model):
    __tablename__ = "saga_log"
    id = db.Column(db.String, primary_key=True, nullable=False)
    source = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

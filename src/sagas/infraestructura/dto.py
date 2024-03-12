from config.db import db
Base = db.declarative_base()

class Saga_Log(db.Model):
    __tablename__ = "saga_log"
    id = db.Column(db.String, primary_key=True, nullable=False)
    source = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

import traceback
from config.db import db
from modulos.propiedades.dominio.repositorios import RepositorioPropiedades
from modulos.propiedades.infraestructura.dto import Propiedad
from modulos.propiedades.dominio.fabricas import FabricaPropiedades
from modulos.propiedades.infraestructura.excepciones import PropiedadNoEncontradoExcepcion
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MappeadorPropiedad
from uuid import UUID

class RepositorioPropiedadesPostgresSQL(RepositorioPropiedades):
    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    def agregar(self, propiedad: Propiedad):
            propiedad_dto = self._fabrica_propiedades.crear_objeto(propiedad, MappeadorPropiedad())
            db.session.add(propiedad_dto)
    
    def obtener_todos(self) -> list[Propiedad]:
        propiedades_list = db.session.query(Propiedad).all()
        return propiedades_list
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
    
    def obtener_por_id(self, id_propiedad: str) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id_propiedad)).first()  
        return self._fabrica_propiedades.crear_objeto(propiedad_dto, MappeadorPropiedad())
    
    def obtener_por_direccion(self, direccion: str) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(direccion=str(direccion)).first()  
        return self._fabrica_propiedades.crear_objeto(propiedad_dto, MappeadorPropiedad())
    
    def eliminar(self, propiedad: Propiedad):
        db.session.query(PropiedadDTO).filter_by(id=str(propiedad.id_propiedad)).delete()
""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from config.db import db
from modulos.companias.dominio.repositorios import RepositorioCompaniaes
from modulos.companias.dominio.entidades import Compania
from modulos.companias.dominio.fabricas import FabricaCompaniaes
from .dto import Compania as CompaniaDTO
from .mapeadores import MappeadorCompania
from uuid import UUID

class RepositorioCompaniaesPostgresSQL(RepositorioCompaniaes):
    def __init__(self):
        self._fabrica_companias: FabricaCompaniaes = FabricaCompaniaes()

    def agregar(self, compania: Compania):
            compania_dto = self._fabrica_companias.crear_objeto(compania, MappeadorCompania())
            db.session.add(compania_dto)

    
    def obtener_todos(self) -> list[Compania]:
        companias_list = db.session.query(Compania).all()
        return companias_list
    
    def obtener_tipo(self) -> type:
        return Compania.__class__
    
    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self._fabrica_companias.crear_objeto(compania_dto, MappeadorCompania())
    
class RepositorioCompaniaesRedis(RepositorioCompaniaes):
    def __init__(self):
        self._fabrica_companias: FabricaCompaniaes = FabricaCompaniaes()

    def agregar(self, compania: Compania):
        ...
        
from propiedadesalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesalpes.modulos.compañias.infraestructura.repositorios import RepositorioCompanias
from dataclasses import dataclass
from .base import CompaniaQueryBaseHandler
from propiedadesalpes.modulos.compañias.aplicacion.mapeadores import MapeadorCompanias
import uuid

@dataclass
class ObtenerCompania(Query):
    id: str

class ObtenerCompaniaHandler(CompaniaQueryBaseHandler):

    def handle(self, query: ObtenerCompania) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        companias =  self.fabrica_compania.crear_objeto(repositorio, MapeadorCompanias())
        return QueryResultado(resultado=companias)

@query.register(ObtenerCompania)
def ejecutar_query_obtener_reserva(query: ObtenerCompania):
    handler = ObtenerCompaniaHandler()
    return handler.handle(query)
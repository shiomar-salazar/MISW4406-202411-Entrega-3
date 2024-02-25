from propiedadesalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query as query
from propiedadesalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias
from dataclasses import dataclass
from .base import CompaniasQueryBaseHandler
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompania
import uuid

@dataclass
class ObtenerCompanias(Query):
    id: str

class ObtenerCompaniasHandler(CompaniasQueryBaseHandler):

    def handle(self, query: ObtenerCompanias) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        companias =  self.fabrica_compania.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCompania())
        return QueryResultado(resultado=companias)

@query.register(ObtenerCompanias)
def ejecutar_query_obtener_reserva(query: ObtenerCompanias):
    handler = ObtenerCompaniasHandler()
    return handler.handle(query)
from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.companias.dominio.entidades import Compania
from modulos.companias.aplicacion.mapeadores import MapeadorCompania
from modulos.companias.aplicacion.dto import CompaniaDTO
from .base import CompaniaQueryBaseHandler


@dataclass
class ObtenerCompaniaPorDireccion(Query):
    direccion: str

class ObtenerCompaniaHandler(CompaniaQueryBaseHandler):    

    def handle(self, query) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Compania)
        compania = self.fabrica_companias.crear_objeto(vista.obtener_por_direccion(query.direccion), MapeadorCompania())
        return QueryResultado(resultado=compania)


@query.register(ObtenerCompaniaPorDireccion)
def ejecutar_query_obtener_compania(query: ObtenerCompaniaPorDireccion):
    handler = ObtenerCompaniaHandler()
    return handler.handle(query)
from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.contratos.dominio.entidades import Contrato
from modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from modulos.contratos.aplicacion.dto import ContratoDTO
from .base import ContratoQueryBaseHandler


@dataclass
class ObtenerContratoPorIds(Query):
    id_compania: str
    id_propiedad: str

class ObtenerContratoPorIdsHandler(ContratoQueryBaseHandler):

    def handle(self, query) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Contrato)
        contrato = self.fabrica_contratos.crear_objeto(vista.obtener_por_ids(query.id_compania, query.id_propiedad), MapeadorContrato())
        return QueryResultado(resultado=contrato)

@query.register(ObtenerContratoPorIds)
def ejecutar_query_obtener_contrato_por_ids(query: ObtenerContratoPorIds):
    handler = ObtenerContratoPorIdsHandler()
    return handler.handle(query)
from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.contratos.dominio.entidades import Contrato
from modulos.contratos.aplicacion.dto import ContratoDTO
from .base import ContratoQueryBaseHandler


@dataclass
class ObtenerTodasContratos(Query):
    ...

class ObtenerTodasContratosHandler(ContratoQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        contratos_dto = []
        vista = self.fabrica_vista.crear_objeto(Contrato)
        contratos = vista.obtener_todos()

        for contrato in contratos:
            dto = ContratoDTO(
                id_contrato = contrato.id,
                id_propiedad  = contrato.id_propiedad,
                id_compania  = contrato.id_compania,
                fecha_inicio  = contrato.fecha_inicio,
                fecha_fin  = contrato.fecha_fin,
                fecha_ejecucion  = contrato.fecha_ejecucion,
                monto  = contrato.monto,
                tipo  = contrato.tipo,
                )
            contratos_dto.append(dto)
        
        return QueryResultado(resultado=contratos_dto)

@query.register(ObtenerTodasContratos)
def ejecutar_query_obtener_contrato(query: ObtenerTodasContratos):
    handler = ObtenerTodasContratosHandler()
    return handler.handle(query)
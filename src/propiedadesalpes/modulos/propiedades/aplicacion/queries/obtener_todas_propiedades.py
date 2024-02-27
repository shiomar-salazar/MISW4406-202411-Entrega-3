from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.companias.dominio.entidades import Compania
from modulos.companias.aplicacion.dto import CompaniaDTO
from .base import ReservaQueryBaseHandler


@dataclass
class ObtenerTodasCompanias(Query):
    ...

class ObtenerTodasCompaniasHandler(ReservaQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        companias_dto = []
        vista = self.fabrica_vista.crear_objeto(Compania)
        companias = vista.obtener_todos()

        for compania in companias:
            dto = CompaniaDTO(
                id_compania = compania.id_compania,
                nombre_compania  = compania.nombre_compania,
                representante_legal  = compania.representante_legal,
                email_contacto  = compania.email_contacto,
                telefono_contacto  = compania.telefono_contacto,
                estado  = compania.estado,
                documento_identidad_tipo  = compania.documento_identidad_tipo,
                documento_identidad_numero_identificacion  = compania.documento_identidad_numero_identificacion,
                tipo_industria  = compania.tipo_industria,
                direccion  = compania.direccion,
                ciudad  = compania.ciudad,
                pais  = compania.pais,
                latitud  = compania.latitud,
                longitud  = compania.longitud
                )
            companias_dto.append(dto)
        
        return QueryResultado(resultado=companias_dto)

@query.register(ObtenerTodasCompanias)
def ejecutar_query_obtener_compania(query: ObtenerTodasCompanias):
    handler = ObtenerTodasCompaniasHandler()
    return handler.handle(query)
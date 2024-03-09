from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import PropiedadQueryBaseHandler


@dataclass
class ObtenerPropiedadDireccion(Query):    
    direccion: str

class ObtenerPropiedadDireccionHandler(PropiedadQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self,  query) -> QueryResultado:
        vista = self.fabrica_vista.crear_objeto(Propiedad)
        propiedad = vista.obtener_por_direccion(query.direccion)
        return QueryResultado(resultado=propiedad)

@query.register(ObtenerPropiedadDireccion)
def ejecutar_query_obtener_propiedad_direccion(query: ObtenerPropiedadDireccion):
    handler = ObtenerPropiedadDireccionHandler()
    return handler.handle(query)
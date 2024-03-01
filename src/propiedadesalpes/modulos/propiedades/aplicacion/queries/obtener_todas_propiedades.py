from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import PropiedadQueryBaseHandler


@dataclass
class ObtenerTodasPropiedades(Query):
    ...

class ObtenerTodasPropiedadesHandler(PropiedadQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self.fabrica_vista.crear_objeto(Propiedad)
        propiedades = vista.obtener_todos()
        print("=================== ObtenerTodasPropiedadesHandler =========================")
        print(propiedades)

        for propiedad in propiedades:
            dto = PropiedadDTO(
                id_propiedad = propiedad.id,
                nombre_propiedad  = propiedad.nombre_propiedad,
                representante_legal  = propiedad.representante_legal,
                email_contacto  = propiedad.email_contacto,
                telefono_contacto  = propiedad.telefono_contacto,
                estado  = propiedad.estado,
                documento_identidad_tipo  = propiedad.documento_identidad_tipo,
                documento_identidad_numero_identificacion  = propiedad.documento_identidad_numero_identificacion,
                tipo_industria  = propiedad.tipo_industria,
                direccion  = propiedad.direccion,
                ciudad  = propiedad.ciudad,
                pais  = propiedad.pais,
                latitud  = propiedad.latitud,
                longitud  = propiedad.longitud
                )
            propiedades_dto.append(dto)

        print("=================== ObtenerTodasPropiedadesHandler =========================")
        print(propiedades_dto)
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasPropiedades)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasPropiedades):
    handler = ObtenerTodasPropiedadesHandler()
    return handler.handle(query)
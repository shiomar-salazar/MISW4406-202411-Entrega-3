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
        for propiedad in propiedades:
            dto = PropiedadDTO(
                nombre_propiedad = propiedad.nombre_propiedad,
                tipo_propiedad = propiedad.tipo_propiedad,
                pais = propiedad.pais,
                departamento = propiedad.departamento,
                ciudad = propiedad.ciudad,
                direccion = propiedad.direccion,
                latitud = propiedad.latitud,
                longitud = propiedad.longitud,
                codigo_postal = propiedad.codigo_postal,
                area_lote = propiedad.area_lote,
                estrato_socioeconomico = propiedad.estrato_socioeconomico,
                valor_venta = propiedad.valor_venta,
                valor_arriendo_mensual = propiedad.valor_arriendo_mensual,
                moneda = propiedad.moneda,
                propietario = propiedad.propietario,
                arrendatario = propiedad.arrendatario,
                fecha_ultimo_contrato = propiedad.fecha_ultimo_contrato,
                fecha_expiracion_contrato_actual = propiedad.fecha_expiracion_contrato_actual,
                estado = propiedad.estado,
                id_compania = propiedad.id_compania,
                id_contrato = propiedad.id_contrato
            )
            propiedades_dto.append(dto)

        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodasPropiedades)
def ejecutar_query_obtener_propiedad(query: ObtenerTodasPropiedades):
    handler = ObtenerTodasPropiedadesHandler()
    return handler.handle(query)
from dataclasses import dataclass
from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from modulos.propiedades.dominio.entidades import Compania
from modulos.propiedades.aplicacion.dto import CompaniaDTO
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
                fecha_creacion=compania.fecha_creacion,
                fecha_actualizacion=compania.fecha_actualizacion,
                id_compania = compania.id,
                nombre = compania.nombre,
                descripcion = compania.descripcion,
                precio = compania.precio,
                fecha_publicacion = compania.fecha_publicacion,
                fecha_baja= compania.fecha_baja,
                estado= compania.estado,
                tipo= compania.tipo,
                habitaciones= compania.habitaciones,
                banos= compania.banos,
                estacionamientos= compania.estacionamientos,
                superficie= compania.superficie,
                imagen= compania.imagen,
                direccion=compania.direccion)
            companias_dto.append(dto)
        
        return QueryResultado(resultado=companias_dto)

@query.register(ObtenerTodasCompanias)
def ejecutar_query_obtener_compania(query: ObtenerTodasCompanias):
    handler = ObtenerTodasCompaniasHandler()
    return handler.handle(query)
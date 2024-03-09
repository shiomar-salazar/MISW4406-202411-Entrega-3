""" Mapeadores para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from seedwork.dominio.repositorios import Mapeador
from modulos.propiedades.infraestructura.excepciones import PropiedadNoEncontradoExcepcion
from modulos.propiedades.dominio.entidades import Propiedad
from .dto import Propiedad as PropiedadDTO
    
class MappeadorPropiedad(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        print('Mapeador entidad_a_dto')
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = entidad.id,
        propiedad_dto.nombre_propiedad = entidad.nombre_propiedad,
        propiedad_dto.tipo_propiedad = entidad.tipo_propiedad,
        propiedad_dto.pais = entidad.pais,
        propiedad_dto.departamento = entidad.departamento,
        propiedad_dto.ciudad = entidad.ciudad,
        propiedad_dto.direccion = entidad.direccion,
        propiedad_dto.latitud = entidad.latitud,
        propiedad_dto.longitud = entidad.longitud,
        propiedad_dto.codigo_postal = entidad.codigo_postal,
        propiedad_dto.area_lote = entidad.area_lote,
        propiedad_dto.estrato_socioeconomico = entidad.estrato_socioeconomico,
        propiedad_dto.valor_venta = entidad.valor_venta,
        propiedad_dto.valor_arriendo_mensual = entidad.valor_arriendo_mensual,
        propiedad_dto.moneda = entidad.moneda,
        propiedad_dto.propietario = entidad.propietario,
        propiedad_dto.arrendatario = entidad.arrendatario,
        propiedad_dto.fecha_ultimo_contrato = entidad.fecha_ultimo_contrato,
        propiedad_dto.fecha_expiracion_contrato_actual = entidad.fecha_expiracion_contrato_actual,
        propiedad_dto.estado = entidad.estado,
        propiedad_dto.id_compania = entidad.id_compania,
        propiedad_dto.id_contrato = entidad.id_contrato
        return propiedad_dto 
    
    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        print('Mapeador dto_a_entidad')
        print(str(dto))
        try:
            propiedad = Propiedad()
            propiedad.id_propiedad = dto.id,
            propiedad.nombre_propiedad = dto.nombre_propiedad,
            propiedad.tipo_propiedad = dto.tipo_propiedad,
            propiedad.pais = dto.pais,
            propiedad.departamento = dto.departamento,
            propiedad.ciudad = dto.ciudad,
            propiedad.direccion = dto.direccion,
            propiedad.latitud = dto.latitud,
            propiedad.longitud = dto.longitud,
            propiedad.codigo_postal = dto.codigo_postal,
            propiedad.area_lote = dto.area_lote,
            propiedad.estrato_socioeconomico = dto.estrato_socioeconomico,
            propiedad.valor_venta = dto.valor_venta,
            propiedad.valor_arriendo_mensual = dto.valor_arriendo_mensual,
            propiedad.moneda = dto.moneda,
            propiedad.propietario = dto.propietario,
            propiedad.arrendatario = dto.arrendatario,
            propiedad.fecha_ultimo_contrato = dto.fecha_ultimo_contrato,
            propiedad.fecha_expiracion_contrato_actual = dto.fecha_expiracion_contrato_actual,
            propiedad.estado = dto.estado,
            propiedad.id_compania = dto.id_compania,
            propiedad.id_contrato = dto.id_contrato
            return propiedad
        except:
            raise PropiedadNoEncontradoExcepcion
    
    def obtener_tipo(self) -> type:
        return Propiedad.__class__
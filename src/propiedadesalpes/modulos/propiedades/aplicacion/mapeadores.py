import uuid
from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.propiedades.dominio.entidades import Propiedad
from .dto import PropiedadDTO

class MapeadorPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id_propiedad = externo.get("id_propiedad")
        propiedad_dto.nombre_propiedad = externo.get("nombre_propiedad")
        propiedad_dto.tipo_propiedad = externo.get("tipo_propiedad")
        propiedad_dto.pais = externo.get("pais")
        propiedad_dto.departamento = externo.get("departamento")
        propiedad_dto.ciudad = externo.get("ciudad")
        propiedad_dto.direccion = externo.get("direccion")
        propiedad_dto.latitud = externo.get("latitud")
        propiedad_dto.longitud = externo.get("longitud")
        propiedad_dto.codigo_postal = externo.get("codigo_postal")
        propiedad_dto.area_lote = externo.get("area_lote")
        propiedad_dto.estrato_socioeconomico = externo.get("estrato_socioeconomico")
        propiedad_dto.valor_venta = externo.get("valor_venta")
        propiedad_dto.valor_arriendo_mensual = externo.get("valor_arriendo_mensual")
        propiedad_dto.moneda = externo.get("moneda")
        propiedad_dto.propietario = externo.get("propietario")
        propiedad_dto.arrendatario = externo.get("arrendatario")
        propiedad_dto.fecha_ultimo_contrato = externo.get("fecha_ultimo_contrato")
        propiedad_dto.fecha_expiracion_contrato_actual = externo.get("fecha_expiracion_contrato_actual")
        propiedad_dto.estado = externo.get("estado")
        propiedad_dto.id_compania = externo.get("id_compania")
        propiedad_dto.id_contrato = externo.get("id_contrato")
        return propiedad_dto
    
    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__


class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"
    def obtener_tipo(self) -> type:
        return Propiedad.__class__ 
    
    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id_propiedad = entidad.id_propiedad
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
        propiedad = Propiedad()
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
    
    def entidad_a_externo(self, dto: Propiedad) -> dict:
        dto.id_propiedad = str(dto.id_propiedad)
        dto.nombre_propiedad = str(dto.nombre_propiedad)
        dto.tipo_propiedad = str(dto.tipo_propiedad)
        dto.pais = str(dto.pais)
        dto.departamento = str(dto.departamento)
        dto.ciudad = str(dto.ciudad)
        dto.direccion = str(dto.direccion)
        dto.latitud = str(dto.latitud)
        dto.longitud = str(dto.longitud)
        dto.codigo_postal = str(dto.codigo_postal)
        dto.area_lote = str(dto.area_lote)
        dto.estrato_socioeconomico = str(dto.estrato_socioeconomico)
        dto.valor_venta = str(dto.valor_venta)
        dto.valor_arriendo_mensual = str(dto.valor_arriendo_mensual)
        dto.moneda = str(dto.moneda)
        dto.propietario = str(dto.propietario)
        dto.arrendatario = str(dto.arrendatario)
        dto.fecha_ultimo_contrato = str(dto.fecha_ultimo_contrato)
        dto.fecha_expiracion_contrato_actual = str(dto.fecha_expiracion_contrato_actual)
        dto.estado = str(dto.estado)
        dto.id_compania = str(dto.id_compania)
        dto.id_contrato = str(dto.id_contrato)
        return dto.__dict__
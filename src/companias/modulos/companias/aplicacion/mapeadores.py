from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.companias.dominio.entidades import Compania
from .dto import CompaniaDTO

class MapeadorCompaniaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.nombre_compania  = externo.get("nombre_compania")
        compania_dto.representante_legal  = externo.get("representante_legal")
        compania_dto.email_contacto  = externo.get("email_contacto")
        compania_dto.telefono_contacto  = externo.get("telefono_contacto")
        compania_dto.estado  = externo.get("estado")
        compania_dto.documento_identidad_tipo  = externo.get("documento_identidad_tipo")
        compania_dto.documento_identidad_numero_identificacion  = externo.get("documento_identidad_numero_identificacion")
        compania_dto.tipo_industria  = externo.get("tipo_industria")
        compania_dto.direccion  = externo.get("direccion")
        compania_dto.ciudad  = externo.get("ciudad")
        compania_dto.pais  = externo.get("pais")
        compania_dto.latitud  = externo.get("latitud")
        compania_dto.longitud  = externo.get("longitud")
        return compania_dto
    
    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__


class MapeadorCompania(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"
    def obtener_tipo(self) -> type:
        return Compania.__class__ 
    
    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id_compania = str(entidad.id_compania)
        compania_dto.nombre_compania  = entidad.nombre_compania
        compania_dto.representante_legal  = entidad.representante_legal
        compania_dto.email_contacto  = entidad.email_contacto
        compania_dto.telefono_contacto  = entidad.telefono_contacto
        compania_dto.estado  = entidad.estado
        compania_dto.documento_identidad_tipo  = entidad.documento_identidad_tipo
        compania_dto.documento_identidad_numero_identificacion  = entidad.documento_identidad_numero_identificacion
        compania_dto.tipo_industria  = entidad.tipo_industria
        compania_dto.direccion  = entidad.direccion
        compania_dto.ciudad  = entidad.ciudad
        compania_dto.pais  = entidad.pais
        compania_dto.latitud  = entidad.latitud
        compania_dto.longitud  = entidad.longitud
        
        return compania_dto
    
    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania.id_compania = str(dto.id_compania)
        compania.nombre_compania  = dto.nombre_compania
        compania.representante_legal  = dto.representante_legal
        compania.email_contacto  = dto.email_contacto
        compania.telefono_contacto  = dto.telefono_contacto
        compania.estado  = dto.estado
        compania.documento_identidad_tipo  = dto.documento_identidad_tipo
        compania.documento_identidad_numero_identificacion  = dto.documento_identidad_numero_identificacion
        compania.tipo_industria  = dto.tipo_industria
        compania.direccion  = dto.direccion
        compania.ciudad  = dto.ciudad
        compania.pais  = dto.pais
        compania.latitud  = dto.latitud
        compania.longitud  = dto.longitud
        return compania
    
    def entidad_a_externo(self, dto: Compania) -> dict:
        dto._id = str(dto._id)
        dto.nombre_compania  = str(dto.nombre_compania)
        dto.representante_legal  = str(dto.representante_legal)
        dto.email_contacto  = str(dto.email_contacto)
        dto.telefono_contacto  = str(dto.telefono_contacto)
        dto.estado  = str(dto.estado)
        dto.documento_identidad_tipo  = str(dto.documento_identidad_tipo)
        dto.documento_identidad_numero_identificacion  = str(dto.documento_identidad_numero_identificacion)
        dto.tipo_industria  = str(dto.tipo_industria)
        dto.direccion  = str(dto.direccion)
        dto.ciudad  = str(dto.ciudad)
        dto.pais  = str(dto.pais)
        dto.latitud  = str(dto.latitud)
        dto.longitud  = str(dto.longitud)
        return dto.__dict__
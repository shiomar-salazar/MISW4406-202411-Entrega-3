""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from modulos.companias.infraestructura.excepciones import CompaniaNoEncontradaExcepcion
from seedwork.dominio.repositorios import Mapeador
from modulos.companias.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO


    
class MappeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id = entidad.id
        compania_dto.nombre_compania = entidad.nombre_compania
        compania_dto.representante_legal = entidad.representante_legal
        compania_dto.email_contacto = entidad.email_contacto
        compania_dto.telefono_contacto = entidad.telefono_contacto
        compania_dto.estado = entidad.estado
        compania_dto.documento_identidad_numero_identificacion = entidad.documento_identidad_numero_identificacion
        compania_dto.documento_identidad_tipo = entidad.documento_identidad_tipo
        compania_dto.tipo_industria = entidad.tipo_industria
        compania_dto.direccion = entidad.direccion
        compania_dto.latitud = entidad.tipo_industria
        compania_dto.longitud = entidad.tipo_industria
        compania_dto.ciudad = entidad.ciudad
        compania_dto.pais = entidad.pais
        return compania_dto 
    
    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        try:
            compania = Compania()
            compania.id_compania = str(dto.id)
            compania.nombre_compania = dto.nombre_compania
            compania.representante_legal = dto.representante_legal
            compania.email_contacto = dto.email_contacto
            compania.telefono_contacto = dto.telefono_contacto
            compania.estado = dto.estado
            compania.documento_identidad_numero_identificacion = dto.documento_identidad_numero_identificacion
            compania.documento_identidad_tipo = dto.documento_identidad_tipo
            compania.tipo_industria = dto.tipo_industria
            compania.direccion = dto.direccion
            compania.latitud = dto.tipo_industria
            compania.longitud = dto.tipo_industria
            compania.ciudad = dto.ciudad
            compania.pais = dto.pais
            return compania
        except:
            raise CompaniaNoEncontradaExcepcion                
    
    def obtener_tipo(self) -> type:
        return Compania.__class__
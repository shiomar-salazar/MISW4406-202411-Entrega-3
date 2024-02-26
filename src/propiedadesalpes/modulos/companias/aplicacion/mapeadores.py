from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from .dto import CompaniaDTO
from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
            compania_dto = CompaniaDTO()

            return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__


class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'        

    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id = entidad.id
        compania_dto.nombre_compania = entidad.nombre_compania
        compania_dto.representante_legal = entidad.representante_legal
        compania_dto.email_contacto = entidad.email_contacto
        compania_dto.telefono_contacto = entidad.telefono_contacto
        compania_dto.estado = entidad.estado
        
        # DocumentoIdentidad
        if entidad.documento_identidad:
            compania_dto.documento_identidad.tipo = entidad.documento_identidad_tipo
            compania_dto.documento_identidad.numero_identificacion = entidad.documento_identidad_numero_identificacion
        # TipoIndustria
        if entidad.tipo_industria:
            compania_dto.tipo_industria = entidad.tipo_industria.nombre
        
        return CompaniaDTO()

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania.id = dto.id
        compania.nombre_compania = dto.nombre_compania
        compania.representante_legal = dto.representante_legal
        compania.email_contacto = dto.email_contacto
        compania.telefono_contacto = dto.telefono_contacto
        compania.estado = dto.estado
        
        # DocumentoIdentidad
        if dto.documento_identidad:
            compania.documento_identidad_tipo = dto.documento_identidad.tipo
            compania.documento_identidad_numero_identificacion = dto.documento_identidad.numero_identificacion
        # TipoIndustria
        if dto.tipo_industria:
            compania.tipo_industria = dto.tipo_industria.nombre
            
        return compania
    
    def obtener_tipo(self) -> type:
        return Compania.__class__
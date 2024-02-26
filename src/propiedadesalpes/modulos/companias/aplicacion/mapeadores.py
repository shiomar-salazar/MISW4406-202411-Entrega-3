import json
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
        return  [compania.__dict__ for compania in dto]


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

    # Función para convertir de DTO a Entidad
    def dto_a_entidad(self, companiasDto: list) -> Compania:
        print('<================ Aplicacion.MapeadorCompania.dto_a_entidad ================>')
        companias_entidad = []
        for  companiaDto in companiasDto:
            compania = Compania()
            companias_entidad.append(compania.crear_compania(companiaDto) )
        print(companias_entidad)
        print('<================ Aplicacion.MapeadorCompania.dto_a_entidad ================>')
        return companias_entidad

    def obtener_tipo(self) -> type:
        return Compania.__class__
from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from propiedadesalpes.seedwork.dominio.objetos_valor import InformacionGeoespacial, DatosGreograficos, Direccion, Localizacion, TipoIndustria, DocumentoIdentidad, Compania_ov
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

    def entidad_a_dto(self, entidad: Compania_ov) -> CompaniaDTO:
        
        return CompaniaDTO()

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        
        return compania
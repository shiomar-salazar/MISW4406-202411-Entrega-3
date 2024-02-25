from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.seedwork.dominio.objetos_valor import Compania_ov
from .dto import  CompaniaDTO



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

    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania_ov:
        compania = Compania_ov()
        
        return compania
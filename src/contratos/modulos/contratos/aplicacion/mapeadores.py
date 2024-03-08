from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.contratos.dominio.entidades import Contrato
from .dto import ContratoDTO

class MapeadorContratoDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id_propiedad  = externo.get("id_propiedad")
        contrato_dto.id_compania  = externo.get("id_compania")
        contrato_dto.fecha_inicio  = externo.get("fecha_inicio")
        contrato_dto.fecha_fin  = externo.get("fecha_fin")
        contrato_dto.fecha_ejecucion  = externo.get("fecha_ejecucion")
        contrato_dto.monto  = externo.get("monto")
        contrato_dto.tipo  = externo.get("tipo")
        return contrato_dto
    
    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__

class MapeadorContrato(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"
    def obtener_tipo(self) -> type:
        return Contrato.__class__ 
    
    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id_contrato = entidad.id_contrato
        contrato_dto.id_propiedad  = entidad.id_propiedad
        contrato_dto.id_compania  = entidad.id_compania
        contrato_dto.fecha_inicio  = entidad.fecha_inicio
        contrato_dto.fecha_fin  = entidad.fecha_fin
        contrato_dto.fecha_ejecucion  = entidad.fecha_ejecucion
        contrato_dto.monto  = entidad.monto
        contrato_dto.tipo  = entidad.tipo
        return contrato_dto
    
    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato()
        contrato.id_propiedad  = dto.id_propiedad
        contrato.id_compania  = dto.id_compania
        contrato.fecha_inicio  = dto.fecha_inicio
        contrato.fecha_fin  = dto.fecha_fin
        contrato.fecha_ejecucion  = dto.fecha_ejecucion
        contrato.monto  = dto.monto
        contrato.tipo  = dto.tipo
        return contrato
    
    def entidad_a_externo(self, dto: Contrato) -> dict:
        dto._id = str(dto._id)
        dto.id_propiedad  = str(dto.id_propiedad)
        dto.id_compania  = str(dto.id_compania)
        dto.fecha_inicio  = str(dto.fecha_inicio)
        dto.fecha_fin  = str(dto.fecha_fin)
        dto.fecha_ejecucion  = str(dto.fecha_ejecucion)
        dto.monto  = str(dto.monto)
        dto.tipo  = str(dto.tipo)
        return dto.__dict__
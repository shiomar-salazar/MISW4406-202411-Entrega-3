""" Mapeadores para la capa de infrastructura del dominio de contratos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from modulos.contratos.infraestructura.excepciones import ContratoNoEncontradoExcepcion
from seedwork.dominio.repositorios import Mapeador
from modulos.contratos.dominio.entidades import Contrato
from .dto import Contrato as ContratoDTO


    
class MappeadorContrato(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'
    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        contrato_dto = ContratoDTO()
        contrato_dto.id = entidad.id
        contrato_dto.id_propiedad = entidad.id_propiedad
        contrato_dto.id_compania = entidad.id_compania
        contrato_dto.fecha_inicio = entidad.fecha_inicio
        contrato_dto.fecha_fin = entidad.fecha_fin
        contrato_dto.fecha_ejecucion = entidad.fecha_ejecucion
        contrato_dto.monto = entidad.monto
        contrato_dto.tipo = entidad.tipo
        return contrato_dto 
    
    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        try:
            contrato = Contrato()
            contrato.id = dto.id
            contrato.id_propiedad = dto.id_propiedad
            contrato.id_compania = dto.id_compania
            contrato.fecha_inicio = dto.fecha_inicio
            contrato.fecha_fin = dto.fecha_fin
            contrato.fecha_ejecucion = dto.fecha_ejecucion
            contrato.monto = dto.monto
            contrato.tipo = dto.tipo
            return contrato
        except:
            raise ContratoNoEncontradoExcepcion
    
    def obtener_tipo(self) -> type:
        return Contrato.__class__
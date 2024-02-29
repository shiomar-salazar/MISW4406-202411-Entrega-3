from .entidades import Contrato
from .excepciones import TipoObjetoNoExisteEnDominioContratosExcepcion
from seedwork.dominio.repositorios import Mapeador, Repositorio
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.entidades import Entidad
from dataclasses import dataclass



@dataclass
class FabricaContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            contrato: Contrato = mapeador.dto_a_entidad(obj)
            return contrato


""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de contratos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de contratos

"""

from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.contratos.dominio.repositorios import RepositorioContratos
from seedwork.infraestructura.vistas import Vista
from modulos.contratos.dominio.entidades import Contrato
from .repositorios import RepositorioContratosPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioContratos.__class__:
            return RepositorioContratosPostgresSQL()
        else:
            raise ExcepcionFabrica(f"Error fábrica {obj}")
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Contrato:
            return RepositorioContratosPostgresSQL()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
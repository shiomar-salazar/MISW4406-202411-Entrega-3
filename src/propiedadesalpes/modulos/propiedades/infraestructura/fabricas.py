""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de companias

"""

from dataclasses import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from modulos.companias.dominio.repositorios import RepositorioCompanias
from seedwork.infraestructura.vistas import Vista
from modulos.companias.dominio.entidades import Compania
from modulos.companias.infraestructura.vistas import VistaCompania

from .repositorios import RepositorioCompaniasPostgresSQL
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasPostgresSQL()
        else:
            raise ExcepcionFabrica(f"Error fábrica {obj}")
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Compania:
            return VistaCompania()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
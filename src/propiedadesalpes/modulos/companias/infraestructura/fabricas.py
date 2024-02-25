""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio
from propiedadesalpes.modulos.companias.dominio.repositorios import  RepositorioCompanias
from .repositorios import RepositorioCompaniasSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias.__class__:
            return RepositorioCompaniasSQLite()
        else:
            raise ExcepcionFabrica()
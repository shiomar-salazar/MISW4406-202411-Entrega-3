""" Interfaces para los repositorios del dominio de Companias

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de Companias

"""

from abc import ABC
from propiedadesalpes.seedwork.dominio.repositorios import Repositorio

class RepositorioCompanias(Repositorio, ABC):
    ...

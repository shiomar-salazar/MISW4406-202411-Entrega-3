""" Interfaces para los repositorios del dominio de contratos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de contratos

"""

from abc import ABC
from seedwork.dominio.repositorios import Repositorio

class RepositorioContratos(Repositorio, ABC):
    ...

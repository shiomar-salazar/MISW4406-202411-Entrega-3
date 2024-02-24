"""Objetos valor reusables parte del seedwork del proyecto

En este archivo usted encontrará los objetos valor reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Informacion(ABC, ObjetoValor):
    nombre: str
    apellido: str    
    compania: str # persona natural si no representa una compania    
    
@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):    
    nit: str

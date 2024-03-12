

from __future__ import annotations
from dataclasses import dataclass
from dataclasses import dataclass, field
import uuid
from seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class DatosAdicionales():
    propiedad: str = field(default_factory=str) 
    compania: str = field(default_factory=str) 
    

@dataclass
class PropiedadAlpes(AgregacionRaiz):
    contrato: str = field(default_factory=str) 
    datos_dicionales: DatosAdicionales = field(default_factory=str) 
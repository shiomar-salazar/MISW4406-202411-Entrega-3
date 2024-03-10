

from __future__ import annotations
from dataclasses import dataclass
from dataclasses import dataclass, field
import uuid
from seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class PropiedadAlpes(AgregacionRaiz):
    propiedad: str = field(default_factory=str) 
    compania: str = field(default_factory=str) 
    contrato: str = field(default_factory=str) 
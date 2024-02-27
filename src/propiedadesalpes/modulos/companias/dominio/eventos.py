from __future__ import annotations
import array
from dataclasses import dataclass
import uuid
from seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaCreada(EventoDominio):
    id: str = None    
    nombre_compania: str = None
    fecha_creacion: datetime = None

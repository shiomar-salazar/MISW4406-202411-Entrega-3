from __future__ import annotations
from dataclasses import dataclass
import uuid
from seedwork.dominio.eventos import (EventoDominio)

@dataclass
class ContratoCreado(EventoDominio):
    id_contrato: uuid.UUID = None    
    id_propiedad: str = None
    id_compania: str = None    
    fecha_inicio: str = None
    fecha_fin: str = None
    fecha_ejecucion: str = None
    monto: int = None
    tipo: str = None


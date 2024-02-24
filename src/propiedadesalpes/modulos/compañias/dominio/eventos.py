from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime


@dataclass
class CompaniaCreada(EventoDominio):
    nit: str = None    
    compania: str = None
    fecha_creacion: datetime = None

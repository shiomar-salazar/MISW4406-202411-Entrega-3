from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO
import uuid


@dataclass(frozen=False)
class ContratoDTO(DTO):
    id_contrato: uuid.UUID = field(hash=True, default=uuid.uuid4())
    id_propiedad: uuid.UUID = field(hash=True, default=uuid.uuid4())
    id_compania: uuid.UUID = field(hash=True, default=uuid.uuid4())
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)   
    fecha_ejecucion: str = field(default_factory=str) 
    monto: int = field(default_factory=int)
    tipo: str = field(default_factory=str)
from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO

@dataclass(frozen=False)
class ContratoDTO(DTO):
    id_contrato: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    id_compania: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)   
    fecha_ejecucion: str = field(default_factory=str) 
    monto: int = field(default_factory=int)
    tipo: str = field(default_factory=str)
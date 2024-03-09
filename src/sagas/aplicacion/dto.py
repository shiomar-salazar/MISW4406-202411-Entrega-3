from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO

@dataclass(frozen=False)
class SagaLogDTO(DTO):
    id_saga: str = field(default_factory=str)
    source: str = field(default_factory=str)   
    status: str = field(default_factory=str)

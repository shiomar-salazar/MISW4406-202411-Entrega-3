from dataclasses import dataclass, field
from seedwork.aplicacion.dto import DTO

@dataclass(frozen=False)
class CompaniaDTO(DTO):
    id_compania: str = field(default_factory=str)
    nombre_compania: str = field(default_factory=str)   
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=str)    
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad_tipo: str = field(default_factory=str)
    documento_identidad_numero_identificacion: str = field(default_factory=str)
    tipo_industria: str = field(default_factory=str)
    direccion : str = field(default_factory=str)
    ciudad : str = field(default_factory=str)
    pais : str = field(default_factory=str)
    latitud : str = field(default_factory=str)
    longitud: str = field(default_factory=str)
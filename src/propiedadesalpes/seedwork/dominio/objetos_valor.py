from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion
from datetime import datetime

#@dataclass(frozen=True)
class ObjetoValor:
    ...

#@dataclass(frozen=True)
class InformacionGeoespacial(ABC, ObjetoValor):
    latitud: str
    longitud: str

#@dataclass(frozen=True)
class DatosGreograficos(ABC, ObjetoValor):
    ciudad: str
    pais: str

#@dataclass(frozen=True)
class Direccion(ABC, ObjetoValor):
    direccion: str
    datos_geograficos: DatosGreograficos

#@dataclass(frozen=True)
class Localizacion(ABC, ObjetoValor):
    direccion: Direccion
    infromacion_geoespacial: InformacionGeoespacial

#@dataclass(frozen=True)
class TipoIndustria(ABC, ObjetoValor):
    id_industria: str
    nombre: str
    descripcion: str

#@dataclass(frozen=True)
class DocumentoIdentidad(ABC, ObjetoValor):
    tipo: str
    numero_identificacion: str
    
    
#@dataclass(frozen=True)
class Compania_ov(ABC, ObjetoValor):
    id_comp: str
    nombre_compania: str
    representante_legal: str
    email_contacto: str
    telefono_contacto: str
    estado: str
    documento_identidad: DocumentoIdentidad
    tipo_industria: TipoIndustria
    localizacion: Localizacion
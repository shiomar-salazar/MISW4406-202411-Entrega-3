"""Objetos valor reusables parte del seedwork del proyecto

En este archivo usted encontrará los objetos valor reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class InformacionGeoespacial(ABC, ObjetoValor):
    latitud: str
    longitud: str

@dataclass(frozen=True)
class DatosGreograficos(ABC, ObjetoValor):
    ciudad: str
    pais: str

@dataclass(frozen=True)
class Direccion(ABC, ObjetoValor):
    direccion: str
    datos_geograficos: DatosGreograficos

@dataclass(frozen=True)
class Localizacion(ABC, ObjetoValor):
    direccion: Direccion
    infromacion_geoespacial: InformacionGeoespacial

@dataclass(frozen=True)
class TipoIndustria(ABC, ObjetoValor):
    id_industria: str
    nombre: str
    descripcion: str

@dataclass(frozen=True)
class DocumentoIdentidad(ABC, ObjetoValor):
    tipo: str
    numero_identificacion: str
    
@dataclass(frozen=True)
class DocumentoIdentidad(ABC, ObjetoValor):
    tipo: str
    numero_identificacion: str
    
@dataclass(frozen=True)
class Compania_ov(ABC, ObjetoValor):
    id: int
    nombre_compania: str
    representante_legal: str
    email_contacto: str
    telefono_contacto: str
    estado: str
    documento_identidad: DocumentoIdentidad
    tipo_industria: TipoIndustria
    localizacion: Localizacion


    """@abstractmethod
    def origen(self) -> Locacion:
        ...
    
    @abstractmethod
    def destino(self) -> Locacion:
        ...
    
    @abstractmethod
    def fecha_salida(self) -> datetime:
        ...

    @abstractmethod
    def fecha_llegada(self) -> datetime:
        ...
    """

"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Informacion, Ruta, Locacion
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class DodumentoIdentidad(Informacion):
    ...

@dataclass(frozen=True)
class Direccion():
    ...
@dataclass(frozen=True)
class DatosGeograficos():
    ...

@dataclass(frozen=True)
class InformacionGeoespacial():
    ...

@dataclass(frozen=True)
class RepresentanteLegal(Informacion):
    ...
@dataclass(frozen=True)
class Identificacion(Codigo):
    ...    

class TipoIndustria(Enum):
    BODEGA = "Bodega"
    OFICINA = "Oficina"
    PROPIEDAD_COMERCIAL = "Popiedad comercial"
    CENTRO_MEDICO = "Centro medico"
    LABORATORIO = "Laboratorio"

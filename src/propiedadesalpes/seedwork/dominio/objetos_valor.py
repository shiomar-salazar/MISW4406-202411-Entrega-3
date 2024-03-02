from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion

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
class Propiedad_ov(ABC, ObjetoValor):
    id_propiedad: str
    nombre_propiedad: str      
    tipo_propiedad: str   
    pais: str   
    departamento: str   
    ciudad: str   
    direccion: str      
    latitud : str   
    longitud: str   
    codigo_postal: str   
    area_lote: str   
    estrato_socioeconomico: str   
    valor_venta : str   
    valor_arriendo_mensual : str   
    moneda : str   
    propietario : str   
    arrendatario : str   
    fecha_ultimo_contrato : str   
    fecha_expiracion_contrato_actual : str   
    estado : str   
    id_compania : str   
    id_contrato : str
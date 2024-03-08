from __future__ import annotations
from dataclasses import dataclass
import uuid
from seedwork.dominio.eventos import (EventoDominio)

@dataclass
class PropiedadCreada(EventoDominio):
    id_propiedad: uuid.UUID = None    
    nombre_propiedad: str = None       
    tipo_propiedad: str = None    
    pais: str = None    
    departamento: str = None    
    ciudad: str = None    
    direccion: str = None       
    latitud : str = None    
    longitud: str = None    
    codigo_postal: str = None    
    area_lote: str = None    
    estrato_socioeconomico: str = None    
    valor_venta : str = None    
    valor_arriendo_mensual : str = None    
    moneda : str = None    
    propietario : str = None    
    arrendatario : str = None    
    fecha_ultimo_contrato : str = None    
    fecha_expiracion_contrato_actual : str = None    
    estado : str = None    
    id_compania : str = None    
    id_contrato : str = None      

@dataclass
class PropiedadEliminada(EventoDominio):
    id_propiedad: uuid.UUID = None
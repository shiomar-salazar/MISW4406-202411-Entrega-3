from __future__ import annotations
from dataclasses import dataclass
import uuid
from seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

@dataclass
class CompaniaCreada(EventoDominio):
    id_compania: uuid.UUID = None    
    nombre_compania: str = None
    representante_legal: str = None    
    email_contacto: str = None
    telefono_contacto: str = None
    estado: str = None
    documento_identidad_tipo: str = None
    documento_identidad_numero_identificacion: str = None
    tipo_industria: str = None
    direccion: str = None
    ciudad: str = None
    pais: str = None
    latitud: str = None
    longitud: str = None   
    fecha_creacion: datetime = None

from __future__ import annotations
from dataclasses import dataclass
from dataclasses import dataclass, field
import sqlalchemy
import uuid
import propiedadesalpes.modulos.companias.dominio.objetos_valor as ov
from propiedadesalpes.modulos.companias.dominio.eventos import CompaniaCreada
from propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad



@dataclass
class Compania(AgregacionRaiz):    
    id_compania: uuid.UUID = field(hash=True, default=uuid.uuid4())
    nombre_compania: str = field(default_factory=str)       
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=str)      
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad_tipo: str = field(default_factory=str)
    documento_identidad_numero_identificacion: str = field(default_factory=str)
    tipo_industria: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)
    def crear_compania(self, compania: Compania):    
            self.id_compania = compania.id_compania
            self.nombre_compania = compania.nombre_compania       
            self.representante_legal = compania.representante_legal
            self.email_contacto = compania.email_contacto      
            self.telefono_contacto = compania.telefono_contacto
            self.estado = compania.estado
            self.documento_identidad_tipo = compania.documento_identidad_tipo
            self.documento_identidad_numero_identificacion = compania.documento_identidad_numero_identificacion
            self.tipo_industria = compania.tipo_industria
            self.direccion = compania.direccion
            self.ciudad = compania.ciudad
            self.pais = compania.pais
            self.latitud = compania.latitud
            self.longitud = compania.longitud
            self.agregar_evento(CompaniaCreada(id=self.id, nombre_compania=self.nombre_compania, fecha_creacion=self.fecha_creacion))
        
 

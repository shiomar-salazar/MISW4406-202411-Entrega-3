from __future__ import annotations
from dataclasses import dataclass, field

import propiedadesalpes.modulos.compañias.dominio.objetos_valor as ov
from propiedadesalpes.modulos.compañias.dominio.eventos import CompaniaCreada
from propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad

@dataclass
class Compania(AgregacionRaiz):
    nombre_compania: str
    representante_legal: str
    email_contacto: str
    telefono_contacto: str
    estado: str
    documentoIdentidad: ov.DodumentoIdentidad
    tipoIndustria: list[ov.TipoIndustria] = field(default_factory=list)
    # informacion: ov.RepresentanteLegal
    # identificacion: ov.Identificacion
    
    
    def crear_compania(self, compania: Compania):
        self.nit = compania.identificacion.nit
        self.compania = compania.informacion.compania        
        self.nombre_representante_legal = compania.informacion.nombre
        self.apellido_representante_legal = compania.informacion.apellido       
        self.tipoIndustria = list[ov.TipoIndustria]
        self.localizacion = Localizacion
        
        self.agregar_evento(CompaniaCreada(nit=self.nit, compania=self.compania, fecha_creacion=self.fecha_creacion))


@dataclass
class Localizacion(AgregacionRaiz):
    direccion: ov.Direccion
    datos_geograficos: ov.DatosGeograficos
    informacion_geoespacial: ov.InformacionGeoespacial

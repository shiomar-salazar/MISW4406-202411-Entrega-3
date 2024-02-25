from __future__ import annotations
from dataclasses import dataclass, field

import propiedadesalpes.modulos.companias.dominio.objetos_valor as ov
from propiedadesalpes.modulos.companias.dominio.eventos import CompaniaCreada
from propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from propiedadesalpes.seedwork.dominio.objetos_valor import Compañia


@dataclass
class Compania(AgregacionRaiz, Compañia):    
    
    def crear_compania(self, compania: Compania):
        self.id = compania.id
        self.nombre_compañia = compania.nombre_compañia       
        self.representante_legal = compania.representante_legal
        self.email_contacto = compania.email_contacto      
        self.telefono_contacto = compania.telefono_contacto
        self.estado = compania.estado
        self.documento_identidad_tipo = compania.documento_identidad.tipo
        self.documento_identidad_numero_identificacion = compania.documento_identidad.numero_identificacion
        self.tipo_industria = compania.tipo_industria
        self.direccion = compania.localizacion.direccion.direccion
        self.ciudad = compania.localizacion.direccion.datos_geograficos.ciudad
        self.pais = compania.localizacion.direccion.datos_geograficos.pais
        self.latitud = compania.localizacion.infromacion_geoespacial.latitud
        self.longitud = compania.localizacion.infromacion_geoespacial.longitud

        self.agregar_evento(CompaniaCreada(id=self.id, nombre_compania=self.nombre_compañia, fecha_creacion=self.fecha_creacion))


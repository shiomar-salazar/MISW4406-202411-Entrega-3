from __future__ import annotations
from dataclasses import dataclass

import sqlalchemy

import propiedadesalpes.modulos.companias.dominio.objetos_valor as ov
from propiedadesalpes.modulos.companias.dominio.eventos import CompaniaCreada
from propiedadesalpes.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from propiedadesalpes.seedwork.dominio.objetos_valor import Compania_ov


@dataclass
class Compania(AgregacionRaiz, Compania_ov):    
    
    def crear_compania(self, compania: Compania):
        print('<================ Compania.crear_compania ================>')
        print(type(compania))
        print(compania)
        if isinstance(compania, sqlalchemy.engine.row.Row):
            self.id_compania = compania[0].id_compania
            self.nombre_compania = compania[0].nombre_compania       
            self.representante_legal = compania[0].representante_legal
            self.email_contacto = compania[0].email_contacto      
            self.telefono_contacto = compania[0].telefono_contacto
            self.estado = compania[0].estado
            self.documento_identidad_tipo = compania[1].tipo_documento
            self.documento_identidad_numero_identificacion = compania[1].numero_documento
            self.tipo_industria = compania[2].nombre
            self.direccion = None
            self.ciudad = None
            self.pais = None
            self.latitud = None
            self.longitud = None
        else:
            self.id_compania = compania.id_compania
            self.nombre_compania = compania.nombre_compania       
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
            self.agregar_evento(CompaniaCreada(id=self.id, nombre_compania=self.nombre_compania, fecha_creacion=self.fecha_creacion))
        
        print('<================ Compania.crear_compania ================>')
        return self


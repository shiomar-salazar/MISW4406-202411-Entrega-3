from __future__ import annotations
from dataclasses import dataclass
from dataclasses import dataclass, field
import sqlalchemy
import uuid
import modulos.contratos.dominio.objetos_valor as ov
from modulos.contratos.dominio.eventos import ContratoCreado
from seedwork.dominio.entidades import AgregacionRaiz, Entidad
import uuid


from .eventos import ContratoCreado

@dataclass
class Contrato(AgregacionRaiz):
    id_contrato: uuid.UUID = field(hash=True, default=uuid.uuid4())
    id_propiedad:uuid.UUID = field(hash=True, default=uuid.uuid4())     
    id_compania: uuid.UUID = field(hash=True, default=uuid.uuid4())
    fecha_inicio:str = field(default_factory=str)      
    fecha_fin:str = field(default_factory=str)
    fecha_ejecucion:str = field(default_factory=str)
    monto :str = field(default_factory=str)
    tipo :str = field(default_factory=str)
    

    def crear_contrato(self, contrato: "Contrato"):
        self.id_propiedad = contrato.id_propiedad
        self.id_compania = contrato.id_compania
        self.fecha_inicio = contrato.fecha_inicio
        self.fecha_fin = contrato.fecha_fin
        self.fecha_ejecucion = contrato.fecha_ejecucion
        self.monto = contrato.monto
        self.tipo = contrato.tipo


        self.agregar_evento(ContratoCreado(
            id_contrato = str(self.id_contrato), 
            id_propiedad = str(self.id_propiedad),
            id_compania = str(self.id_compania),
            fecha_inicio = str(self.fecha_inicio),
            fecha_fin = str(self.fecha_fin),
            fecha_ejecucion = str(self.fecha_ejecucion),
            monto = str(self.monto),
            tipo = str(self.tipo),
        )
    )


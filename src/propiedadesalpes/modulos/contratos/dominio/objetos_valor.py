"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Contrato(ObjetoValor):
    id :str
    id_propiedad :str       
    id_compania :str
    fecha_inicio :str      
    fecha_fin :str
    fecha_ejecucion :str
    monto :str
    tipo :str
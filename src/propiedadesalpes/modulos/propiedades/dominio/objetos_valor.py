"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Propiedad(ObjetoValor):
    id :str
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

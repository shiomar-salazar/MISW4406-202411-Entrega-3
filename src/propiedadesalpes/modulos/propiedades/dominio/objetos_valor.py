"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass

@dataclass(frozen=True)
class Compania(ObjetoValor):
    id :str
    nombre_compania :str       
    representante_legal :str
    email_contacto :str      
    telefono_contacto :str
    estado :str
    documento_identidad_tipo :str
    documento_identidad_numero_identificacion :str
    tipo_industria :str
    direccion :str
    ciudad :str
    pais :str
    latitud :str
    longitud :str

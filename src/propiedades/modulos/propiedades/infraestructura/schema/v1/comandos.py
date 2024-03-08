from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()

class ComandoCrearPropiedad(ComandoIntegracion):
    data = ComandoCrearPropiedadPayload()
    
class ComandoEliminarPropiedadPayload(ComandoIntegracion):
    id_propiedad = String()

class ComandoEliminarPropiedad(ComandoIntegracion):
    data = ComandoEliminarPropiedadPayload()    
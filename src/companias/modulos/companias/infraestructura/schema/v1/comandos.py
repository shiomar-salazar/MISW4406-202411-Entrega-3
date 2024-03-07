from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()
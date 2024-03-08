from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearCompaniaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearCompania(ComandoIntegracion):
    data = ComandoCrearCompaniaPayload()

class ComandoEliminarCompaniaPayload(ComandoIntegracion):
    id_compania = String()

class ComandoEliminarCompania(ComandoIntegracion):
    data = ComandoEliminarCompaniaPayload()
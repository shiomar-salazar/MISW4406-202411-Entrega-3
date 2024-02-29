from pulsar.schema import *
from dataclasses import dataclass, field
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearContratoPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearContrato(ComandoIntegracion):
    data = ComandoCrearContratoPayload()
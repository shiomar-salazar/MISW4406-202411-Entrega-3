from pulsar.schema import *
from seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoCrearContratoSagaPayload(ComandoIntegracion):
    id_usuario = String()

class ComandoCrearContratoSaga(ComandoIntegracion):
    data = ComandoCrearContratoSagaPayload()
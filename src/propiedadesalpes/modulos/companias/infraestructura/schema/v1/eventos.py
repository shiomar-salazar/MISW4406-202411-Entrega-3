from pulsar.schema import *
from propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class CompaniaCreadaPayload(Record):
    id_compania = String()
    estado = String()
    fecha_creacion = Long()

class EventoCompaniaCreada(EventoIntegracion):
    data = CompaniaCreadaPayload()
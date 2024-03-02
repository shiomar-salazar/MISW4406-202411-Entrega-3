from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from seedwork.infraestructura.utils import time_millis
import uuid

class ContratoCreadoPayload(Record):
    id = String()
    id_propiedad = String()
    id_compania = String()
    fecha_inicio = String()
    telefono_contacto = String()
    fecha_ejecucion = String()
    monto = String()
    tipo = String()



class EventoContratoCreado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    id_propiedad = String()
    id_compania = String()
    fecha_inicio = String(default=time_millis())
    telefono_contacto = String()
    fecha_ejecucion = String()
    monto = String()
    tipo = String()

    data = ContratoCreadoPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class ContratoCreadoPayload(Record):
    id = String()
    id_propiedad = String()
    id_compania = String()
    fecha_inicio = String()
    telefono_contacto = String()
    fecha_ejecucion = String()
    monto = Int()
    tipo = String()



class EventoContratoCreado(EventoIntegracion):
    data = ContratoCreadoPayload()
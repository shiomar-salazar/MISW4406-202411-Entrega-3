from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id = String()
    nombre_propiedad = String()
    representante_legal = String()
    email_contacto = String()
    telefono_contacto = String()
    estado = String()
    documento_identidad_numero_identificacion = String()
    documento_identidad_tipo = String()
    tipo_industria = String()
    direccion = String()
    latitud = String()
    longitud = String()
    ciudad = String()
    pais = String()


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()
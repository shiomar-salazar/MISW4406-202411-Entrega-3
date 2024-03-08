import pulsar
from pulsar.schema import *
from modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada, CompaniaCreadaPayload, CompaniaEliminadaPayload, EventoCompaniaEliminada 
from modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearCompania, ComandoCrearCompaniaPayload, ComandoEliminarCompaniaPayload, ComandoEliminarCompania
from seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # publicador = cliente.create_producer(topico, schema=AvroSchema(EventoCompaniaCreada))
        publicador = cliente.create_producer(topico, schema=schema)        
        publicador.send(mensaje)
        print(f'INFO: Se envia mensaje [{mensaje}], topico [{topico}], schema [{schema}]')
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = CompaniaCreadaPayload(
            id_compania = str(evento.id_compania),
            nombre_compania = evento.nombre_compania,
            representante_legal = evento.representante_legal,
            email_contacto = evento.email_contacto,
            telefono_contacto = evento.telefono_contacto,
            estado = evento.estado,
            documento_identidad_numero_identificacion = evento.documento_identidad_numero_identificacion,
            documento_identidad_tipo = evento.documento_identidad_tipo,
            tipo_industria = evento.tipo_industria,
            direccion = evento.direccion,
            latitud = evento.tipo_industria,
            longitud = evento.tipo_industria,
            ciudad = evento.ciudad,
            pais = evento.pais
        )
        evento_integracion = EventoCompaniaCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoCompaniaCreada))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearCompaniaPayload(
            id_compania=str(comando.id_compania)
        )
        comando_integracion = ComandoCrearCompania(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearCompania))

    def publicar_evento_eliminada(self, evento, topico):
        payload = CompaniaEliminadaPayload(
            id = str(evento.id_compania),
        )
        evento_integracion = EventoCompaniaEliminada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoCompaniaEliminada))

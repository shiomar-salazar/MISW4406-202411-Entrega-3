import pulsar
from pulsar.schema import *
import pika

from modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada, CompaniaCreadaPayload
from modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearCompania, ComandoCrearCompaniaPayload
from seedwork.infraestructura import utils

import datetime
import json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoCompaniaCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = CompaniaCreadaPayload(
            id = str(evento.id),
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
        print('<=============== Despachador.publicar_evento [payload] ==================>')
        print(payload)

        evento_integracion = EventoCompaniaCreada(data=payload)
        print('<=============== Despachador.publicar_evento [evento_integracion] ==================>')
        print(evento_integracion)

        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoCompaniaCreada))
        
        # En el tutorial 9 esta asi el metodo publicar_evento
        # def publicar_evento(self, evento, topico):
        #     evento = self.mapper.entidad_a_dto(evento)
        #     self._publicar_mensaje(evento, topico, AvroSchema(evento.__class__))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearCompaniaPayload(
            id_compania=str(comando.id_compania)
        )
        comando_integracion = ComandoCrearCompania(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearCompania))
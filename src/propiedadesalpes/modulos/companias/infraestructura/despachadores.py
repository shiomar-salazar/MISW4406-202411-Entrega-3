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
            id = evento.id,
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



    def _publicar_mensaje_rabbit(self, mensaje, topico):
        credentials = pika.PlainCredentials(username=f'{utils.broker_rabbit_user()}', password=f'{utils.broker_rabbit_password()}')
        connection = pika.BlockingConnection(pika.ConnectionParameters(f'{utils.broker_rabbit_host()}', port=utils.broker_rabbit_port(), credentials= credentials))
        channel = connection.channel()
        channel.exchange_declare(exchange=topico, exchange_type='topic', durable=True)
        message = mensaje
        
        channel.basic_publish(exchange=topico, routing_key=f'{utils.broker_rabbit_password()}', body=message)
        connection.close()

    def publicar_evento_rabbit(self, evento, topico):
        payload = {
            "id" : f'{evento.id}',
            "nombre_compania" : f"{evento.nombre_compania}",
            "representante_legal" : f"{evento.representante_legal}",
            "email_contacto" : f"{evento.email_contacto}",
            "telefono_contacto" : f"{evento.telefono_contacto}",
            "estado" : f"{evento.estado}",
            "documento_identidad_numero_identificacion" : f"{evento.documento_identidad_numero_identificacion}",
            "documento_identidad_tipo" : f"{evento.documento_identidad_tipo}",
            "tipo_industria" : f"{evento.tipo_industria}",
            "direccion" : f"{evento.direccion}",
            "latitud" : f"{evento.latitud}",
            "longitud" : f"{evento.longitud}",
            "ciudad" : f"{evento.ciudad}",
            "pais" : f"{evento.pais}"
        }
        
        mensaje = json.dumps(payload)
        self._publicar_mensaje_rabbit(mensaje, topico)

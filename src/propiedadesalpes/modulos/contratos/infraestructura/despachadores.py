import pulsar
from pulsar.schema import *
import pika

from modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload
from modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContrato, ComandoCrearContratoPayload
from seedwork.infraestructura import utils

import datetime
import json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoContratoCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = ContratoCreadoPayload(
            id = evento.id,
            id_propiedad = evento.id_propiedad,
            id_compania = evento.id_compania,
            fecha_inicio = evento.fecha_inicio,
            fecha_fin = evento.fecha_fin,
            fecha_ejecucion = evento.fecha_ejecucion,
            monto = evento.monto,
            tipo = evento.tipo,
        )
        
        evento_integracion = EventoContratoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoContratoCreado))

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearContratoPayload(
            id_contrato=str(comando.id_contrato)
        )
        comando_integracion = ComandoCrearContrato(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearContrato))



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
            "id_propiedad" : f"{evento.id_propiedad}",
            "id_compania" : f"{evento.id_compania}",
            "fecha_inicio" : f"{evento.fecha_inicio}",
            "fecha_fin" : f"{evento.fecha_fin}",
            "fecha_ejecucion" : f"{evento.fecha_ejecucion}",
            "monto" : f"{evento.monto}",
        }
        
        mensaje = json.dumps(payload)
        self._publicar_mensaje_rabbit(mensaje, topico)

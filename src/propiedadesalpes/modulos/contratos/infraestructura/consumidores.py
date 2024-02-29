import json
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from modulos.contratos.aplicacion.comandos.crear_cache_contrato import CrearCacheContrato

from modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado
from modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContrato
from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contrato', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoContratoCreado))

        while True:
            mensaje = consumidor.receive()
            ex = mensaje.value()
            contrato_dto = ex.data
            comando = CrearCacheContrato(
                id = contrato_dto.id,
                id_propiedad = contrato_dto.id_propiedad,
                id_compania = contrato_dto.id_compania,
                fecha_inicio = contrato_dto.fecha_inicio,
                fecha_fin = contrato_dto.fecha_fin,
                fecha_ejecucion = contrato_dto.fecha_ejecucion,
                monto = contrato_dto.monto,
                tipo = contrato_dto.tipo,
            )
            ejecutar_commando(comando)
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearContrato))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.data()}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

import pika
def suscribirse_a_eventos_rabbit():
    def callback(ch, method, properties, body):
            contrato_dto = json.loads(body)
            comando = CrearCacheContrato(
                id = contrato_dto['id'],
                id_propiedad = contrato_dto['id_propiedad'],
                id_compania = contrato_dto['id_compania'],
                fecha_inicio = contrato_dto['fecha_inicio'],
                fecha_fin = contrato_dto['fecha_fin'],
                fecha_ejecucion = contrato_dto['fecha_ejecucion'],
                monto = contrato_dto['monto'],
                tipo = contrato_dto['tipo'],                
                )
            ejecutar_commando(comando)

    topico = 'eventos-contrato'
    credentials = pika.PlainCredentials(username=f'{utils.broker_rabbit_user()}', password=f'{utils.broker_rabbit_password()}')
    connection = pika.BlockingConnection(pika.ConnectionParameters(f'{utils.broker_rabbit_host()}', port=utils.broker_rabbit_port(), credentials= credentials))
    channel = connection.channel()
    channel.exchange_declare(exchange=topico, exchange_type='topic', durable=True)
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=topico, queue=queue_name, routing_key=f'{utils.broker_rabbit_password()}')
    print(f" [*] Esperando mensajes en el topico {topico}. Para salir, presiona Ctrl+C")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
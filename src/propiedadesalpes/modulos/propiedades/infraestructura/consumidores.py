import json
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from modulos.propiedades.aplicacion.comandos.crear_cache_compania import CrearCacheCompania

from modulos.propiedades.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearCompania
from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoCompaniaCreada))

        while True:
            mensaje = consumidor.receive()
            ex = mensaje.value()
            compania_dto = ex.data
            comando = CrearCacheCompania(
                id = compania_dto.id,
                nombre_compania = compania_dto.nombre_compania,
                representante_legal = compania_dto.representante_legal,
                email_contacto = compania_dto.email_contacto,
                telefono_contacto = compania_dto.telefono_contacto,
                estado = compania_dto.estado,
                documento_identidad_numero_identificacion = compania_dto.documento_identidad_numero_identificacion,
                documento_identidad_tipo = compania_dto.documento_identidad_tipo,
                tipo_industria = compania_dto.tipo_industria,
                direccion = compania_dto.direccion,
                latitud = compania_dto.tipo_industria,
                longitud = compania_dto.tipo_industria,
                ciudad = compania_dto.ciudad,
                pais = compania_dto.pais
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
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearCompania))

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
            compania_dto = json.loads(body)
            comando = CrearCacheCompania(
                id = compania_dto['id'],
                nombre_compania = compania_dto['nombre_compania'],
                representante_legal = compania_dto['representante_legal'],
                email_contacto = compania_dto['email_contacto'],
                telefono_contacto = compania_dto['telefono_contacto'],
                estado = compania_dto['estado'],
                documento_identidad_numero_identificacion = compania_dto['documento_identidad_numero_identificacion'],
                documento_identidad_tipo = compania_dto['documento_identidad_tipo'],
                tipo_industria = compania_dto['tipo_industria'],
                direccion = compania_dto['direccion'],
                latitud = compania_dto['latitud'],
                longitud = compania_dto['longitud'],
                ciudad = compania_dto['ciudad'],
                pais = compania_dto['pais']
                
                )
            ejecutar_commando(comando)

    topico = 'eventos-compania'
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
import json
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
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
            print(f'Evento recibido: {ex}')
            # TODO Lógica a realizar cuando se recibe el evento

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
            
            # TODO Lógica a realizar cuando se recibe el comando

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

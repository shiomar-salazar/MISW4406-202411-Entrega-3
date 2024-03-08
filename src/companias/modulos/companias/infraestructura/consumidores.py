import pulsar,_pulsar  
from pulsar.schema import *
import traceback
from modulos.companias.aplicacion.comandos.crear_compania import CrearCompania
from modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada, EventoCompaniaEliminada
from modulos.companias.infraestructura.schema.v1.comandos import ComandoCrearCompania, ComandoEliminarCompania
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoCompaniaCreada))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (EventoCompaniaCreada) => [{datos_mensaje.data}]')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearCompania))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ComandoCrearCompania) => [{datos_mensaje.data}]')            
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_eliminada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania-eliminada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoCompaniaEliminada))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (EventoCompaniaEliminada) => [{datos_mensaje.data}]')
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_eliminada(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compania-eliminada', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoEliminarCompania))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ComandoEliminarCompania) => [{datos_mensaje.data}]')
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

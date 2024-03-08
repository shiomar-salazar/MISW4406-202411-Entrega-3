import pulsar,_pulsar  
import traceback
from pulsar.schema import *
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from modulos.propiedades.aplicacion.comandos.eliminar_propiedad import EliminarPropiedad
from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, EventoPropiedadEliminada
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoEliminarPropiedad
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (PropiedadCreada) => [{datos_mensaje.data}]')
            # TODO Lógica a realizar cuando se recibe el evento de propiedad creada
            consumidor.acknowledge(mensaje)     
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_eliminada():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad-eliminada', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoPropiedadEliminada))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (PropiedadEliminada) => [{datos_mensaje.data}]')
            # TODO Lógica a realizar cuando se recibe el evento de propiedad eliminada
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
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearPropiedad))
        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ComandoCrearPropiedad) => [{datos_mensaje.data}]')
            # TODO Lógica a realizar cuando se recibe el comando
            consumidor.acknowledge(mensaje)     
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_eliminar(app=None):
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-propiedad-eliminada', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoEliminarPropiedad))
        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ComandoEliminarPropiedad) => [{datos_mensaje.data}]')
            # TODO Lógica a realizar cuando se recibe el comando
            consumidor.acknowledge(mensaje)     
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
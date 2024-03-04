import json
import pulsar,_pulsar  
from pulsar.schema import *
import logging
import traceback
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad

from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad
from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoPropiedadCreada))

        while True:
            mensaje = consumidor.receive()
            datos = mensaje.value()
            print(f'Evento recibido: {datos}')
            
            # En el tutorial 9 va el tema de proyecciones
            
            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
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
            print(f'Comando recibido: {mensaje.data()}')

            # try:
            #     with app.app_context():
            #         comando = CrearPropiedad(fecha_creacion, fecha_creacion, id_reserva, itinerarios)
            #         ejecutar_commando(comando)
            # except:
            #     logging.error('ERROR: Procesando eventos!')
            #     traceback.print_exc()
            
            
            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

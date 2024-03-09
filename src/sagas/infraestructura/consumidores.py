import json
import pulsar,_pulsar  
from pulsar.schema import *
import traceback
from infraestructura.schema.v1.eventos import EventoSagaContratoCreado
from infraestructura.schema.v1.comandos import ComandoCrearContratoSaga
from seedwork.infraestructura import utils
from aplicacion.orquestadores.sagas_contrato import CoordiandorContratos,

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-contrato', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedadesalpes-sub-eventos', schema=AvroSchema(EventoSagaContratoCreado))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (EventoSagaContratoCreado) => [{datos_mensaje.data}]')
            
            coordinador = CoordiandorContratos()
            coordinador.persistir_en_saga_log(datos_mensaje.data)

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedadesalpes-sub-comandos', schema=AvroSchema(ComandoCrearContratoSaga))

        while True:
            mensaje = consumidor.receive()
            datos_mensaje = mensaje.value()
            print(F'INFO: Se recibe evento (ComandoCrearContratoSaga) => [{datos_mensaje.data}]')
            
            coordinador = CoordiandorContratos()
            coordinador.persistir_en_saga_log(datos_mensaje.data)

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        print('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

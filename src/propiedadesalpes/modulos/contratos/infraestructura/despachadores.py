import pulsar
from pulsar.schema import *
from modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload
from modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContrato, ComandoCrearContratoPayload
from seedwork.infraestructura import utils
import datetime

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
            id = str(evento.id),
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


import pulsar
from pulsar.schema import *
from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload, EventoPropiedadEliminada, PropiedadEliminadaPayload
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from seedwork.infraestructura import utils
import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        # publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        print(f'INFO: Se envia mensaje [{mensaje}], topico [{topico}], schema [{schema}]')
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            id_propiedad = str(evento.id_propiedad),
            nombre_propiedad = evento.nombre_propiedad,
            tipo_propiedad = evento.tipo_propiedad,
            pais = evento.pais,
            departamento = evento.departamento,
            ciudad = evento.ciudad,
            direccion = evento.direccion,
            latitud = evento.latitud,
            longitud = evento.longitud,
            codigo_postal = evento.codigo_postal,
            area_lote = evento.area_lote,
            estrato_socioeconomico = evento.estrato_socioeconomico,
            valor_venta = evento.valor_venta,
            valor_arriendo_mensual = evento.valor_arriendo_mensual,
            moneda = evento.moneda,
            propietario = evento.propietario,
            arrendatario = evento.arrendatario,
            fecha_ultimo_contrato = evento.fecha_ultimo_contrato,
            fecha_expiracion_contrato_actual = evento.fecha_expiracion_contrato_actual,
            estado = evento.estado,
            id_compania = evento.id_compania,
            id_contrato = evento.id_contrato
        )
        evento_integracion = EventoPropiedadCreada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadCreada))
        
    def publicar_evento_eliminada(self, evento, topico):
        payload = PropiedadEliminadaPayload(
            id_propiedad = str(evento.id_propiedad)
        )
        evento_integracion = EventoPropiedadEliminada(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPropiedadEliminada))   
        
    def publicar_comando(self, comando, topico):
        payload = ComandoCrearPropiedadPayload(
            id_propiedad=str(comando.id_propiedad)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))

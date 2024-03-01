import pulsar
from pulsar.schema import *
import pika

from modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreada, PropiedadCreadaPayload
from modulos.propiedades.infraestructura.schema.v1.comandos import ComandoCrearPropiedad, ComandoCrearPropiedadPayload
from seedwork.infraestructura import utils

import datetime
import json

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoPropiedadCreada))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        payload = PropiedadCreadaPayload(
            id = evento.id,
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

    def publicar_comando(self, comando, topico):
        payload = ComandoCrearPropiedadPayload(
            id_propiedad=str(comando.id_propiedad)
        )
        comando_integracion = ComandoCrearPropiedad(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearPropiedad))



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
            "id" : f"{evento.id}",
            "nombre_propiedad" : f"{evento.nombre_propiedad}",
            "tipo_propiedad" : f"{evento.tipo_propiedad}",
            "pais" : f"{evento.pais}",
            "departamento" : f"{evento.departamento}",
            "ciudad" : f"{evento.ciudad}",
            "direccion" : f"{evento.direccion}",
            "latitud" : f"{evento.latitud}",
            "longitud" : f"{evento.longitud}",
            "codigo_postal" : f"{evento.codigo_postal}",
            "area_lote" : f"{evento.area_lote}",
            "estrato_socioeconomico" : f"{evento.estrato_socioeconomico}",
            "valor_venta" : f"{evento.valor_venta}",
            "valor_arriendo_mensual" : f"{evento.valor_arriendo_mensual}",
            "moneda" : f"{evento.moneda}",
            "propietario" : f"{evento.propietario}",
            "arrendatario" : f"{evento.arrendatario}",
            "echa_ultimo_contrato" : f"{evento.fecha_ultimo_contrato}",
            "echa_expiracion_contrato_actual" : f"{evento.fecha_expiracion_contrato_actual}",
            "estado" : f"{evento.estado}",
            "id_compania" : f"{evento.id_compania}",
            "id_contrato" : f"{evento.id_contrato}"
        }
        
        mensaje = json.dumps(payload)
        self._publicar_mensaje_rabbit(mensaje, topico)

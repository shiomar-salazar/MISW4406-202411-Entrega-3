from flask import request, Blueprint
from flask import Response
from api.utils import crear_compania, crear_contrato, crear_propiedad, obtener_compania, obtener_contrato, obtener_propiedad
import json

class CrearSagas:
    def __init__(self, post_request):
        self.post_request = post_request
        
    def execute(self):
        try:
            crear_compania()
            direccion = self.post_request['direccion']
            id_compania = obtener_compania(direccion)
            crear_propiedad()
            id_propiedad = obtener_propiedad(direccion)            
            crear_contrato(id_compania, id_propiedad)
            contrato = obtener_contrato(id_compania, id_propiedad)            
            return contrato

        except Exception as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
                        

















    def autenticar_usuario(self, propiedad_json, token):
        is_token = revisar_token(token)
        if is_token == False:
            raise Exception("No se pudo autenticar el usuario")

    def procesar_propiedad(self, propiedad_json, token):
        bytes_io = io.BytesIO()
        writer = DatumWriter(self.propiedad_schema)
        encoder = BinaryEncoder(bytes_io)
        writer.write(propiedad_json, encoder)
        encoded_data = bytes_io.getvalue()  
        client = Client('pulsar://10.182.0.2:6650')
        producer_comandos_propiedad = client.create_producer('persistent://public/default/comandos-propiedades', chunking_enabled=True) 
        producer_comandos_propiedad.send(encoded_data)
        consumer = client.subscribe('persistent://public/default/eventos-propiedades', 'eventos-subscription-bff')
        start_time = time.time()
        timeout = 1
        while time.time() - start_time < timeout:
            msg = consumer.receive()
            if msg:
                consumer.acknowledge(msg)
                client.close()
                return  
        client.close()
        raise Exception("No se recibió respuesta de Pulsar dentro del tiempo especificado")
    


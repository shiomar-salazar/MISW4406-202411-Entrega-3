from flask import request, Blueprint
from flask import Response
from api.utils import crear_compania, crear_contrato, crear_propiedad, obtener_compania, obtener_contrato, obtener_propiedad, eliminar_compania, eliminar_propiedad
import json
from aplicacion.mapeadores import MapeadorContratoDTOJson
class CrearSagas:
    def __init__(self, post_request):
        self.post_request = post_request
    def execute(self):        
        mapeador = MapeadorContratoDTOJson()
        saga_contrato = mapeador.externo_a_dto(self.post_request)        
        crear_compania(saga_contrato)        
        id_compania = obtener_compania(saga_contrato.direccion)
        if not id_compania:
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')
        crear_propiedad(saga_contrato)
        id_propiedad = obtener_propiedad(saga_contrato.direccion)
        if not id_propiedad:
            eliminar_compania(id_compania)
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')
        crear_contrato(saga_contrato, id_compania, id_propiedad)
        contrato = obtener_contrato(id_compania, id_propiedad)
        if not contrato:
            eliminar_compania(id_compania)
            eliminar_propiedad(id_propiedad)
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')
        else:
            return contrato
        





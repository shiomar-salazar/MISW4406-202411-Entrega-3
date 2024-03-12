from flask import request, Blueprint
from flask import Response
from api.utils import crear_compania, crear_contrato, crear_propiedad, obtener_compania, obtener_contrato, obtener_propiedad
import json
from aplicacion.mapeadores import MapeadorContratoDTOJson
class CrearSagas:
    def __init__(self, post_request):
        self.post_request = post_request
    def execute(self):
        try:
            mapeador = MapeadorContratoDTOJson()
            saga_contrato = mapeador.externo_a_dto(self.post_request)
            crear_compania(saga_contrato)
            id_compania = obtener_compania(saga_contrato.direccion)
            crear_propiedad(saga_contrato)
            id_propiedad = obtener_propiedad(saga_contrato.direccion)
            crear_contrato(saga_contrato, id_compania, id_propiedad)
            contrato = obtener_contrato(id_compania, id_propiedad)
            return contrato
        except Exception as e:
            return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')





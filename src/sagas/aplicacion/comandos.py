from flask import request, Blueprint
from flask import Response
from api.utils import crear_compania, crear_contrato, crear_propiedad, obtener_compania, obtener_contrato, obtener_propiedad, eliminar_compania, eliminar_propiedad
import json
from aplicacion.mapeadores import MapeadorContratoDTOJson
from infraestructura.repositorios import RepositorioSagaLogPostgresSQL
import uuid


class CrearSagas:
    def __init__(self, post_request):
        self.post_request = post_request
        self.saga_log = RepositorioSagaLogPostgresSQL()


    def execute(self):        
        mapeador = MapeadorContratoDTOJson()
        saga_contrato = mapeador.externo_a_dto(self.post_request)        
        self.saga_log.agregar('paso 1 - crear compania')
        crear_compania(saga_contrato)                        
        id_compania = obtener_compania(saga_contrato.direccion)        
        if not id_compania:
            self.saga_log.agregar('paso 2 - compania fallida')
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')        
        self.saga_log.agregar('paso 2 - compania creada')
        self.saga_log.agregar('paso 3 - crear propiedad')
        crear_propiedad(saga_contrato)
        id_propiedad = obtener_propiedad(saga_contrato.direccion)
        if not id_propiedad:
            eliminar_compania(id_compania)
            self.saga_log.agregar('paso 4 - propiedad fallida')
            self.saga_log.agregar('paso 4 - compania roll back')
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')
        self.saga_log.agregar('paso 4 - propiedad creada')
        self.saga_log.agregar('paso 5 - crear contrato')
        crear_contrato(saga_contrato, id_compania, id_propiedad)
        contrato = obtener_contrato(id_compania, id_propiedad)
        if not contrato:
            eliminar_compania(id_compania)
            eliminar_propiedad(id_propiedad)
            self.saga_log.agregar('paso 6 - contrato fallido')
            self.saga_log.agregar('paso 6 - compania roll back')
            self.saga_log.agregar('paso 6 - propiedad roll back')
            return Response(json.dumps({'msg':'No se pudo realizar la crecion del contrato'}), status=409, mimetype='application/json')
        else:
            self.saga_log.agregar('paso 6 - contrato creado')
            return contrato
        





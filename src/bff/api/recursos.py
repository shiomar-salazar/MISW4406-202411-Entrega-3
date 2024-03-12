from asyncio import exceptions
import seedwork.presentacion.api as api
from flask import Response
from flask import request
import json
from modulos.aplicacion.command.consulta_propiedad_direccion import ConsultarDatos
from modulos.aplicacion.command.crear_contrato_saga import CrearContratoSaga


bp = api.crear_blueprint('bff-propiedad', '/bff-propiedad')

@bp.route('/direccion', methods=['GET'])
def dar_propiedad_por_direccion_usando_query():
    print('Inicial consulta propiedad')
    direccion = request.args.get('direccion') 
    direccion.replace(" ","&nbsp;")    
    print('direccion' + direccion)
    try:
        return ConsultarDatos(direccion).execute()      
    except exceptions as e:
       return Response(json.dumps(dict(error=str(e))), status=404, mimetype='application/json')
    

@bp.route('', methods=['POST'])
def crear_contrato_saga():
    print('Inicial crear propiedad saga')
    propiedad_request = request.json
    
    print('propiedad_request' )
    print(propiedad_request)
    try:
        return CrearContratoSaga(propiedad_request).execute()      
    except exceptions as e:
       return Response(json.dumps(dict(error=str(e))), status=404, mimetype='application/json')
    


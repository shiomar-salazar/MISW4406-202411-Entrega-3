from asyncio import exceptions
import seedwork.presentacion.api as api
from flask import Response
from flask import request
import json
from modulos.aplicacion.command.consulta_propiedad_direccion import ConsultarDatos


bp = api.crear_blueprint('propiedad', '/propiedad')

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
    


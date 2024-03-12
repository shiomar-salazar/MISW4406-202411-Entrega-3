import json
from flask import Response
from flask import request
import seedwork.presentacion.api as api
from aplicacion.comandos import CrearSagas

bp = api.crear_blueprint('saga-contratos', '/saga-contratos')


@bp.route('/crear-contrato', methods=['POST'])
def crear():
    try:
        contrato_dict = request.get_json()
        return CrearSagas(contrato_dict).execute()
    except Exception as e:
        print(e)



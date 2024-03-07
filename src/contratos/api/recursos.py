import seedwork.presentacion.api as api
from seedwork.dominio.excepciones import ExcepcionDominio
from modulos.contratos.aplicacion.mapeadores import MapeadorContratoDTOJson
from modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from modulos.contratos.aplicacion.queries.obtener_todos_contratos import ObtenerTodasContratos
from seedwork.aplicacion.queries import ejecutar_query
from seedwork.aplicacion.comandos import ejecutar_commando
import json
from flask import Response
from flask import request


bp = api.crear_blueprint('contrato', '/contrato')

@bp.route('/crear', methods=['POST',])
def crear():
    try:
        contrato_dict = request.json
        map_contrato = MapeadorContratoDTOJson()
        contrato_dto = map_contrato.externo_a_dto(contrato_dict)

        comando = CrearContrato(
            id_propiedad = contrato_dto.id_propiedad,
            id_compania = contrato_dto.id_compania,
            fecha_inicio = contrato_dto.fecha_inicio,
            fecha_fin = contrato_dto.fecha_fin,
            fecha_ejecucion = contrato_dto.fecha_ejecucion,
            monto = contrato_dto.monto,
            tipo = contrato_dto.tipo,
        )

        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=('GET',))
def dar_contrato_usando_query():
    map_contrato = MapeadorContratoDTOJson()
    query_resultado = ejecutar_query(ObtenerTodasContratos())
    resultados = []
    
    for contrato in query_resultado.resultado:
        resultados.append(map_contrato.dto_a_externo(contrato))
    
    return resultados
    
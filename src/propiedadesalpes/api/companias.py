import propiedadesalpes.seedwork.presentacion.api as api
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from propiedadesalpes.modulos.companias.aplicacion.queries.obtener_companias import ObtenerCompanias
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio
from propiedadesalpes.modulos.companias.aplicacion.comandos.registrar_compania import RegistrarCompania
import json
from flask import redirect, render_template, request, session, url_for
from flask import Response


bp = api.crear_blueprint('companias', '/companias')

@bp.route('/compania-query', methods=('GET',))
def dar_compania_usando_query():
    query_resultado = ejecutar_query(ObtenerCompanias())
    map_compania = MapeadorCompaniaDTOJson()
    return map_compania.dto_a_externo(query_resultado.resultado)


@bp.route('/compania-comando', methods=('POST',))
def reservar_asincrona():
    try:
        compania_dict = request.json

        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)

        comando = RegistrarCompania(compania_dto.id, compania_dto.nombre_compania, compania_dto.representante_legal,
                                    compania_dto.email_contacto, compania_dto.telefono_contacto, compania_dto.estado,
                                    compania_dto.documento_identidad, compania_dto.tipo_industria, compania_dto.localizacion)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
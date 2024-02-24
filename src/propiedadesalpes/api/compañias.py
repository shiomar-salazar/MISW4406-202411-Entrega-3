import propiedadesalpes.seedwork.presentacion.api as api
import json
from propiedadesalpes.modulos.compañias.aplicacion.servicios import ServicioCompania
from propiedadesalpes.modulos.compañias.aplicacion.dto import CompaniaDTO
from propiedadesalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from propiedadesalpes.modulos.compañias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from propiedadesalpes.modulos.compañias.aplicacion.queries.obtener_companias import ObtenerCompanias
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('companias', '/companias')

@bp.route('/compania-query', methods=('GET',))
def dar_compania_usando_query():
    query_resultado = ejecutar_query(ObtenerCompanias())
    map_compania = MapeadorCompaniaDTOJson()
    return map_compania.dto_a_externo(query_resultado.resultado)
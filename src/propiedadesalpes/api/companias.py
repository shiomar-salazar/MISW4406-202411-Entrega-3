import propiedadesalpes.seedwork.presentacion.api as api
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from propiedadesalpes.modulos.companias.aplicacion.queries.obtener_companias import ObtenerCompanias
from propiedadesalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('companias', '/companias')

@bp.route('/compania-query', methods=('GET',))
def dar_compania_usando_query():
    query_resultado = ejecutar_query(ObtenerCompanias())
    map_compania = MapeadorCompaniaDTOJson()
    return map_compania.dto_a_externo(query_resultado.resultado)
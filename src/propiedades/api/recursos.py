import seedwork.presentacion.api as api
from seedwork.dominio.excepciones import ExcepcionDominio
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from modulos.propiedades.aplicacion.comandos.eliminar_propiedad import EliminarPropiedad
from modulos.propiedades.aplicacion.queries.obtener_todas_propiedades import ObtenerTodasPropiedades
from modulos.propiedades.aplicacion.queries.obtener_propiedad_direccion import ObtenerPropiedadDireccion
from modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from seedwork.aplicacion.queries import ejecutar_query
from seedwork.aplicacion.comandos import ejecutar_commando
import json
from flask import Response
from flask import request


bp = api.crear_blueprint('propiedad', '/propiedad')

@bp.route('/crear', methods=['POST'])
def crear():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

        comando = CrearPropiedad(
            id_propiedad = propiedad_dto.id_propiedad,
            nombre_propiedad = propiedad_dto.nombre_propiedad,
            tipo_propiedad = propiedad_dto.tipo_propiedad,
            pais = propiedad_dto.pais,
            departamento = propiedad_dto.departamento,
            ciudad = propiedad_dto.ciudad,
            direccion = propiedad_dto.direccion,
            latitud = propiedad_dto.latitud,
            longitud = propiedad_dto.longitud,
            codigo_postal = propiedad_dto.codigo_postal,
            area_lote = propiedad_dto.area_lote,
            estrato_socioeconomico = propiedad_dto.estrato_socioeconomico,
            valor_venta = propiedad_dto.valor_venta,
            valor_arriendo_mensual = propiedad_dto.valor_arriendo_mensual,
            moneda = propiedad_dto.moneda,
            propietario = propiedad_dto.propietario,
            arrendatario = propiedad_dto.arrendatario,
            fecha_ultimo_contrato = propiedad_dto.fecha_ultimo_contrato,
            fecha_expiracion_contrato_actual = propiedad_dto.fecha_expiracion_contrato_actual,
            estado = propiedad_dto.estado,
            id_compania = propiedad_dto.id_compania,
            id_contrato = propiedad_dto.id_contrato
        )

        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/eliminar/<id_propiedad>', methods=['DELETE'])
def eliminar(id_propiedad):
    try:
        comando = EliminarPropiedad(
            id_propiedad = id_propiedad
        )
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
       return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('', methods=['GET'])
def dar_propiedad_usando_query():
    map_propiedad = MapeadorPropiedadDTOJson()
    query_resultado = ejecutar_query(ObtenerTodasPropiedades())
    resultados = []
    for propiedad in query_resultado.resultado:
        resultados.append(map_propiedad.dto_a_externo(propiedad))
    return resultados


@bp.route('<id_propiedad>', methods=['GET'])
def dar_propiedad_por_id_usando_query(id_propiedad):
    print('Inicial consulta propiedad')
    id_propiedad = id_propiedad
    print('propiedad' + id_propiedad)
    try:
        map_propiedad = MapeadorPropiedadDTOJson()
        query_resultado = ejecutar_query(ObtenerPropiedad(id_propiedad))
        return map_propiedad.dto_sigle_a_externo(query_resultado.resultado)      
    except ExcepcionDominio as e:
       return Response(json.dumps(dict(error=str(e))), status=404, mimetype='application/json')


@bp.route('/direccion', methods=['GET'])
def dar_propiedad_por_direccion_usando_query():
    print('Inicial consulta propiedad')
    direccion = request.args.get('direccion')     
    print('direccion' + direccion)
    try:
        map_propiedad = MapeadorPropiedadDTOJson()
        query_resultado = ejecutar_query(ObtenerPropiedadDireccion(direccion))
        return map_propiedad.dto_sigle_a_externo(query_resultado.resultado)      
    except ExcepcionDominio as e:
       return Response(json.dumps(dict(error=str(e))), status=404, mimetype='application/json')
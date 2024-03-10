from asyncio import exceptions
import seedwork.presentacion.api as api
# from seedwork.dominio.excepciones import ExcepcionDominio
# from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
# from modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
# from modulos.propiedades.aplicacion.comandos.eliminar_propiedad import EliminarPropiedad
# from modulos.propiedades.aplicacion.queries.obtener_todas_propiedades import ObtenerTodasPropiedades
# from modulos.propiedades.aplicacion.queries.obtener_propiedad_direccion import ObtenerPropiedadDireccion
# from modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
# from seedwork.aplicacion.queries import ejecutar_query
# from seedwork.aplicacion.comandos import ejecutar_commando
# import json
from flask import Response
from flask import request
import json
from modulos.aplicacion.command.consulta_propiedad_direccion import ConsultarDatos


bp = api.crear_blueprint('propiedad', '/propiedad')

# @bp.route('/crear', methods=['POST'])
# def crear():
#     try:
#         propiedad_dict = request.json
#         map_propiedad = MapeadorPropiedadDTOJson()
#         propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)

#         comando = CrearPropiedad(
#             id_propiedad = propiedad_dto.id_propiedad,
#             nombre_propiedad = propiedad_dto.nombre_propiedad,
#             tipo_propiedad = propiedad_dto.tipo_propiedad,
#             pais = propiedad_dto.pais,
#             departamento = propiedad_dto.departamento,
#             ciudad = propiedad_dto.ciudad,
#             direccion = propiedad_dto.direccion,
#             latitud = propiedad_dto.latitud,
#             longitud = propiedad_dto.longitud,
#             codigo_postal = propiedad_dto.codigo_postal,
#             area_lote = propiedad_dto.area_lote,
#             estrato_socioeconomico = propiedad_dto.estrato_socioeconomico,
#             valor_venta = propiedad_dto.valor_venta,
#             valor_arriendo_mensual = propiedad_dto.valor_arriendo_mensual,
#             moneda = propiedad_dto.moneda,
#             propietario = propiedad_dto.propietario,
#             arrendatario = propiedad_dto.arrendatario,
#             fecha_ultimo_contrato = propiedad_dto.fecha_ultimo_contrato,
#             fecha_expiracion_contrato_actual = propiedad_dto.fecha_expiracion_contrato_actual,
#             estado = propiedad_dto.estado,
#             id_compania = propiedad_dto.id_compania,
#             id_contrato = propiedad_dto.id_contrato
#         )

#         ejecutar_commando(comando)
#         return Response('{}', status=202, mimetype='application/json')
#     except ExcepcionDominio as e:
#         return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

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
    


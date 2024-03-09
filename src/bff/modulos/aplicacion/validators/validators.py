# Importación de dependencias
from modulos.aplicacion.errors.errors import BadRequest, ErrorConsumoServicioExterno
#from jsonschema import validate
import traceback
#import jsonschema


# Función que valida el http-response-code del consumo de un servicio
def validar_resultado_consumo_servicio(resultado):
    print('<================ validar_resultado_consumo_servicio =====================>')
    print(f'Http-response-code [{resultado.status}]')
    if resultado.status != 200:
        traceback.print_exc()
        raise ErrorConsumoServicioExterno
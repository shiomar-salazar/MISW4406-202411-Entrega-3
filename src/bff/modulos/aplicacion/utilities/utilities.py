import asyncio
import os
import traceback
import aiohttp
from modulos.aplicacion.validators.validators import validar_resultado_consumo_servicio
from modulos.aplicacion.errors.errors import ErrorMetodoNoPermitido

batch_servicios = []


# Función retorna el enpoint del servicio de plan nutricional
def obtener_endpoint_propiedades():
    url= os.getenv('HOST_PROPIEDADES')+os.getenv('API_CONSULTA_PROPIEDADES')
    print(url)
    return url

def obtener_endpoint_companias(direccion):
    url= os.getenv('HOST_COMPANIAS')+os.getenv('API_CONSULTA_COMPANIAS')+'/'+direccion
    print(url)
    return url

def obtener_endpoint_contratos(id_compania,id_propiedad):
    url= os.getenv('HOST_CONTRATOS')+os.getenv('API_CONSULTA_CONTRATOS')+'/'+id_compania+'/'+id_propiedad
    print(url)
    return url



# Función que agregar un nuevo  endpoint de la API a llamar
def agregar_servicio_a_batch(servicio):
    batch_servicios.append(servicio)

# Función que limpia el listado de APIs a llamar
def limpiar_batch_de_servicios():
    batch_servicios.clear()

# Función que permite realizar el consumo de un servicio de forma asincrona
async def consumo_servicio_asincrono(url, metodo, data=None, params=None, headers=None):
    print('<================ consumo_servicio_asincrono-request =====================>')
    print(f'Endpoint [{url}]')
    print(f'Metodo [{metodo}]')
    print(f'Request [{data}]')
    print(f'params [{params}]')
    async with aiohttp.ClientSession() as session:
        if metodo == "POST":
            async with session.post(url, json=data, headers=headers) as resultado:                
                validar_resultado_consumo_servicio(resultado)
                return await resultado.json()
        elif metodo == "GET":
            async with session.get(url,params=params, headers=headers) as resultado:                
                validar_resultado_consumo_servicio(resultado)
                return await resultado.json()
        else:
            raise ErrorMetodoNoPermitido 
    
# Función que permite realizar el consumo en paralelo de servicios
async def ejecucion_batch_en_paralelo():
    tareas = [consumo_servicio_asincrono(url, metodo, data,params, headers) for url, metodo, data,params, headers in batch_servicios]
    resultados = await asyncio.gather(*tareas)
    return resultados
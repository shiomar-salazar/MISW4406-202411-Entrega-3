import asyncio
import os
import traceback
import aiohttp
from modulos.aplicacion.command.base_command import BaseCommannd
from modulos.aplicacion.errors.errors import ApiError
from modulos.aplicacion.utilities.utilities import  obtener_endpoint_propiedades, agregar_servicio_a_batch, limpiar_batch_de_servicios, ejecucion_batch_en_paralelo

# Clase que contiene la logica de creción de Alerta
class ConsultarDatos(BaseCommannd):
    direccion: str
    def __init__(self, direccion):
        self.direccion = direccion

    def agregar_servicio_propiedades(self):
        # Mapeo de información
        headers = {'Content-Type': 'application/json'}
        headers = {'Content-Type': 'application/json'}
        data = {}        
        params = {'direccion': self.direccion}
        agregar_servicio_a_batch((obtener_endpoint_propiedades(), 'GET', data, params, headers))


    # Función que ejecuta el consumo en paralelo de servicios
    def ejecutar_batch_servicios(self):
        self.agregar_servicio_propiedades()
        resultados = asyncio.run(ejecucion_batch_en_paralelo())
        limpiar_batch_de_servicios()
        return resultados
    
    def execute(self):
        try:
            # Logica de negocio
            resultado = self.ejecutar_batch_servicios()            
            return resultado
        except Exception as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        

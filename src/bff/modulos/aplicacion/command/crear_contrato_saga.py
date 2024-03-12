import asyncio
import os
import traceback
import aiohttp
from modulos.aplicacion.command.base_command import BaseCommannd
from modulos.aplicacion.errors.errors import ApiError
from modulos.schema.modelo import PropiedadAlpes, DatosAdicionales
from modulos.aplicacion.utilities.utilities import  obtener_endpoint_contrato_saga, agregar_servicio_a_batch, limpiar_batch_de_servicios, ejecucion_batch_en_paralelo

# Clase que contiene la logica de consulta de propiedades
class CrearContratoSaga(BaseCommannd):    
    request: str
    def __init__(self, request):
        self.request = request

    def agregar_servicio_contrato_saga(self):
        # Mapeo de información
        headers = {'Content-Type': 'application/json'}        
        #data = {request}        
        params = {}
        agregar_servicio_a_batch((obtener_endpoint_contrato_saga(), 'POST', self.request, params, headers))

    # Función que ejecuta el consumo en paralelo de servicios
    def ejecutar_batch_servicios(self):
        self.agregar_servicio_contrato_saga()
        resultados = asyncio.run(ejecucion_batch_en_paralelo())
        limpiar_batch_de_servicios()
        return resultados

    # Función que ejecuta el consumo en paralelo de servicios
    def ejecutar_batch_contratos(self):
        self.agregar_servicio_contratos()        
        resultados = asyncio.run(ejecucion_batch_en_paralelo())
        limpiar_batch_de_servicios()
        return resultados


    def execute(self):
        try:
            # Logica de negocio
            resultado = self.ejecutar_batch_servicios()
            print('propiedad')            
            print(resultado[0])            
           
            print("================Response final")
            print(resultado)
            return resultado
        except Exception as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        
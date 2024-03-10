import asyncio
import os
import traceback
import aiohttp
from modulos.aplicacion.command.base_command import BaseCommannd
from modulos.aplicacion.errors.errors import ApiError
from modulos.schema.modelo import PropiedadAlpes
from modulos.aplicacion.utilities.utilities import  obtener_endpoint_propiedades, obtener_endpoint_companias,obtener_endpoint_contratos, agregar_servicio_a_batch, limpiar_batch_de_servicios, ejecucion_batch_en_paralelo

# Clase que contiene la logica de creción de Alerta
class ConsultarDatos(BaseCommannd):
    direccion: str
    def __init__(self, direccion):
        self.direccion = direccion

    def agregar_servicio_propiedades(self):
        # Mapeo de información
        headers = {'Content-Type': 'application/json'}        
        data = {}        
        params = {'direccion': self.direccion}
        agregar_servicio_a_batch((obtener_endpoint_propiedades(), 'GET', data, params, headers))

    def agregar_servicio_companias(self):
        # Mapeo de información
        headers = {'Content-Type': 'application/json'}        
        data = {}        
        params = {}
        agregar_servicio_a_batch((obtener_endpoint_companias(self.direccion), 'GET', data, params, headers))

    def agregar_servicio_contratos(self,id_compania,id_propiedad):
        # Mapeo de información
        headers = {'Content-Type': 'application/json'}        
        data = {}        
        params = {}
        agregar_servicio_a_batch((obtener_endpoint_contratos(id_compania,id_propiedad), 'GET', data, params, headers))

    # Función que ejecuta el consumo en paralelo de servicios
    def ejecutar_batch_servicios(self):
        self.agregar_servicio_propiedades()
        self.agregar_servicio_companias()
        resultados = asyncio.run(ejecucion_batch_en_paralelo())
        limpiar_batch_de_servicios()
        return resultados

    # Función que ejecuta el consumo en paralelo de servicios
    def ejecutar_batch_contratos(self,id_compania,id_propiedad):
        self.agregar_servicio_contratos(id_compania,id_propiedad)        
        resultados = asyncio.run(ejecucion_batch_en_paralelo())
        limpiar_batch_de_servicios()
        return resultados


    def execute(self):
        try:
            # Logica de negocio
            resultado = self.ejecutar_batch_servicios()
            #resultado_contrato = self.ejecutar_batch_contratos(resultado[1].get("id_compania"),resultado[0].get("_id"))
            print('propiedad')            
            print(resultado[0])            
            print('compania')            
            print(resultado[1])   
            print('contratos')            
            #print(resultado_contrato[0])   


            propiedadAlpes=PropiedadAlpes(
                propiedad=resultado[0],
                compania=resultado[1],
                #contrato=resultado_contrato[0]
            )
            print(propiedadAlpes)
            return propiedadAlpes.__dict__
        except Exception as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        

from seedwork.infraestructura.vistas import Vista
from modulos.companias.infraestructura.redis import RedisRepositorio
from modulos.companias.dominio.entidades import Compania
from config.db import db
from .dto import Compania as CompaniaDTO
import json



class VistaCompania(Vista):
    def obtener_todos(self):
        companias = list()
        redis = RedisRepositorio()
        companiasRedis = redis.lrange('companias', 0, -1)
        for compania_dto in companiasRedis:
            fixed = compania_dto.decode('utf-8')
            fixed = fixed.replace("'", '"')
            compania_dto = json.loads(fixed)

            companias.append(CompaniaDTO(id = compania_dto['id'],
                                        nombre_compania = compania_dto['nombre_compania'],
                                        representante_legal = compania_dto['representante_legal'],
                                        email_contacto = compania_dto['email_contacto'],
                                        telefono_contacto = compania_dto['telefono_contacto'],
                                        estado = compania_dto['estado'],
                                        documento_identidad_numero_identificacion = compania_dto['documento_identidad_numero_identificacion'],
                                        documento_identidad_tipo = compania_dto['documento_identidad_tipo'],
                                        tipo_industria = compania_dto['tipo_industria'],
                                        direccion = compania_dto['direccion'],
                                        latitud = compania_dto['latitud'],
                                        longitud = compania_dto['longitud'],
                                        ciudad = compania_dto['ciudad'],
                                        pais = compania_dto['pais']
                                        ))

        return companias
    
    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Método no implementado')

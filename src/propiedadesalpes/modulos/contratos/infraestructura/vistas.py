from seedwork.infraestructura.vistas import Vista
from modulos.contratos.infraestructura.redis import RedisRepositorio
from modulos.contratos.dominio.entidades import Contrato
from config.db import db
from .dto import Contrato as ContratoDTO
import json



class VistaContrato(Vista):
    def obtener_todos(self):
        contratos = list()
        redis = RedisRepositorio()
        contratosRedis = redis.lrange('contratos', 0, -1)
        for contrato_dto in contratosRedis:
            fixed = contrato_dto.decode('utf-8')
            fixed = fixed.replace("'", '"')
            contrato_dto = json.loads(fixed)

            contratos.append(ContratoDTO(id = contrato_dto['id'],
                                        id_propiedad = contrato_dto['id_propiedad'],
                                        id_compania = contrato_dto['id_compania'],
                                        fecha_inicio = contrato_dto['fecha_inicio'],
                                        telefono_contacto = contrato_dto['telefono_contacto'],
                                        fecha_fin = contrato_dto['fecha_fin'],
                                        fecha_ejecucion = contrato_dto['fecha_ejecucion'],
                                        monto = contrato_dto['monto'],
                                        tipo = contrato_dto['tipo']
                                        ))

        return contratos
    
    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Método no implementado')

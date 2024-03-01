from seedwork.infraestructura.vistas import Vista
from modulos.propiedades.infraestructura.redis import RedisRepositorio
from modulos.propiedades.dominio.entidades import Propiedad
from config.db import db
from .dto import Propiedad as PropiedadDTO
import json

class VistaPropiedad(Vista):
    def obtener_todos(self):
        propiedades = list()
        redis = RedisRepositorio()
        propiedadesRedis = redis.lrange('propiedades', 0, -1)
        for propiedad_dto in propiedadesRedis:
            fixed = propiedad_dto.decode('utf-8')
            fixed = fixed.replace("'", '"')
            propiedad_dto = json.loads(fixed)

            propiedades.append(PropiedadDTO(id = propiedad_dto["id"],
                        nombre_propiedad = propiedad_dto["nombre_propiedad"],
                        tipo_propiedad = propiedad_dto["tipo_propiedad"],
                        pais = propiedad_dto["pais"],
                        departamento = propiedad_dto["departamento"],
                        ciudad = propiedad_dto["ciudad"],
                        direccion = propiedad_dto["direccion"],
                        latitud = propiedad_dto["latitud"],
                        longitud = propiedad_dto["longitud"],
                        codigo_postal = propiedad_dto["codigo_postal"],
                        area_lote = propiedad_dto["area_lote"],
                        estrato_socioeconomico = propiedad_dto["estrato_socioeconomico"],
                        valor_venta = propiedad_dto["valor_venta"],
                        valor_arriendo_mensual = propiedad_dto["valor_arriendo_mensual"],
                        moneda = propiedad_dto["moneda"],
                        propietario = propiedad_dto["propietario"],
                        arrendatario = propiedad_dto["arrendatario"],
                        fecha_ultimo_contrato = propiedad_dto["fecha_ultimo_contrato"],
                        fecha_expiracion_contrato_actual = propiedad_dto["fecha_expiracion_contrato_actual"],
                        estado = propiedad_dto["estado"],
                        id_compania = propiedad_dto["id_compania"],
                        id_contrato = propiedad_dto["id_contrato"]
                )
            )

        return propiedades
    
    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs):
        raise NotImplementedError('Método no implementado')

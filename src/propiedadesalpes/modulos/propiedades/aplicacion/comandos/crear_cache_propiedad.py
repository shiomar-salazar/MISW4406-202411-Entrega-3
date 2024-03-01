
from dataclasses import dataclass, field

from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from seedwork.aplicacion.comandos import ejecutar_commando as comando
from modulos.propiedades.infraestructura.redis import RedisRepositorio

@dataclass
class CrearCachePropiedad(Comando):
    id_propiedad: str = field(default_factory=str)
    nombre_propiedad: str = field(default_factory=str)
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=str)
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad_tipo: str = field(default_factory=str)
    documento_identidad_numero_identificacion: str = field(default_factory=str)
    tipo_industria: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)

class CrearCachePropiedadHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: CrearCachePropiedad):
        propiedad_dto = PropiedadDTO(
            id_propiedad= comando.id_propiedad,
            nombre_propiedad=comando.nombre_propiedad,
            representante_legal=comando.representante_legal,
            email_contacto=comando.email_contacto,
            telefono_contacto=comando.telefono_contacto,
            estado=comando.estado,
            documento_identidad_tipo=comando.documento_identidad_tipo,
            documento_identidad_numero_identificacion=comando.documento_identidad_numero_identificacion,
            tipo_industria=comando.tipo_industria,
            direccion=comando.direccion,
            ciudad=comando.ciudad,
            pais=comando.pais,
            latitud=comando.latitud,
            longitud=comando.longitud,
            )
        

        propiedad_ext = {
            "id_propiedad": comando.id_propiedad,
            "nombre_propiedad": comando.nombre_propiedad,
            "representante_legal": comando.representante_legal,
            "email_contacto": comando.email_contacto,
            "telefono_contacto": comando.telefono_contacto,
            "estado": comando.estado,
            "documento_identidad_tipo": comando.documento_identidad_tipo,
            "documento_identidad_numero_identificacion": comando.documento_identidad_numero_identificacion,
            "tipo_industria": comando.tipo_industria,
            "direccion": comando.direccion,
            "ciudad": comando.ciudad,
            "pais": comando.pais,
            "latitud": comando.latitud,
            "longitud": comando.longitud

        }
        redis = RedisRepositorio()
        redis.lpush("propiedades", str(propiedad_ext))

@comando.register(CrearCachePropiedad)
def ejecutar_comando_crear_propiedad_cache(comando: CrearCachePropiedad):
    handler = CrearCachePropiedadHandler()
    handler.handle(comando)
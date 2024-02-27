
from dataclasses import dataclass, field
from datetime import datetime

from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import CompaniaDTO
from modulos.propiedades.dominio.entidades import Compania
from modulos.propiedades.aplicacion.comandos.base import CrearCompaniaBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorCompania
from seedwork.aplicacion.comandos import ejecutar_commando as comando
from modulos.propiedades.infraestructura.redis import RedisRepositorio

@dataclass
class CrearCacheCompania(Comando):
    id_compania: str = field(default_factory=str)
    nombre_compania: str = field(default_factory=str)
    representante_legal: str = field(default_factory=str)
    email_contacto: float = field(default_factory=str)
    telefono_contacto: datetime = field(default_factory=str)
    estado: datetime = field(default_factory=str)
    documento_identidad_tipo: datetime = field(default_factory=str)
    documento_identidad_numero_identificacion: datetime = field(default_factory=str)
    tipo_industria: int = field(default_factory=str)
    direccion: int = field(default_factory=str)
    ciudad: int = field(default_factory=str)
    pais: int = field(default_factory=str)
    latitud: int = field(default_factory=str)
    longitud: int = field(default_factory=str)

class CrearCacheCompaniaHandler(CrearCompaniaBaseHandler):
    def handle(self, comando: CrearCacheCompania):
        compania_dto = CompaniaDTO(
            id_compania= comando.id_compania,
            nombre_compania=comando.nombre_compania,
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
        

        compania_ext = {
            "id_compania": comando.id_compania,
            "nombre": comando.nombre,
            "descripcion": comando.descripcion,
            "direccion": comando.direccion,
            "precio": comando.precio,
            "fecha_creacion": comando.fecha_creacion,
            "fecha_actualizacion": comando.fecha_actualizacion,
            "fecha_publicacion": comando.fecha_publicacion,
            "fecha_baja": comando.fecha_baja,
            "estado": comando.estado,
            "tipo": comando.tipo,
            "habitaciones": comando.habitaciones,
            "banos": comando.banos,
            "estacionamientos": comando.estacionamientos,
            "superficie": comando.superficie,
            "imagen": comando.imagen
        }
        redis = RedisRepositorio()
        redis.lpush("companias", str(compania_ext))

@comando.register(CrearCacheCompania)
def ejecutar_comando_crear_reserva_cache(comando: CrearCacheCompania):
    handler = CrearCacheCompaniaHandler()
    handler.handle(comando)

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
    id_compania : str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    descripcion: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    precio: float = field(default_factory=float)
    fecha_creacion: datetime = field(default_factory=datetime.now)
    fecha_actualizacion: datetime = field(default_factory=datetime.now)
    fecha_publicacion: datetime = field(default_factory=datetime.now)
    fecha_baja: datetime = field(default_factory=datetime.now)
    estado: int = field(default_factory=int)
    tipo: int = field(default_factory=int)
    habitaciones: int = field(default_factory=int)
    banos: int = field(default_factory=int)
    estacionamientos: int = field(default_factory=int)
    superficie: int = field(default_factory=int)
    imagen: str = field(default_factory=str)

class CrearCacheCompaniaHandler(CrearCompaniaBaseHandler):
    def handle(self, comando: CrearCacheCompania):
        compania_dto = CompaniaDTO(
            id_compania= comando.id_compania,
            nombre=comando.nombre,
            descripcion=comando.descripcion,
            direccion=comando.direccion,
            precio=comando.precio,
            fecha_creacion=comando.fecha_creacion,
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_publicacion=comando.fecha_publicacion,
            fecha_baja=comando.fecha_baja,
            estado=comando.estado,
            tipo=comando.tipo,
            habitaciones=comando.habitaciones,
            banos=comando.banos,
            estacionamientos=comando.estacionamientos,
            superficie=comando.superficie,
            imagen=comando.imagen)
        
        # compania : Compania = self._fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        # compania.crear_compania(compania)

        # map_compania = MapeadorCompania()
        # compania_ext = map_compania.entidad_a_externo(compania)
        # print(f"COMPANIA QUE SE ENVIA A JSON {str(compania_ext)}")
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
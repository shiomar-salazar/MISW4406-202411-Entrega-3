from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from modulos.propiedades.dominio.entidades import Compania
from .dto import CompaniaDTO

from datetime import datetime

class MapeadorCompaniaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.nombre = externo.get("nombre")
        compania_dto.descripcion = externo.get("descripcion")
        compania_dto.direccion = externo.get("direccion")
        compania_dto.precio = externo.get("precio")
        compania_dto.estado = externo.get("estado")
        compania_dto.imagen = externo.get("imagen")
        compania_dto.fecha_creacion = datetime.now()
        compania_dto.fecha_actualizacion = datetime.now()
        compania_dto.habitaciones = externo.get("habitaciones")
        compania_dto.banos = externo.get("banos")
        return compania_dto
    
    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return dto.__dict__


class MapeadorCompania(RepMap):
    _FORMATO_FECHA = "%Y-%m-%dT%H:%M:%SZ"
    def obtener_tipo(self) -> type:
        return Compania.__class__ 
    
    def entidad_a_dto(self, entidad: Compania) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id_compania = entidad.id
        compania_dto.nombre = entidad.nombre
        compania_dto.descripcion = entidad.descripcion
        compania_dto.tipo = entidad.tipo
        compania_dto.estado = entidad.estado
        compania_dto.imagen = entidad.imagen
        compania_dto.fecha_creacion = entidad.fecha_creacion
        compania_dto.fecha_actualizacion = entidad.fecha_actualizacion
        compania_dto.habitaciones = entidad.habitaciones
        compania_dto.banos = entidad.banos
        compania_dto.precio = entidad.precio
        compania_dto.superficie = entidad.superficie
        compania_dto.direccion = entidad.direccion
        return compania_dto
    
    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        compania = Compania()
        compania.nombre=dto.nombre
        compania.descripcion=dto.descripcion
        compania.tipo=dto.tipo 
        compania.estado=dto.estado 
        compania.fecha_creacion=dto.fecha_creacion 
        compania.fecha_actualizacion=dto.fecha_actualizacion 
        compania.habitaciones=dto.habitaciones 
        compania.precio= dto.precio 
        compania.superficie= dto.superficie
        compania.direccion=dto.direccion
        compania.imagen=dto.imagen
        compania.banos =dto.banos
        return compania
    
    def entidad_a_externo(self, dto: Compania) -> dict:
        dto._id = str(dto._id)
        dto.id_compania = str(dto.id_compania)
        dto.fecha_creacion = str(dto.fecha_creacion)
        dto.fecha_actualizacion = str(dto.fecha_actualizacion)
        dto.fecha_baja = str(dto.fecha_baja)
        dto.fecha_publicacion = str(dto.fecha_publicacion)
        return dto.__dict__

from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.comandos.base import EliminarPropiedadBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from seedwork.infraestructura.uow import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class EliminarPropiedad(Comando):
    id_propiedad: str = field(default_factory=str)   

class EliminarPropiedadHandler(EliminarPropiedadBaseHandler):
    def handle(self, comando: EliminarPropiedad):
        propiedad_dto = PropiedadDTO(
            id_propiedad = comando.id_propiedad
        )
        propiedad : Propiedad = self._fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.eliminar_propiedad(propiedad)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, propiedad)
        UnidadTrabajoPuerto.commit()

@comando.register(EliminarPropiedad)
def ejecutar_comando_eliminar(comando: EliminarPropiedad):
    handler = EliminarPropiedadHandler()
    handler.handle(comando)
from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import Comando
from modulos.companias.aplicacion.comandos.base import RollbackCompaniaBaseHandler
from modulos.companias.infraestructura.repositorios import RepositorioCompanias
from modulos.companias.dominio.entidades import Compania
from modulos.companias.aplicacion.mapeadores import MapeadorCompania
from modulos.companias.aplicacion.dto import CompaniaDTO
from seedwork.infraestructura.uow import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class RollbackCompania(Comando):
    id_compania: str = field(default_factory=str)

class RollbackCompaniaHandler(RollbackCompaniaBaseHandler):
    def handle(self, comando: RollbackCompania):
        compania_dto = CompaniaDTO(
            id_compania=comando.id_compania
            )
        
        compania : Compania = self._fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        compania.eliminar_compania(compania)

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar_por_id, compania_dto.id_compania)
        UnidadTrabajoPuerto.commit()


@comando.register(RollbackCompania)
def ejecutar_comando_rollback_compania(comando: RollbackCompania):
    handler = RollbackCompaniaHandler()
    handler.handle(comando)
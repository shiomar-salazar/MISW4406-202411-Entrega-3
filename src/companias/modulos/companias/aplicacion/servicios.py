from seedwork.aplicacion.servicios import Servicio
from modulos.companias.infraestructura.fabricas import FabricaRepositorio
from modulos.companias.dominio.fabricas import FabricaCompanias
from modulos.companias.dominio.entidades import Compania
from modulos.companias.infraestructura.repositorios import RepositorioCompanias
from seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .dto import CompaniaDTO
from .mapeadores import MapeadorCompania

class ServicioCompania(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio 
    
    @property
    def _fabrica_companias(self):
        return self._fabrica_companias
    
    def crear_compania(self, dto: CompaniaDTO) -> CompaniaDTO:
        compania : Compania = self._fabrica_companias.crear_objeto(dto, MapeadorCompania())
        compania.crear_compania(compania)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.commit()

        return self._fabrica_companias.crear_objeto(compania, MapeadorCompania())
    
    def obtener_compania_por_id(self, id) -> CompaniaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        return self._fabrica_companias.crear_objeto(repositorio.obtener_por_id(id), MapeadorCompania())
    
    def eliminar_compania_por_id(self, id):
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar_por_id, id)
        UnidadTrabajoPuerto.commit()
        
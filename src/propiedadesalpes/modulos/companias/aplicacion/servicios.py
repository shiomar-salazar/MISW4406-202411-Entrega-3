from propiedadesalpes.seedwork.aplicacion.servicios import Servicio
from propiedadesalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propiedadesalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias
from propiedadesalpes.modulos.companias.dominio.fabricas import FabricaCompanias
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from propiedadesalpes.modulos.companias.aplicacion.dto import CompaniaDTO
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompania




import asyncio

class ServicioCompanias(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_compania: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_compania       
    
    def crear_compania(self, compania_dto: CompaniaDTO) -> CompaniaDTO:
        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())       
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self._fabrica_compania.crear_objeto(compania, MapeadorCompania())

    def obtener_compania_por_id(self) -> CompaniaDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)
        return self._fabrica_compania.crear_objeto(repositorio, MapeadorCompania())

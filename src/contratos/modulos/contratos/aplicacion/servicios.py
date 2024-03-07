from seedwork.aplicacion.servicios import Servicio
from modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from modulos.contratos.dominio.fabricas import FabricaContratos
from modulos.contratos.dominio.entidades import Contrato
from modulos.contratos.infraestructura.repositorios import RepositorioContratos
from seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .dto import ContratoDTO
from .mapeadores import MapeadorContrato

class ServicioContrato(Servicio):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio 
    
    @property
    def _fabrica_contratos(self):
        return self._fabrica_contratos
    
    def crear_contrato(self, dto: ContratoDTO) -> ContratoDTO:
        contrato : Contrato = self._fabrica_contratos.crear_objeto(dto, MapeadorContrato())
        contrato.crear_contrato(contrato)
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        
        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, contrato)
        UnidadTrabajoPuerto.commit()

        return self._fabrica_contratos.crear_objeto(contrato, MapeadorContrato())
    
    def obtener_contrato_por_id(self, id) -> ContratoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        return self._fabrica_contratos.crear_objeto(repositorio.obtener_por_id(id), MapeadorContrato())
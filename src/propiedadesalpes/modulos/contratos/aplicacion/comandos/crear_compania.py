
from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import Comando
from modulos.contratos.aplicacion.dto import ContratoDTO
from modulos.contratos.dominio.entidades import Contrato
from modulos.contratos.aplicacion.comandos.base import CrearContratoBaseHandler
from modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from modulos.contratos.infraestructura.repositorios import RepositorioContratos
from seedwork.infraestructura.uow import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class CrearContrato(Comando):
    id_contrato: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    id_compania: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)
    fecha_ejecucion: str = field(default_factory=str)
    monto: int = field(default_factory=int)
    tipo: str = field(default_factory=str)

class CrearContratoHandler(CrearContratoBaseHandler):
    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
            id_contrato=comando.id_contrato,
            id_propiedad=comando.id_propiedad,
            id_compania=comando.id_compania,
            fecha_inicio=comando.fecha_inicio,
            fecha_fin=comando.fecha_fin,
            fecha_ejecucion=comando.fecha_ejecucion,
            monto=comando.monto,
            tipo=comando.tipo,
            )
        
        contrato : Contrato = self._fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        contrato.crear_contrato(contrato)

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, contrato)
        UnidadTrabajoPuerto.commit()

@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
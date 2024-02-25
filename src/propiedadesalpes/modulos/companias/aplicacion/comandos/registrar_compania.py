from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.companias.aplicacion.dto import DocumentoIdentidadDTO, TipoIndustriaDTO, LocalizacionDTO, CompaniaDTO
from .base import RegistrarCompaniaBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorCompania
from propiedadesalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias

@dataclass
class RegistrarCompania(Comando):
    id: int = field(default_factory=int)
    nombre_compania: str = field(default_factory=str)
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=str)
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad: DocumentoIdentidadDTO = field(default_factory=DocumentoIdentidadDTO)
    tipo_industria: TipoIndustriaDTO = field(default_factory=TipoIndustriaDTO)
    localizacion: LocalizacionDTO = field(default_factory=LocalizacionDTO)


class RegistrarCompaniaHandler(RegistrarCompaniaBaseHandler):
    
    def handle(self, comando: RegistrarCompania):
        compania_dto = CompaniaDTO(
                id=comando.id,
                nombre_compania=comando.nombre_compania,
                representante_legal=comando.representante_legal,
                email_contacto=comando.email_contacto,
                telefono_contacto=comando.telefono_contacto,
                estado=comando.estado,
                documento_identidad=comando.documento_identidad,
                tipo_industria=comando.tipo_industria,
                localizacion=comando.localizacion)

        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())       
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(RegistrarCompania)
def ejecutar_comando_registra_compania(comando: RegistrarCompania):
    handler = RegistrarCompaniaHandler()
    handler.handle(comando)
    
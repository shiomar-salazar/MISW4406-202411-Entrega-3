
from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import Comando
from modulos.companias.aplicacion.dto import CompaniaDTO
from modulos.companias.dominio.entidades import Compania
from modulos.companias.aplicacion.comandos.base import CrearCompaniaBaseHandler
from modulos.companias.aplicacion.mapeadores import MapeadorCompania
from modulos.companias.infraestructura.repositorios import RepositorioCompanias
from seedwork.infraestructura.uow import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class CrearCompania(Comando):
    id_compania: str = field(default_factory=str)
    nombre_compania: str = field(default_factory=str)
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=float)
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad_tipo: str = field(default_factory=str)
    documento_identidad_numero_identificacion: str = field(default_factory=str)
    tipo_industria: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    latitud: str = field(default_factory=str)
    longitud: str = field(default_factory=str)


class CrearCompaniaHandler(CrearCompaniaBaseHandler):
    def handle(self, comando: CrearCompania):
        compania_dto = CompaniaDTO(
            id_compania=comando.id_compania,
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
        
        compania : Compania = self._fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        compania.crear_compania(compania)

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        UnidadTrabajoPuerto.commit()

@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
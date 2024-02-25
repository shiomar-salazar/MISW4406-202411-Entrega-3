from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.companias.aplicacion.dto import DocumentoIdentidadDTO, TipoIndustriaDTO, LocalizacionDTO, CompañiaDTO
from .base import RegistrarCompañiaBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.companias.dominio.entidades import Reserva
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorReserva
from propiedadesalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias

@dataclass
class RegistrarCompañia(Comando):
    id: int = field(default_factory=int)
    nombre_compañia: str = field(default_factory=str)
    representante_legal: str = field(default_factory=str)
    email_contacto: str = field(default_factory=str)
    telefono_contacto: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    documento_identidad: DocumentoIdentidadDTO = field(default_factory=DocumentoIdentidadDTO)
    tipo_industria: TipoIndustriaDTO = field(default_factory=TipoIndustriaDTO)
    localizacion: LocalizacionDTO = field(default_factory=LocalizacionDTO)


class RegistrarCompañiaHandler(RegistrarCompañiaBaseHandler):
    
    def handle(self, comando: RegistrarCompañia):
        compañia_dto = CompañiaDTO(
                id=comando.id,
                nombre_compañia=comando.nombre_compañia,
                representante_legal=comando.representante_legal,
                email_contacto=comando.email_contacto,
                telefono_contacto=comando.telefono_contacto,
                estado=comando.estado,
                documento_identidad=comando.documento_identidad,
                tipo_industria=comando.tipo_industria,
                localizacion=comando.localizacion)

        #reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        #reserva.crear_reserva(reserva)

        #repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        #UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        #UnidadTrabajoPuerto.savepoint()
        #UnidadTrabajoPuerto.commit()


@comando.register(RegistrarCompañia)
def ejecutar_comando_registra_compañia(comando: RegistrarCompañia):
    handler = RegistrarCompañiaHandler()
    handler.handle(comando)
    
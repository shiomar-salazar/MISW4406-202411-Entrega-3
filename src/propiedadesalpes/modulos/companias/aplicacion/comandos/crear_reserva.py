from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.companias.aplicacion.dto import ItinerarioDTO, ReservaDTO
from .base import CrearReservaBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.companias.dominio.entidades import Reserva
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedadesalpes.modulos.companias.aplicacion.mapeadores import MapeadorReserva
from propiedadesalpes.modulos.companias.infraestructura.repositorios import RepositorioCompanias

@dataclass
class CrearReserva(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    itinerarios: list[ItinerarioDTO]


class CrearReservaHandler(CrearReservaBaseHandler):
    
    def handle(self, comando: CrearReserva):
        reserva_dto = ReservaDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   itinerarios=comando.itinerarios)

        reserva: Reserva = self.fabrica_vuelos.crear_objeto(reserva_dto, MapeadorReserva())
        reserva.crear_reserva(reserva)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, reserva)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearReserva)
def ejecutar_comando_crear_reserva(comando: CrearReserva):
    handler = CrearReservaHandler()
    handler.handle(comando)
    
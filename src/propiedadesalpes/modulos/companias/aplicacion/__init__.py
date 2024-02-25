from pydispatch import dispatcher

from .handlers import HandlerReservaIntegracion

# from propiedadesalpes.modulos.companias.dominio.eventos import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from propiedadesalpes.modulos.companias.dominio.eventos import CompaniaCreada

dispatcher.connect(HandlerReservaIntegracion.handle_reserva_creada, signal=f'{CompaniaCreada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
# dispatcher.connect(HandlerReservaIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')
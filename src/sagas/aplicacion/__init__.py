from pydispatch import dispatcher
from .handlers import HandlerContratoSagaDominio

dispatcher.connect(HandlerContratoSagaDominio.handle_saga_contrato_creada, signal='ContratoSagaCreadaDominio')


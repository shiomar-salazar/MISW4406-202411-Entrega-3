from pydispatch import dispatcher
from .handlers import HandlerContratoDominio

dispatcher.connect(HandlerContratoDominio.handle_contrato_creado, signal='ContratoCreadoDominio')

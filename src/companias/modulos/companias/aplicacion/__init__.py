from pydispatch import dispatcher
from .handlers import HandlerCompaniaDominio

dispatcher.connect(HandlerCompaniaDominio.handle_compania_creada, signal='CompaniaCreadaDominio')
dispatcher.connect(HandlerCompaniaDominio.handle_compania_eliminada, signal='CompaniaEliminadaDominio')


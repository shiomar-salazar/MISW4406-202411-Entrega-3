

from modulos.companias.dominio.eventos import CompaniaCreada
from seedwork.aplicacion.handlers import Handler
from modulos.companias.infraestructura.despachadores import Despachador

class HandlerCompaniaDominio(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento(evento, 'eventos-compania')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
        
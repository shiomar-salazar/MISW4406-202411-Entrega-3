

from modulos.contratos.dominio.eventos import ContratoCreado
from seedwork.aplicacion.handlers import Handler
from modulos.contratos.infraestructura.despachadores import Despachador

class HandlerContratoDominio(Handler):

    @staticmethod
    def handle_contrato_creado(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento_rabbit(evento, 'eventos-contrato')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
        
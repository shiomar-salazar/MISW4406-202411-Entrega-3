from seedwork.aplicacion.handlers import Handler
from infraestructura.despachadores import Despachador

class HandlerContratoSagaDominio(Handler):

    @staticmethod
    def handle_saga_contrato_creada(evento):
        try:
            despachador = Despachador()
            despachador.publicar_evento(evento, 'eventos-saga-contratos')
        except Exception as e:
            print(f"ERROR AL PUBLICAR {e}")
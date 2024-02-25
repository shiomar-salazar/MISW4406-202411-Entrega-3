from propiedadesalpes.modulos.companias.dominio.eventos import CompaniaCreada
from propiedadesalpes.seedwork.aplicacion.handlers import Handler
from propiedadesalpes.modulos.companias.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')
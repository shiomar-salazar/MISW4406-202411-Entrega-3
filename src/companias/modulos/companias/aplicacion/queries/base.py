from seedwork.aplicacion.queries import QueryHandler
from modulos.companias.infraestructura.fabricas import FabricaVista
from modulos.companias.dominio.fabricas import FabricaCompanias

class CompaniaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_companias    
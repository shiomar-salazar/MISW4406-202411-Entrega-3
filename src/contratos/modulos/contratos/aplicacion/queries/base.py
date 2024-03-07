from seedwork.aplicacion.queries import QueryHandler
from modulos.contratos.infraestructura.fabricas import FabricaVista
from modulos.contratos.dominio.fabricas import FabricaContratos

class ContratoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_vista: FabricaVista = FabricaVista()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_contratos    
from propiedadesalpes.seedwork.aplicacion.queries import QueryHandler
from propiedadesalpes.modulos.compañias.infraestructura.fabricas import FabricaRepositorio
from propiedadesalpes.modulos.compañias.dominio.fabricas import FabricaCompania

class CompaniaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_compania: FabricaCompania = FabricaCompania()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_compania(self):
        return self._fabrica_compania 
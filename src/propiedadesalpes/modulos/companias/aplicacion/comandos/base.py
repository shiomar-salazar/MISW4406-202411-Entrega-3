from propiedadesalpes.seedwork.aplicacion.comandos import ComandoHandler
from propiedadesalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio

class RegistrarCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()        

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
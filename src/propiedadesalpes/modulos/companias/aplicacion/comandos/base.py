from propiedadesalpes.seedwork.aplicacion.comandos import ComandoHandler
from propiedadesalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propiedadesalpes.modulos.companias.dominio.fabricas import FabricaCompanias

class RegistrarCompaniaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()        
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    

    @property
    def fabrica_companias(self):
        return self._fabrica_companias    
    
    
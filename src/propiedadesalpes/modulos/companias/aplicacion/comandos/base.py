from propiedadesalpes.seedwork.aplicacion.comandos import ComandoHandler
from propiedadesalpes.modulos.companias.infraestructura.fabricas import FabricaRepositorio
from propiedadesalpes.modulos.companias.dominio.fabricas import FabricaVuelos

class CrearReservaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    
    
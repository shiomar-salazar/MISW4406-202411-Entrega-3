from seedwork.dominio.excepciones import ExcepcionFabrica

class NoExisteImplementacionParaTipoFabricaExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una implementación para el repositorio con el tipo dado.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)

class PropiedadNoEncontradoExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No se encontró ningúna propiedad con los valores especificados.'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)        
""" Excepciones del dominio de Companias

En este archivo usted encontrará los Excepciones relacionadas
al dominio de Companias

"""

from propiedadesalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioCompaniasExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de Companias'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)
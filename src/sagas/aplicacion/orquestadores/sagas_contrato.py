from sagas.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from sagas.seedwork.aplicacion.comandos import Comando
from sagas.seedwork.dominio.eventos import EventoDominio

from companias.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania
from companias.modulos.companias.dominio.eventos import CompaniaCreada, CompaniaCreadaFallida
from companias.modulos.companias.aplicacion.comandos.rollback import RollbackCompania

from propiedades.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreada

from contratos.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from contratos.modulos.contratos.dominio.eventos import ContratoCreado


class CoordiandorContratos(CoordinadorOrquestacion):
    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearCompania, evento=CompaniaCreada, error=None, compensacion=None),
            #Transaccion(index=2, comando=, evento=, error=CompaniaCreadaFallida, compensacion=RollbackCompania),
            Transaccion(index=3, comando=CrearPropiedad, evento=PropiedadCreada, error=None, compensacion=None),
            #Transaccion(index=4, comando=, evento=, error=PropiedadCreadaFallida, compensacion=None),
            Transaccion(index=5, comando=CrearContrato, evento=ContratoCreado, error=None, compensacion=None),
            #Transaccion(index=6, comando=, evento=, error=ContratoCreadoFallido, compensacion=None),
            Fin(index=7)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])

    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        ...

    def oir_mensaje(mensaje):
        if isinstance(mensaje, EventoDominio):
            coordinador = CoordiandorContratos()
            coordinador.procesar_evento(mensaje)
        else:
            raise NotImplementedError("El mensaje no es evento de Dominio")
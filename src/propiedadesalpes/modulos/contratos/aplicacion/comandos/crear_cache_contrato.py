
from dataclasses import dataclass, field

from seedwork.aplicacion.comandos import Comando
from modulos.contratos.aplicacion.dto import ContratoDTO
from modulos.contratos.dominio.entidades import Contrato
from modulos.contratos.aplicacion.comandos.base import CrearContratoBaseHandler
from modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from seedwork.aplicacion.comandos import ejecutar_commando as comando
from modulos.contratos.infraestructura.redis import RedisRepositorio

@dataclass
class CrearCacheContrato(Comando):
    id_contrato: str = field(default_factory=str)
    id_propiedad: str = field(default_factory=str)
    id_compania: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)
    fecha_ejecucion: str = field(default_factory=str)
    monto: int  = field(default_factory=int )
    tipo: str = field(default_factory=str)

class CrearCacheContratoHandler(CrearContratoBaseHandler):
    def handle(self, comando: CrearCacheContrato):
        contrato_dto = ContratoDTO(
            id_contrato= comando.id_contrato,
            id_propiedad=comando.id_propiedad,
            id_compania=comando.id_compania,
            fecha_inicio=comando.fecha_inicio,
            fecha_fin=comando.fecha_fin,
            fecha_ejecucion=comando.fecha_ejecucion,
            monto=comando.monto,
            tipo=comando.tipo,
            )
        

        contrato_ext = {
            "id_contrato": comando.id_contrato,
            "id_propiedad": comando.id_propiedad,
            "id_compania": comando.id_compania,
            "fecha_inicio": comando.fecha_inicio,
            "fecha_fin": comando.fecha_fin,
            "fecha_ejecucion": comando.fecha_ejecucion,
            "monto": comando.monto,
            "tipo": comando.tipo,
        }
        redis = RedisRepositorio()
        redis.lpush("contratos", str(contrato_ext))

@comando.register(CrearCacheContrato)
def ejecutar_comando_crear_contrato_cache(comando: CrearCacheContrato):
    handler = CrearCacheContratoHandler()
    handler.handle(comando)
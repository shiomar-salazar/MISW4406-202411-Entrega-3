
from dataclasses import dataclass, field
from seedwork.aplicacion.comandos import Comando
from modulos.propiedades.aplicacion.dto import PropiedadDTO
from modulos.propiedades.dominio.entidades import Propiedad
from modulos.propiedades.aplicacion.comandos.base import CrearPropiedadBaseHandler
from modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from modulos.propiedades.infraestructura.repositorios import RepositorioPropiedades
from seedwork.infraestructura.uow import UnidadTrabajoPuerto
from seedwork.aplicacion.comandos import ejecutar_commando as comando

@dataclass
class CrearPropiedad(Comando):
    id_propiedad: str = field(default_factory=str)
    nombre_propiedad: str = field(default_factory=str)   
    tipo_propiedad: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    departamento: str = field(default_factory=str)
    ciudad: str = field(default_factory=str)
    direccion: str = field(default_factory=str)   
    latitud : str = field(default_factory=str)
    longitud: str = field(default_factory=str)
    codigo_postal: str = field(default_factory=str)
    area_lote: str = field(default_factory=str)
    estrato_socioeconomico: str = field(default_factory=str)
    valor_venta : str = field(default_factory=str)
    valor_arriendo_mensual : str = field(default_factory=str)
    moneda : str = field(default_factory=str)
    propietario : str = field(default_factory=str)
    arrendatario : str = field(default_factory=str)
    fecha_ultimo_contrato : str = field(default_factory=str)
    fecha_expiracion_contrato_actual : str = field(default_factory=str)
    estado : str = field(default_factory=str)
    id_compania : str = field(default_factory=str)
    id_contrato : str = field(default_factory=str)  


class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    def handle(self, comando: CrearPropiedad):
        propiedad_dto = PropiedadDTO(
            id_propiedad = comando.id_propiedad,
            nombre_propiedad = comando.nombre_propiedad,
            tipo_propiedad = comando.tipo_propiedad,
            pais = comando.pais,
            departamento = comando.departamento,
            ciudad = comando.ciudad,
            direccion = comando.direccion,
            latitud = comando.latitud,
            longitud = comando.longitud,
            codigo_postal = comando.codigo_postal,
            area_lote = comando.area_lote,
            estrato_socioeconomico = comando.estrato_socioeconomico,
            valor_venta = comando.valor_venta,
            valor_arriendo_mensual = comando.valor_arriendo_mensual,
            moneda = comando.moneda,
            propietario = comando.propietario,
            arrendatario = comando.arrendatario,
            fecha_ultimo_contrato = comando.fecha_ultimo_contrato,
            fecha_expiracion_contrato_actual = comando.fecha_expiracion_contrato_actual,
            estado = comando.estado,
            id_compania = comando.id_compania,
            id_contrato = comando.id_contrato
        )
        propiedad : Propiedad = self._fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)
    
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioPropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.commit()

@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
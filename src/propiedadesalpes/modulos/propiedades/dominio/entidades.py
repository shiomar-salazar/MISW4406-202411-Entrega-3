from __future__ import annotations
from dataclasses import dataclass
from dataclasses import dataclass, field
import sqlalchemy
import uuid
import modulos.propiedades.dominio.objetos_valor as ov
from modulos.propiedades.dominio.eventos import PropiedadCreada
from seedwork.dominio.entidades import AgregacionRaiz, Entidad


from .eventos import PropiedadCreada

@dataclass
class Propiedad(AgregacionRaiz):
    id_propiedad: uuid.UUID = field(hash=True, default=uuid.uuid4())
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
    

    def crear_propiedad(self, propiedad: "Propiedad"):
        self.nombre_propiedad = propiedad.nombre_propiedad,
        self.tipo_propiedad = propiedad.tipo_propiedad,
        self.pais = propiedad.pais,
        self.departamento = propiedad.departamento,
        self.ciudad = propiedad.ciudad,
        self.direccion = propiedad.direccion,
        self.latitud = propiedad.latitud,
        self.longitud = propiedad.longitud,
        self.codigo_postal = propiedad.codigo_postal,
        self.area_lote = propiedad.area_lote,
        self.estrato_socioeconomico = propiedad.estrato_socioeconomico,
        self.valor_venta = propiedad.valor_venta,
        self.valor_arriendo_mensual = propiedad.valor_arriendo_mensual,
        self.moneda = propiedad.moneda,
        self.propietario = propiedad.propietario,
        self.arrendatario = propiedad.arrendatario,
        self.fecha_ultimo_contrato = propiedad.fecha_ultimo_contrato,
        self.fecha_expiracion_contrato_actual = propiedad.fecha_expiracion_contrato_actual,
        self.estado = propiedad.estado,
        self.id_compania = propiedad.id_compania,
        self.id_contrato = propiedad.id_contrato

        self.agregar_evento(PropiedadCreada(
            nombre_propiedad = str(self.nombre_propiedad),   
            tipo_propiedad = str(self.tipo_propiedad),
            pais = str(self.pais),
            departamento = str(self.departamento),
            ciudad = str(self.ciudad),
            direccion = str(self.direccion),   
            latitud  = str(self.latitud),
            longitud = str(self.longitud),
            codigo_postal = str(self.codigo_postal),
            area_lote = str(self.area_lote),
            estrato_socioeconomico = str(self.estrato_socioeconomico),
            valor_venta  = str(self.valor_venta),
            valor_arriendo_mensual  = str(self.valor_arriendo_mensual),
            moneda  = str(self.moneda),
            propietario  = str(self.propietario),
            arrendatario  = str(self.arrendatario),
            fecha_ultimo_contrato  = str(self.fecha_ultimo_contrato),
            fecha_expiracion_contrato_actual  = str(self.fecha_expiracion_contrato_actual),
            estado  = str(self.estado),
            id_compania  = str(self.id_compania),
            id_contrato  = str(self.id_contrato)
        )
    )


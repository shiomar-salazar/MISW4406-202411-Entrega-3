from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class PropiedadCreadaPayload(Record):
    id_propiedad = String()    
    nombre_propiedad = String()          
    tipo_propiedad = String()       
    pais = String()       
    departamento = String()       
    ciudad = String()       
    direccion = String()          
    latitud  = String()       
    longitud = String()       
    codigo_postal = String()       
    area_lote = String()       
    estrato_socioeconomico = String()       
    valor_venta  = String()       
    valor_arriendo_mensual  = String()       
    moneda  = String()       
    propietario  = String()       
    arrendatario  = String()       
    fecha_ultimo_contrato  = String()       
    fecha_expiracion_contrato_actual  = String()       
    estado  = String()       
    id_compania  = String()       
    id_contrato  = String()  


class EventoPropiedadCreada(EventoIntegracion):
    data = PropiedadCreadaPayload()
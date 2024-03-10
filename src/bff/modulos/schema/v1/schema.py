import graphene
import traceback
from modulos.aplicacion.errors.errors import ApiError

from modulos.aplicacion.command.consulta_propiedad_direccion import ConsultarDatos

def extract_propiedades(direccion):
    print('schema extract_propiedades')
    try:
        # Logica de negocio
        propiedad = ConsultarDatos(direccion).execute()   
        print(propiedad)          
        return propiedad
    except Exception as e:# pragma: no cover
        traceback.print_exc()
        raise ApiError(e)


class Propiedad(graphene.ObjectType):
    direccion = graphene.String(required=True) 
    id_propiedad = graphene.String()    
    nombre_propiedad = graphene.String() 
    tipo_propiedad = graphene.String()
    pais = graphene.String()
    departamento = graphene.String()
    ciudad = graphene.String() 
    latitud  = graphene.String()
    longitud = graphene.String()
    codigo_postal = graphene.String()
    area_lote = graphene.String()
    estrato_socioeconomico = graphene.String()
    valor_venta  = graphene.String()
    valor_arriendo_mensual  = graphene.String()
    moneda  = graphene.String()
    propietario  = graphene.String()
    arrendatario  = graphene.String()
    fecha_ultimo_contrato  = graphene.String()
    fecha_expiracion_contrato_actual  = graphene.String()
    estado  = graphene.String()
    id_compania  = graphene.String()
    id_contrato  = graphene.String()  


class Query(graphene.ObjectType):
    propiedad = graphene.Field(Propiedad, direccion=graphene.String())

    def resolve_propiedad(self, info, direccion):
        try:
            extracted = extract_propiedades(direccion)
            return Propiedad(direccion=direccion,
                        id_propiedad=extracted.id_propiedad,
                        nombre_propiedad=extracted.nombre_propiedad,
                        tipo_propiedad=extracted.tipo_propiedad,
                        pais=extracted.pais,
                        departamento=extracted.departamento,
                        ciudad=extracted.ciudad,
                        latitud=extracted.latitud,
                        longitud=extracted.longitud,
                        codigo_postal=extracted.codigo_postal,
                        area_lote=extracted.area_lote,
                        estrato_socioeconomico=extracted.estrato_socioeconomico,
                        valor_venta=extracted.valor_venta,
                        valor_arriendo_mensual=extracted.valor_arriendo_mensual,
                        moneda=extracted.moneda,
                        propietario=extracted.propietario,
                        arrendatario=extracted.arrendatario,
                        fecha_ultimo_contrato=extracted.fecha_ultimo_contrato,
                        fecha_expiracion_contrato_actual=extracted.fecha_expiracion_contrato_actual,
                        estado=extracted.estado,
                        id_compania=extracted.id_compania,
                        id_contrato=extracted.id_contrato,
            )
        except Exception as e: 
            print('error')
            print(e)
            return None

schema = graphene.Schema(query=Query)
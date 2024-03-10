import pprint
from modulos.schema.v1 import schema


def query_propiedades(propiedad):
    q = """
        {
        propiedad(direccion: "Calle") {
            id_propiedad
            nombre_propiedad
            tipo_propiedad
            pais
            departamento
            ciudad
            direccion
            latitud
            longitud
            codigo_postal
            area_lote
            estrato_socioeconomico
            valor_venta
            valor_arriendo_mensual
            moneda
            propietario
            arrendatario
            fecha_ultimo_contrato
            fecha_expiracion_contrato_actual
            estado
            id_compania
            id_contrato
        }
        }
    """
    result = schema.schema.schema.execute(q)
    if result.errors:
        if len(result.errors) == 1:
            raise Exception(result.errors[0])
        else:
            raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    results = query_propiedades("Calle")
    pprint.pprint(results)
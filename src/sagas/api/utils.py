import requests
from flask import request
import os
import json
  

def crear_compania(dto):
    url= f"{os.getenv('HOST_COMPANIAS')}/compania/crear"
    data = {
        "ciudad": dto.ciudad,
        "direccion": dto.direccion,
        "documento_identidad_numero_identificacion": dto.documento_identidad_numero_identificacion,
        "documento_identidad_tipo": dto.documento_identidad_tipo,
        "email_contacto": dto.email_contacto,
        "estado": dto.estado,
        "latitud": dto.latitud,
        "longitud": dto.longitud,
        "nombre_compania": dto.nombre_compania,
        "pais": dto.pais,
        "representante_legal": dto.representante_legal,
        "telefono_contacto": dto.telefono_contacto,
        "tipo_industria": dto.tipo_industria
    }
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(data), headers=headers)
    
    

def obtener_compania(direccion):
    url= f"{os.getenv('HOST_COMPANIAS')}/compania/direccion/{direccion}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['id_compania']
    else:
        return None     


def crear_propiedad(dto):
    url= f"{os.getenv('HOST_PROPIEDADES')}/propiedad/crear"
    data = {
        "nombre_propiedad": dto.nombre_propiedad,
        "tipo_propiedad": dto.tipo_propiedad,
        "pais": dto.pais,
        "departamento": dto.departamento,
        "ciudad": dto.ciudad,
        "direccion": dto.direccion,
        "latitud": dto.latitud,
        "longitud": dto.longitud,
        "codigo_postal": dto.codigo_postal,
        "area_lote": dto.area_lote,
        "estrato_socioeconomico": dto.estrato_socioeconomico,
        "valor_venta": dto.valor_venta,
        "valor_arriendo_mensual": dto.valor_arriendo_mensual,
        "moneda": dto.moneda,
        "propietario": dto.propietario,
        "arrendatario": dto.arrendatario,
        "fecha_ultimo_contrato": dto.fecha_ultimo_contrato,
        "fecha_expiracion_contrato_actual": dto.fecha_expiracion_contrato_actual,
        "estado": dto.estado
    }
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(data), headers=headers)
   

def obtener_propiedad(direccion):
    url= f"{os.getenv('HOST_PROPIEDADES')}/propiedad/direccion?direccion={direccion}"    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['id_propiedad']
    else:
        return False  


def crear_contrato(dto, id_compania, id_propiedad):
    url= f"{os.getenv('HOST_CONTRATOS')}/contrato/crear" 
    data = {
        "id_compania": id_compania,
        "id_propiedad": id_propiedad,
        "fecha_inicio": dto.fecha_inicio,
        "fecha_fin": dto.fecha_fin,
        "fecha_ejecucion": dto.fecha_ejecucion,
        "monto": dto.monto,
        "tipo": dto.tipo
    }
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(data), headers=headers)
    
    
    

def obtener_contrato(id_compania, id_propiedad):
    url= f"{os.getenv('HOST_CONTRATOS')}/contrato/{id_compania}/{id_propiedad}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None   


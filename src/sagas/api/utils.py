import requests
from flask import request
import os
import json
  

def crear_compania():
    url= f"{os.getenv('HOST_COMPANIAS')}/compania/crear"
    data = {
        "ciudad": "Bogota",
        "direccion": "calle 25",
        "documento_identidad_numero_identificacion": "10189832943",
        "documento_identidad_tipo": "NIT",
        "email_contacto": "pepito@gmail.com",
        "estado": "Registrado",
        "latitud": None,
        "longitud": None,
        "nombre_compania": "Starbuks 122",
        "pais": "Colombia",
        "representante_legal": "Pepit Peleaz",
        "telefono_contacto": "695587569",
        "tipo_industria": "Laboratorio"
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


def crear_propiedad():
    url= f"{os.getenv('HOST_PROPIEDADES')}/propiedad/crear"  
    data = {
        "nombre_propiedad": "Bodegas las Palmas",
        "tipo_propiedad": "Bodega",
        "pais": "Colombia",
        "departamento": "Cundinamarca",
        "ciudad": "Bogotá D.C",
        "direccion": "calle 25",
        "latitud": 123.456,
        "longitud": -78.910,
        "codigo_postal": "110110",
        "area_lote": 500,
        "estrato_socioeconomico": 3,
        "valor_venta": 740000000.00,
        "valor_arriendo_mensual": 5500000.00,
        "moneda": "COL",
        "propietario": "Carlos Enrique Morales",
        "arrendatario": "Nestor Guillermo Salcedo",
        "fecha_ultimo_contrato": "2024-02-20",
        "fecha_expiracion_contrato_actual": "2025-02-20",
        "estado": "Activo"
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


def crear_contrato(id_compania, id_propiedad):
    url= f"{os.getenv('HOST_CONTRATOS')}/contrato/crear" 
    data = {
        "id_compania": id_compania,
        "id_propiedad": id_propiedad,
        "fecha_inicio": "2024-02-29",
        "fecha_fin": "2028-02-29",
        "fecha_ejecucion": "2024-02-20",
        "monto": 12500,
        "tipo": "Arrendamiento"
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


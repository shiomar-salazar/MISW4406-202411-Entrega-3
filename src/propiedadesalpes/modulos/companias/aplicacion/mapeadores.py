import json
from propiedadesalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from propiedadesalpes.seedwork.dominio.objetos_valor import Compania_ov
from .dto import CompaniaDTO, DocumentoIdentidadDTO, TipoIndustriaDTO, LocalizacionDTO, InformacionGeoespacialDTO, DireccionDTO, DatosGreograficosDTO
from datetime import datetime
import uuid


class MapeadorCompaniaDTOJson(AppMap):

    def externo_a_dto(self, externo: dict) -> CompaniaDTO:

        documento_identidad_dto = DocumentoIdentidadDTO()
        documento_identidad_dto.tipo = externo.get("documento_identidad_tipo")
        documento_identidad_dto.numero_identificacion = externo.get("documento_identidad_numero_identificacion")

        tipo_industria_dto = TipoIndustriaDTO()
        tipo_industria_dto.nombre = externo.get("tipo_industria")

        info_geoespacila_dto = InformacionGeoespacialDTO()
        info_geoespacila_dto.latitud = externo.get("latitud")
        info_geoespacila_dto.longitud = externo.get("longitud")

        datos_geograficos_dto = DatosGreograficosDTO()
        datos_geograficos_dto.ciudad = externo.get("ciudad")
        datos_geograficos_dto.pais = externo.get("pais")

        direccion_dto = DireccionDTO()
        direccion_dto.direccion = externo.get("direccion")
        direccion_dto.datos_geograficos = datos_geograficos_dto

        localizacion_dto = LocalizacionDTO()
        localizacion_dto.infromacion_geoespacial = info_geoespacila_dto
        localizacion_dto.direccion = direccion_dto

        compania_dto = CompaniaDTO()
        compania_dto.id = str(uuid.uuid4())
        compania_dto.nombre_compania = externo.get("nombre_compania")
        compania_dto.representante_legal = externo.get("representante_legal")
        compania_dto.email_contacto = externo.get("email_contacto")
        compania_dto.telefono_contacto = externo.get("telefono_contacto")
        compania_dto.estado = externo.get("estado")
        compania_dto.documento_identidad = documento_identidad_dto
        compania_dto.tipo_industria = tipo_industria_dto
        compania_dto.localizacion = localizacion_dto

        return compania_dto

    def dto_a_externo(self, dto: CompaniaDTO) -> dict:
        return  [compania.__dict__ for compania in dto]


class MapeadorCompania(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'        

    def entidad_a_dto(self, entidad: Compania_ov) -> CompaniaDTO:
        compania_dto = CompaniaDTO()
        compania_dto.id = entidad.id_comp
        compania_dto.nombre_compania = entidad.nombre_compania
        compania_dto.representante_legal = entidad.representante_legal
        compania_dto.email_contacto = entidad.email_contacto
        compania_dto.telefono_contacto = entidad.telefono_contacto
        compania_dto.estado = entidad.estado
        
        # DocumentoIdentidad
        # if entidad.documento_identidad:
        #     compania_dto.documento_identidad.tipo = entidad.documento_identidad_tipo
        #     compania_dto.documento_identidad.numero_identificacion = entidad.documento_identidad_numero_identificacion
        # TipoIndustria
        # if entidad.tipo_industria:
        #     compania_dto.tipo_industria = entidad.tipo_industria.nombre
        
        return compania_dto

    # Función para convertir de DTO a Entidad
    def dto_a_entidad(self, companiasDto: list) -> Compania:
        print('<================ Aplicacion.MapeadorCompania.dto_a_entidad ================>')
        companias_entidad = []
        print(companiasDto)
        for  companiaDto in companiasDto:
            compania = Compania()
            companias_entidad.append(compania.crear_compania(companiaDto) )
        print(companias_entidad)
        print('<================ Aplicacion.MapeadorCompania.dto_a_entidad ================>')
        return companias_entidad

    def obtener_tipo(self) -> type:
        return Compania.__class__
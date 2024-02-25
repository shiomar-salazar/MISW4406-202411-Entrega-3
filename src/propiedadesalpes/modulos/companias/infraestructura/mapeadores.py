""" Mapeadores para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from .dto import Compania as CompaniaDTO, DocumentoIdentidad, TipoIndustria

class MapeadorCompania(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    # Función para convertir una lista de DTO a Entidad
    def _procesar_compania_dto(self, companias_dto: list) -> list[Compania]:
        companias = []
        for dto in companias_dto:
            entidad = Compania()
            entidad.id = dto.id
            entidad.nombre_compania = dto.nombre_compania
            entidad.representante_legal = dto.representante_legal
            entidad.email_contacto = dto.email_contacto
            entidad.telefono_contacto = dto.telefono_contacto
            entidad.estado = dto.estado

            # DocumentoIdentidad
            if dto.documento_identidad:
                entidad.documento_identidad_tipo = dto.documento_identidad.tipo_documento
                entidad.documento_identidad_numero_identificacion = dto.documento_identidad.numero_documento

            # TipoIndustria
            if dto.tipo_industria:
                entidad.tipo_industria = dto.tipo_industria.nombre

            companias.append(entidad)

        return companias

    # Función para obtener la clase
    def obtener_tipo(self) -> type:
        return Compania.__class__

    # Función para convertir de Entidad a DTO
    def entidad_a_dto(entidad: Compania) -> Compania:
        compania_dto = Compania()
        compania_dto.id = entidad.id
        compania_dto.nombre_compania = entidad.nombre_compania
        compania_dto.representante_legal = entidad.representante_legal
        compania_dto.email_contacto = entidad.email_contacto
        compania_dto.telefono_contacto = entidad.telefono_contacto
        compania_dto.estado = entidad.estado

        # DocumentoIdentidad
        if entidad.documento_identidad_tipo and entidad.documento_identidad_numero_identificacion:
            compania_dto.documento_identidad = DocumentoIdentidad(
                tipo_documento=entidad.documento_identidad_tipo,
                numero_documento=entidad.documento_identidad_numero_identificacion
            )

        # TipoIndustria
        if entidad.tipo_industria:
            compania_dto.tipo_industria = TipoIndustria(nombre=entidad.tipo_industria, descripcion="")

        return compania_dto

    # Función para convertir de DTO a Entidad
    def dto_a_entidad(self, dto: CompaniaDTO) -> Compania:
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        print(dto.to_dict())
        print('+++++++++++++++++++++++++++++++++++++++++++++')
        compania = Compania()
        compania.id = dto.id
        compania.nombre_compania = dto.nombre_compania
        compania.representante_legal = dto.representante_legal
        compania.email_contacto = dto.email_contacto
        compania.telefono_contacto = dto.telefono_contacto
        compania.estado = dto.estado

        # DocumentoIdentidad
        if dto.documento_identidad:
            compania.documento_identidad_tipo = dto.documento_identidad.tipo_documento
            compania.documento_identidad_numero_identificacion = dto.documento_identidad.numero_documento

        # TipoIndustria
        if dto.tipo_industria:
            compania.tipo_industria = dto.tipo_industria.nombre

        return compania
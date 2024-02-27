from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.dto import DTO


class InformacionGeoespacialDTO(DTO):
    latitud: str
    longitud: str


class DatosGreograficosDTO(DTO):
    ciudad: str
    pais: str


class DireccionDTO(DTO):
    direccion: str
    datos_geograficos: DatosGreograficosDTO


class LocalizacionDTO(DTO):
    direccion: DireccionDTO
    infromacion_geoespacial: InformacionGeoespacialDTO


class TipoIndustriaDTO(DTO):
    id_industria: str
    nombre: str
    descripcion: str


class DocumentoIdentidadDTO(DTO):
    tipo: str
    numero_identificacion: str

class CompaniaDTO(DTO):
    id: str
    nombre_compania: str
    representante_legal: str
    email_contacto: str
    telefono_contacto: str
    estado: str
    # documento_identidad: DocumentoIdentidadDTO
    # tipo_industria: TipoIndustriaDTO
    # localizacion: LocalizacionDTO

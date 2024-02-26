""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de Companias

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de Companias

"""
from sqlalchemy.orm import joinedload
from propiedadesalpes.config.db import db
from propiedadesalpes.modulos.companias.dominio.repositorios import RepositorioCompanias
from propiedadesalpes.modulos.companias.dominio.entidades import Compania
from propiedadesalpes.modulos.companias.dominio.fabricas import FabricaCompanias
from .dto import Compania as CompaniaDTO, DocumentoIdentidad, TipoIndustria
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioCompaniasPostgresql(RepositorioCompanias):

    def __init__(self):
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        print('<================ RepositorioCompaniasPostgresql.obtener_por_id ================>')
        compania_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(CompaniaDTO.id == id).join(DocumentoIdentidad, CompaniaDTO.documento_identidad).join(TipoIndustria, CompaniaDTO.tipo_industria).options(joinedload(CompaniaDTO.documento_identidad), joinedload(CompaniaDTO.tipo_industria)).first()
        print(compania_dto)
        print('<================ RepositorioCompaniasPostgresql.obtener_por_id ================>')
        return compania_dto

    def obtener_registradas(self) -> Compania:
        print('<================ RepositorioCompaniasPostgresql.obtener_registradas ================>')
        companias_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(CompaniaDTO.estado == 'Registrado').join(DocumentoIdentidad, CompaniaDTO.documento_identidad).join(TipoIndustria, CompaniaDTO.tipo_industria).options(joinedload(CompaniaDTO.documento_identidad), joinedload(CompaniaDTO.tipo_industria)).all()
        print(companias_dto)
        print('<================ RepositorioCompaniasPostgresql.obtener_registradas ================>')
        return companias_dto

    def obtener_procesadas(self) -> Compania:
        print('<================ RepositorioCompaniasPostgresql.obtener_procesadas ================>')
        companias_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(CompaniaDTO.estado == 'Procesado').join(DocumentoIdentidad, CompaniaDTO.documento_identidad).join(TipoIndustria, CompaniaDTO.tipo_industria).options(joinedload(CompaniaDTO.documento_identidad), joinedload(CompaniaDTO.tipo_industria)).all()
        print(companias_dto)
        print('<================ RepositorioCompaniasPostgresql.obtener_procesadas ================>')
        return companias_dto

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: CompaniaDTO):
        compania_dto = self.fabrica_companias.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)

    def actualizar(self, compania: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        # TODO
        raise NotImplementedError
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

class RepositorioCompaniasSQLite(RepositorioCompanias):

    def __init__(self):
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(Compania.id == id).join(DocumentoIdentidad, Compania.documento_identidad).join(TipoIndustria, Compania.tipo_industria).options(joinedload(Compania.documento_identidad), joinedload(Compania.tipo_industria)).first()
        print('==========================================')
        print(compania_dto.to_dict())
        print('==========================================')
        return self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())

    def obtener_registradas(self) -> Compania:
        companias_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(Compania.estado == 'Registrado').join(DocumentoIdentidad, Compania.documento_identidad).join(TipoIndustria, Compania.tipo_industria).options(joinedload(Compania.documento_identidad), joinedload(Compania.tipo_industria)).all()
        return [MapeadorCompania._procesar_compania_dto(self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())) for compania_dto in companias_dto]

    def obtener_procesadas(self) -> Compania:
        companias_dto = db.session.query(CompaniaDTO, DocumentoIdentidad, TipoIndustria).filter(Compania.estado == 'Procesado').join(DocumentoIdentidad, Compania.documento_identidad).join(TipoIndustria, Compania.tipo_industria).options(joinedload(Compania.documento_identidad), joinedload(Compania.tipo_industria)).all()
        return [MapeadorCompania._procesar_compania_dto(self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())) for compania_dto in companias_dto]

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
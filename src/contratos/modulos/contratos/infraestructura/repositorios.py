from config.db import db
from modulos.contratos.dominio.repositorios import RepositorioContratos
from modulos.contratos.infraestructura.dto import Contrato
from modulos.contratos.dominio.fabricas import FabricaContratos
from .dto import Contrato as ContratoDTO
from .mapeadores import MappeadorContrato
from uuid import UUID

class RepositorioContratosPostgresSQL(RepositorioContratos):
    def __init__(self):
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    def agregar(self, contrato: Contrato):
            contrato_dto = self._fabrica_contratos.crear_objeto(contrato, MappeadorContrato())
            db.session.add(contrato_dto)
    
    def obtener_todos(self) -> list[Contrato]:
        contratos_list = db.session.query(Contrato).all()
        return contratos_list
    
    def obtener_tipo(self) -> type:
        return Contrato.__class__
    
    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        return self._fabrica_contratos.crear_objeto(contrato_dto, MappeadorContrato())

    def obtener_por_ids(self, id_compania: UUID, id_propiedad: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id_compania=str(id_compania), id_propiedad=str(id_propiedad)).first()
        return self._fabrica_contratos.crear_objeto(contrato_dto, MappeadorContrato())
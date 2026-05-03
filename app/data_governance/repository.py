from typing import List, Optional
from app.data_governance.models import (
    DataContract, DataSchema, DatasetQualityReport, TrustVerdict,
    GovernanceCatalogEntry, DatasetRef
)
from app.data_governance.storage import GovernanceStorage
from app.data_governance.catalog import GovernanceCatalog
from app.data_governance.schemas import SchemaRegistry
from app.data_governance.contracts import DataContractRegistry

class GovernanceRepository:
    def __init__(self, storage: GovernanceStorage):
        self.storage = storage
        self.catalog = GovernanceCatalog()
        self.schema_registry = SchemaRegistry()
        self.contract_registry = DataContractRegistry()
        self._load_all()

    def _load_all(self):
        # Load contracts
        for c_dict in self.storage.list_contracts():
             try:
                 contract = DataContract(**c_dict)
                 self.contract_registry.register_contract(contract)
             except Exception:
                 pass

    def save_contract(self, contract: DataContract):
        self.contract_registry.register_contract(contract)
        self.storage.save_contract(contract.contract_id, contract.model_dump())

    def get_contract(self, contract_id: str) -> DataContract:
        return self.contract_registry.get_contract(contract_id)

    def list_contracts(self) -> List[DataContract]:
        return self.contract_registry.list_contracts()

    def save_schema(self, schema: DataSchema):
        self.schema_registry.register_schema(schema)
        self.storage.save_schema(schema.schema_id, schema.version, schema.model_dump())

    def get_schema(self, schema_id: str, version: str) -> DataSchema:
        from app.data_governance.models import SchemaVersionRef
        return self.schema_registry.get_schema(SchemaVersionRef(schema_id=schema_id, version=version))

    def list_schemas(self) -> List[DataSchema]:
        return self.schema_registry.list_schemas()

    def save_trust_verdict(self, verdict: TrustVerdict):
         self.storage.save_trust_verdict(
              verdict.dataset_ref.dataset_id,
              verdict.dataset_ref.version,
              verdict.model_dump()
         )
         # Update catalog
         entry = GovernanceCatalogEntry(
              dataset_ref=verdict.dataset_ref,
              contract_id="unknown", # normally fetched via lineage/metadata
              latest_quality_status=verdict.verdict,
              latest_trust_verdict=verdict.verdict,
              last_updated=verdict.dataset_ref.__class__.model_fields.get("version", None) # dummy
         )
         from datetime import datetime, timezone
         entry.last_updated = datetime.now(timezone.utc)
         self.catalog.update_entry(entry)

    def get_trust_verdict(self, ref: DatasetRef) -> Optional[TrustVerdict]:
         data = self.storage.get_trust_verdict(ref.dataset_id, ref.version)
         if data:
             return TrustVerdict(**data)
         return None

    def save_quality_report(self, report: DatasetQualityReport):
         self.storage.save_quality_report(report.run_id, report.model_dump())

    def list_catalog_entries(self) -> List[GovernanceCatalogEntry]:
         return self.catalog.list_entries()

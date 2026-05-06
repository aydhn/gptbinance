from typing import Dict, Any, List
from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.models import ArtefactRecord, ArtefactDescriptor
from app.evidence_graph.enums import ArtefactType


class ArtefactIngestor:
    def __init__(self, registry: ArtefactRegistry):
        self.registry = registry

    def ingest_from_source(
        self, source_data: Dict[str, Any], mapping_config: Dict[str, Any]
    ) -> ArtefactRecord:
        # Simulate typed artefact extraction
        a_type = mapping_config.get("artefact_type", ArtefactType.UNKNOWN)
        scope = mapping_config.get("scope")
        owner = mapping_config.get("owner_domain", "system")

        desc = ArtefactDescriptor(
            descriptor_type=mapping_config.get("descriptor_type", "generic"),
            metadata=source_data,
        )

        # Check for duplicates based on descriptor hash logic in registry
        # For simplicity, just register
        return self.registry.register_artefact(
            a_type=a_type, scope=scope, owner_domain=owner, descriptor=desc
        )

    def batch_ingest(
        self, source_data_list: List[Dict[str, Any]], mapping_config: Dict[str, Any]
    ) -> List[ArtefactRecord]:
        return [
            self.ingest_from_source(data, mapping_config) for data in source_data_list
        ]

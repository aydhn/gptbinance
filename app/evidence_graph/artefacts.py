from typing import Dict, List, Optional
from datetime import datetime
import uuid
import hashlib
import json

from app.evidence_graph.models import (
    ArtefactRecord,
    ArtefactScope,
    ArtefactLineage,
    ArtefactDescriptor,
)
from app.evidence_graph.enums import ArtefactType
from app.evidence_graph.exceptions import InvalidArtefactRecordError


class ArtefactRegistry:
    def __init__(self):
        self._artefacts: Dict[str, ArtefactRecord] = {}

    def _generate_immutable_hash(self, descriptor: ArtefactDescriptor) -> str:
        # Simplified hash generation for immutability
        desc_str = json.dumps(descriptor.__dict__, sort_keys=True)
        return hashlib.sha256(desc_str.encode("utf-8")).hexdigest()

    def register_artefact(
        self,
        a_type: ArtefactType,
        scope: ArtefactScope,
        owner_domain: str,
        descriptor: ArtefactDescriptor,
        lineage: Optional[ArtefactLineage] = None,
    ) -> ArtefactRecord:
        if not lineage:
            lineage = ArtefactLineage()

        record = ArtefactRecord(
            id=f"ART-{uuid.uuid4().hex[:8]}",
            type=a_type,
            scope=scope,
            created_at=datetime.now(),
            immutable_ref=self._generate_immutable_hash(descriptor),
            owner_domain=owner_domain,
            lineage=lineage,
            descriptor=descriptor,
            freshness_timestamp=datetime.now(),
        )
        self._artefacts[record.id] = record
        return record

    def get_artefact(self, artefact_id: str) -> Optional[ArtefactRecord]:
        return self._artefacts.get(artefact_id)

    def list_artefacts(self) -> List[ArtefactRecord]:
        return list(self._artefacts.values())

    def mark_superseded(self, artefact_id: str):
        if artefact_id in self._artefacts:
            self._artefacts[artefact_id].is_superseded = True
        else:
            raise InvalidArtefactRecordError(f"Artefact {artefact_id} not found")

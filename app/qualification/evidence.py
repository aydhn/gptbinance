from typing import List
from app.qualification.models import QualificationEvidenceRef
from app.qualification.enums import EvidenceStatus


class EvidenceCollector:
    def collect_refs(self, section: str) -> List[QualificationEvidenceRef]:
        # Mocking collection based on section name
        return [
            QualificationEvidenceRef(
                evidence_id=f"ev-{section}-1",
                source=section,
                status=EvidenceStatus.COMPLETE,
                artifact_uri=f"file:///var/logs/{section}.log",
            )
        ]

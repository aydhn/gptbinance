from typing import List, Dict
from datetime import datetime

from app.evidence_graph.models import ArtefactRecord, RedactionRecord
from app.evidence_graph.enums import RedactionClass


class RedactionEngine:
    def __init__(self, redaction_policies: Dict[str, RedactionClass]):
        self.policies = redaction_policies

    def apply_redaction(
        self, artefacts: List[ArtefactRecord], user_role: str
    ) -> tuple[List[ArtefactRecord], List[RedactionRecord]]:
        redacted_artefacts = []
        notes = []

        for a in artefacts:
            if a.owner_domain in self.policies and user_role != "admin":
                # Redact
                notes.append(
                    RedactionRecord(
                        artefact_id=a.id,
                        redaction_class=self.policies[a.owner_domain],
                        reason="Domain restricted",
                        redacted_at=datetime.now(),
                    )
                )
            else:
                redacted_artefacts.append(a)

        return redacted_artefacts, notes

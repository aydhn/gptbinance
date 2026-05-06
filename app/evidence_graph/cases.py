from datetime import datetime
import uuid

from app.evidence_graph.models import EvidenceCaseFile, EvidenceCaseSection, ArtefactRef
from app.evidence_graph.enums import CaseFileClass, CompletenessClass
from app.evidence_graph.artefacts import ArtefactRegistry
from app.evidence_graph.lineage import LineageEngine


class CaseFileAssembler:
    def __init__(
        self, artefact_registry: ArtefactRegistry, lineage_engine: LineageEngine
    ):
        self.artefact_registry = artefact_registry
        self.lineage_engine = lineage_engine

    def assemble(
        self, case_class: CaseFileClass, anchor_artefact_id: str
    ) -> EvidenceCaseFile:
        anchor = self.artefact_registry.get_artefact(anchor_artefact_id)
        if not anchor:
            raise ValueError(f"Anchor artefact {anchor_artefact_id} not found")

        # Get full lineage (backward to find origins, forward to find impacts)
        backward = self.lineage_engine.traverse(
            anchor_artefact_id, direction="BACKWARD"
        )  # simplified

        sections = [
            EvidenceCaseSection(
                title="Executive Summary",
                content=f"Case file for {case_class.name} anchored at {anchor_artefact_id}",
                artefact_refs=[
                    ArtefactRef(
                        artefact_id=anchor.id, immutable_hash=anchor.immutable_ref
                    )
                ],
            ),
            EvidenceCaseSection(
                title="Chronology & Lineage",
                content=f"Found {len(backward.visited_artefacts)} related artefacts in history.",
                artefact_refs=[
                    ArtefactRef(artefact_id=a.id, immutable_hash=a.immutable_ref)
                    for a in backward.visited_artefacts
                ],
            ),
        ]

        accepted_evidence = [
            ArtefactRef(artefact_id=a.id, immutable_hash=a.immutable_ref)
            for a in backward.visited_artefacts
        ]

        return EvidenceCaseFile(
            case_id=f"CASE-{uuid.uuid4().hex[:8]}",
            case_class=case_class,
            created_at=datetime.now(),
            executive_summary=f"Auto-assembled {case_class.name}",
            sections=sections,
            accepted_evidence=accepted_evidence,
            rejected_evidence=[],
            completeness=CompletenessClass.COMPLETE,
        )

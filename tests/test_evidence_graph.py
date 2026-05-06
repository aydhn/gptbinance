import pytest
from datetime import datetime

from app.evidence_graph.models import (
    EvidenceGraphConfig,
    ArtefactScope,
    ArtefactDescriptor,
    ArtefactLineage,
)
from app.evidence_graph.enums import (
    ArtefactType,
    ScopeClass,
    RelationType,
    TraversalClass,
    CaseFileClass,
    CompletenessClass,
)
from app.evidence_graph.repository import EvidenceGraphRepository


def test_artefact_registry():
    repo = EvidenceGraphRepository(EvidenceGraphConfig())
    scope = ArtefactScope(scope_class=ScopeClass.GLOBAL)
    desc = ArtefactDescriptor(descriptor_type="test", metadata={"test": True})

    art = repo.artefact_registry.register_artefact(
        a_type=ArtefactType.POLICY_DECISION,
        scope=scope,
        owner_domain="policy",
        descriptor=desc,
    )

    assert art.id.startswith("ART-")
    assert repo.artefact_registry.get_artefact(art.id) == art


def test_relation_registry():
    repo = EvidenceGraphRepository(EvidenceGraphConfig())
    scope = ArtefactScope(scope_class=ScopeClass.GLOBAL)
    desc = ArtefactDescriptor(descriptor_type="test", metadata={"test": True})

    art1 = repo.artefact_registry.register_artefact(
        ArtefactType.POLICY_DECISION, scope, "policy", desc
    )
    art2 = repo.artefact_registry.register_artefact(
        ArtefactType.READINESS_MEMO, scope, "readiness", desc
    )

    rel = repo.relation_registry.add_relation(
        source_id=art2.id,
        source_type=art2.type,
        target_id=art1.id,
        target_type=art1.type,
        relation_type=RelationType.DERIVED_FROM,
    )

    assert rel.edge_id.startswith("REL-")
    assert len(repo.relation_registry.get_relations_for_source(art2.id)) == 1


def test_lineage_traversal():
    repo = EvidenceGraphRepository(EvidenceGraphConfig())
    scope = ArtefactScope(scope_class=ScopeClass.GLOBAL)
    desc = ArtefactDescriptor(descriptor_type="test", metadata={})

    a1 = repo.artefact_registry.register_artefact(
        ArtefactType.INCIDENT_SNAPSHOT, scope, "incident", desc
    )
    a2 = repo.artefact_registry.register_artefact(
        ArtefactType.POSTMORTEM_REPORT, scope, "postmortem", desc
    )

    repo.relation_registry.add_relation(
        a2.id, a2.type, a1.id, a1.type, RelationType.FOLLOWS_INCIDENT
    )

    # Traverse backward from postmortem should find incident
    res = repo.lineage_engine.traverse(a2.id, direction=TraversalClass.BACKWARD)
    assert len(res.visited_artefacts) == 2  # Includes self and target
    assert a1.id in [a.id for a in res.visited_artefacts]


def test_case_file_assembly():
    repo = EvidenceGraphRepository(EvidenceGraphConfig())
    scope = ArtefactScope(scope_class=ScopeClass.GLOBAL)
    desc = ArtefactDescriptor(descriptor_type="test", metadata={})

    a1 = repo.artefact_registry.register_artefact(
        ArtefactType.INCIDENT_SNAPSHOT, scope, "incident", desc
    )

    case = repo.case_assembler.assemble(CaseFileClass.INCIDENT_CASE, a1.id)
    assert case.case_id.startswith("CASE-")
    assert case.completeness == CompletenessClass.COMPLETE
    assert len(case.sections) > 0


def test_gap_detection():
    repo = EvidenceGraphRepository(EvidenceGraphConfig())

    # Add relation without valid artefacts
    repo.relation_registry._relations["BAD_EDGE"] = type(
        "MockEdge",
        (),
        {
            "edge_id": "BAD_EDGE",
            "source_id": "missing",
            "target_id": "missing",
            "relation_type": RelationType.CITES,
            "created_at": datetime.now(),
            "metadata": {},
        },
    )()

    gaps = repo.gap_detector.find_gaps()
    assert len(gaps) == 1

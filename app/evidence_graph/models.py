from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

from app.evidence_graph.enums import (
    ArtefactType,
    RelationType,
    QueryClass,
    TraversalClass,
    CaseFileClass,
    CompletenessClass,
    RedactionClass,
    GraphGapSeverity,
    ScopeClass,
    )


@dataclass
class EvidenceGraphConfig:
    storage_path: str = "data/evidence_graph"
    enforce_strict_types: bool = True
    enable_auto_snapshot: bool = True


@dataclass
class ArtefactScope:
    scope_class: ScopeClass
    workspace: Optional[str] = None
    profile: Optional[str] = None
    symbol: Optional[str] = None
    session_id: Optional[str] = None


@dataclass
class ArtefactDescriptor:
    descriptor_type: str
    metadata: Dict[str, Any]


@dataclass
class ArtefactRef:
    artefact_id: str
    immutable_hash: str


@dataclass
class ArtefactLineage:
    root_id: Optional[str] = None
    parent_ids: List[str] = field(default_factory=list)


@dataclass
class ArtefactRecord:
    id: str
    type: ArtefactType
    scope: ArtefactScope
    created_at: datetime
    immutable_ref: str
    owner_domain: str
    lineage: ArtefactLineage
    descriptor: ArtefactDescriptor
    freshness_timestamp: datetime
    is_superseded: bool = False


@dataclass
class RelationEdge:
    edge_id: str
    source_id: str
    target_id: str
    relation_type: RelationType
    created_at: datetime
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class RelationPath:
    edges: List[RelationEdge]


@dataclass
class EvidenceCaseSection:
    title: str
    content: str
    artefact_refs: List[ArtefactRef] = field(default_factory=list)


@dataclass
class RedactionRecord:
    artefact_id: str
    redaction_class: RedactionClass
    reason: str
    redacted_at: datetime


@dataclass
class EvidenceCaseFile:
    case_id: str
    case_class: CaseFileClass
    created_at: datetime
    executive_summary: str
    sections: List[EvidenceCaseSection]
    accepted_evidence: List[ArtefactRef]
    rejected_evidence: List[ArtefactRef]
    completeness: CompletenessClass
    redaction_notes: List[RedactionRecord] = field(default_factory=list)


@dataclass
class EvidencePack:
    pack_id: str
    pack_type: str
    created_at: datetime
    artefacts: List[ArtefactRecord]
    relations: List[RelationEdge]
    completeness: CompletenessClass


@dataclass
class QueryRequest:
    query_class: QueryClass
    filters: Dict[str, Any]
    target_scope: ArtefactScope
    include_redacted: bool = False


@dataclass
class QueryResult:
    artefacts: List[ArtefactRecord]
    relations: List[RelationEdge]
    completeness: CompletenessClass
    redaction_notes: List[RedactionRecord] = field(default_factory=list)


@dataclass
class LineageTraversal:
    start_id: str
    direction: TraversalClass
    visited_artefacts: List[ArtefactRecord]
    edges: List[RelationEdge]
    completeness: CompletenessClass


@dataclass
class DependencyTraversal:
    start_id: str
    dependents: List[ArtefactRecord]
    invalidated_by: List[ArtefactRecord]
    fanout_count: int


@dataclass
class GraphGapFinding:
    gap_id: str
    severity: GraphGapSeverity
    description: str
    affected_artefacts: List[str]
    suggested_action: str


@dataclass
class EvidenceGraphAuditRecord:
    audit_id: str
    timestamp: datetime
    action: str
    actor: str
    details: Dict[str, Any]


@dataclass
class EvidenceGraphArtifactManifest:
    manifest_id: str
    timestamp: datetime
    records: List[str]
    edges: List[str]
    checksum: str

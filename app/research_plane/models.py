import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from app.research_plane.enums import (
    ResearchClass,
    QuestionClass,
    EvidenceClass,
    ContradictionClass,
    ConfidenceClass,
    ReadinessClass,
    InvalidationClass,
    OverlapSeverity,
    EquivalenceVerdict,
    TrustVerdict,
)


class ResearchPlaneConfig(BaseModel):
    storage_path: str = "data/research_registry"
    strict_falsifiability: bool = True
    require_contradiction_analysis: bool = True


class ResearchRef(BaseModel):
    item_id: str
    description: str


class ResearchScope(BaseModel):
    symbols: Optional[List[str]] = None
    sleeves: Optional[List[str]] = None
    regimes: Optional[List[str]] = None
    sessions: Optional[List[str]] = None
    products: Optional[List[str]] = None
    profiles: Optional[List[str]] = None
    explicit_narrowing: Optional[str] = None


class ResearchQuestion(BaseModel):
    question_id: str
    text: str
    question_class: QuestionClass
    independent_variables: List[str]
    dependent_variables: List[str]
    falsifiable: bool = False
    scope: ResearchScope
    lineage_refs: List[ResearchRef] = Field(default_factory=list)


class ResearchObservation(BaseModel):
    observation_id: str
    source: str  # replay, runtime, postmortem, anomaly
    text: str
    confidence_score: float
    freshness: datetime.datetime
    lineage_refs: List[ResearchRef] = Field(default_factory=list)


class ResearchHypothesis(BaseModel):
    hypothesis_id: str
    question_ref: str
    claimed_effect: str
    expected_mechanism: str
    expected_favorable_regimes: List[str]
    expected_invalidation_triggers: List[str]
    benchmark_expectation: str
    dependency_assumptions: List[str]
    proof_notes: Optional[str] = None


class EvidenceBundleEntry(BaseModel):
    entry_id: str
    evidence_class: EvidenceClass
    description: str
    source_ref: str
    freshness: datetime.datetime
    quality_notes: Optional[str] = None


class EvidenceBundle(BaseModel):
    bundle_id: str
    hypothesis_ref: str
    entries: List[EvidenceBundleEntry] = Field(default_factory=list)


class ContradictionRecord(BaseModel):
    contradiction_id: str
    hypothesis_ref: str
    contradiction_class: ContradictionClass
    description: str
    unresolved_burden: bool = True
    lineage_refs: List[ResearchRef] = Field(default_factory=list)


class ConfidenceAssessment(BaseModel):
    hypothesis_ref: str
    current_class: ConfidenceClass
    previous_class: Optional[ConfidenceClass] = None
    transition_reason: str
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchReadinessRecord(BaseModel):
    hypothesis_ref: str
    readiness_class: ReadinessClass
    blockers: List[str] = Field(default_factory=list)
    proof_notes: Optional[str] = None


class ResearchInvalidationRecord(BaseModel):
    hypothesis_ref: str
    invalidation_class: InvalidationClass
    reason: str
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchOverlapReport(BaseModel):
    report_id: str
    primary_hypothesis_ref: str
    overlapping_hypothesis_refs: List[str]
    severity: OverlapSeverity
    description: str
    proof_notes: Optional[str] = None


class ResearchMaturationReport(BaseModel):
    hypothesis_ref: str
    evidence_growth: int
    contradiction_resolution_trend: int
    stagnation_detected: bool
    maturation_to_candidate: bool
    dead_end: bool
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchEquivalenceReport(BaseModel):
    report_id: str
    hypothesis_ref: str
    verdict: EquivalenceVerdict
    divergence_sources: List[str] = Field(default_factory=list)
    proof_notes: Optional[str] = None


class ResearchTrustVerdict(BaseModel):
    hypothesis_ref: str
    verdict: TrustVerdict
    factors: Dict[str, str] = Field(default_factory=dict)
    caveats: List[str] = Field(default_factory=list)
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchItem(BaseModel):
    research_id: str
    title: str
    research_class: ResearchClass
    question: Optional[ResearchQuestion] = None
    observations: List[ResearchObservation] = Field(default_factory=list)
    hypotheses: List[ResearchHypothesis] = Field(default_factory=list)
    evidence_bundles: List[EvidenceBundle] = Field(default_factory=list)
    contradictions: List[ContradictionRecord] = Field(default_factory=list)
    confidence: Optional[ConfidenceAssessment] = None
    readiness: Optional[ResearchReadinessRecord] = None
    invalidation: Optional[ResearchInvalidationRecord] = None
    created_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
    updated_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchAuditRecord(BaseModel):
    audit_id: str
    research_id: str
    action: str
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )


class ResearchArtifactManifest(BaseModel):
    manifest_id: str
    research_id: str
    question_refs: List[str]
    observation_refs: List[str]
    hypothesis_refs: List[str]
    evidence_refs: List[str]
    contradiction_refs: List[str]
    confidence_class: ConfidenceClass
    trust_verdict: TrustVerdict
    timestamp: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )

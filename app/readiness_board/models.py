from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

from app.readiness_board.enums import (
    CandidateClass,
    EvidenceClass,
    AdmissibilityVerdict,
    ReadinessDomain,
    BoardVerdict,
    ContradictionClass,
    ConditionalScope,
    PromotionStage,
    MemoClass,
    DomainVerdict,
)


class ReadinessBoardConfig(BaseModel):
    stale_evidence_threshold_seconds: int = 86400
    require_freeze_for_review: bool = True


class CandidateScope(BaseModel):
    symbols: Optional[List[str]] = None
    profiles: Optional[List[str]] = None


class CandidateRecord(BaseModel):
    candidate_id: str
    candidate_class: CandidateClass
    scope: CandidateScope
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    lineage_refs: List[str] = Field(default_factory=list)


class CandidateFreezeSnapshot(BaseModel):
    snapshot_id: str
    candidate_id: str
    frozen_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    artifacts: Dict[str, str] = Field(default_factory=dict)
    is_valid: bool = True


class EvidenceSubmission(BaseModel):
    submission_id: str
    candidate_id: str
    evidence_class: EvidenceClass
    content: Dict[str, Any]
    submitted_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source_ref: str


class EvidenceAdmissibilityReport(BaseModel):
    report_id: str
    submission_id: str
    verdict: AdmissibilityVerdict
    reasons: List[str] = Field(default_factory=list)
    evaluated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ReadinessDomainVerdict(BaseModel):
    domain: ReadinessDomain
    verdict: DomainVerdict
    blockers: List[str] = Field(default_factory=list)
    caveats: List[str] = Field(default_factory=list)
    evidence_refs: List[str] = Field(default_factory=list)


class EvidenceConflict(BaseModel):
    conflict_id: str
    contradiction_class: ContradictionClass
    description: str
    involved_domains: List[ReadinessDomain]
    resolution_note: Optional[str] = None
    resolved: bool = False


class ReadinessDossier(BaseModel):
    dossier_id: str
    candidate_id: str
    snapshot_id: str
    domain_verdicts: Dict[ReadinessDomain, ReadinessDomainVerdict] = Field(
        default_factory=dict
    )
    admissible_evidence_refs: List[str] = Field(default_factory=list)
    inadmissible_evidence_refs: List[str] = Field(default_factory=list)
    conflicts: List[EvidenceConflict] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ConditionalGoTerms(BaseModel):
    scopes: List[ConditionalScope]
    expires_at: datetime
    conditions: List[str]
    monitoring_expectations: List[str]


class GoNoGoDecision(BaseModel):
    decision_id: str
    dossier_id: str
    verdict: BoardVerdict
    rationale: str
    conditional_terms: Optional[ConditionalGoTerms] = None
    decided_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class FinalDecisionMemo(BaseModel):
    memo_id: str
    decision_id: str
    memo_class: MemoClass
    executive_summary: str
    accepted_risks: List[str] = Field(default_factory=list)
    next_steps: List[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StagedPromotionPlan(BaseModel):
    plan_id: str
    candidate_id: str
    current_stage: PromotionStage
    target_stage: PromotionStage
    allowed: bool
    reasons: List[str] = Field(default_factory=list)

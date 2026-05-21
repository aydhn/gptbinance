from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.epistemic_plane.enums import (
    EpistemicClass, EvidenceClass, SufficiencyClass, ConfidenceClass,
    UncertaintyClass, KnowabilityClass, ContradictionClass, RefutationClass,
    EpistemicTrustVerdict, EpistemicEquivalenceVerdict
)

class EpistemicObjectRef(BaseModel):
    epistemic_id: str
    object_class: EpistemicClass

class BaseEpistemicRecord(BaseModel):
    epistemic_id: str
    owner: str
    scope: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class FactRecord(BaseEpistemicRecord):
    fact_description: str
    observed: bool = False
    validated: bool = False
    stale: bool = False
    proof_notes: str
    lineage_refs: List[str] = []

class ClaimRecord(BaseEpistemicRecord):
    claim_type: str # operational, policy, causal, eligibility
    description: str
    caveats: str
    basis_refs: List[str] = []
    lineage_refs: List[str] = []

class InferenceRecord(BaseEpistemicRecord):
    inference_type: str # direct, chained, heuristic
    description: str
    caveats: str
    proof_notes: str
    lineage_refs: List[str] = []

class HypothesisRecord(BaseEpistemicRecord):
    hypothesis_type: str # causal, operational, adversarial, competing
    description: str
    proof_notes: str
    lineage_refs: List[str] = []

class AssumptionRecord(BaseEpistemicRecord):
    assumption_type: str # explicit, dependency, scenario
    description: str
    hidden_warning: bool = False
    proof_notes: str
    lineage_refs: List[str] = []

class EstimateRecord(BaseEpistemicRecord):
    estimate_type: str # risk, value, timing
    description: str
    confidence_band: str
    proof_notes: str
    lineage_refs: List[str] = []

class EvidenceItemRecord(BaseEpistemicRecord):
    evidence_class: EvidenceClass
    description: str
    provenance_notes: str
    lineage_refs: List[str] = []

class EvidenceSetRecord(BaseEpistemicRecord):
    set_type: str # supporting, mixed, contradictory
    evidence_item_ids: List[str]
    completeness_notes: str
    lineage_refs: List[str] = []

class EvidenceLinkRecord(BaseEpistemicRecord):
    link_type: str # support, weaken, contradict, refute
    source_evidence_id: str
    target_claim_id: str
    sufficiency_notes: str
    lineage_refs: List[str] = []

class EvidenceSufficiencyRecord(BaseEpistemicRecord):
    target_claim_id: str
    sufficiency: SufficiencyClass
    rationale_notes: str
    lineage_refs: List[str] = []

class ConfidenceRecord(BaseEpistemicRecord):
    target_claim_id: str
    confidence_class: ConfidenceClass
    score: float
    proof_notes: str
    lineage_refs: List[str] = []

class UncertaintyRecord(BaseEpistemicRecord):
    target_claim_id: str
    uncertainty_class: UncertaintyClass
    caveats: str
    lineage_refs: List[str] = []

class ContradictionRecord(BaseEpistemicRecord):
    contradiction_class: ContradictionClass
    claim_id_a: str
    claim_id_b: str
    resolved: bool = False
    resolution_notes: Optional[str] = None
    lineage_refs: List[str] = []

class RefutationRecord(BaseEpistemicRecord):
    refutation_class: RefutationClass
    target_claim_id: str
    evidence_id: str
    stale_warning: bool = False
    scope_notes: str
    lineage_refs: List[str] = []

class UnknownRecord(BaseEpistemicRecord):
    unknown_type: str # explicit, known_unknown, currently_unknowable, monitoring_needed
    description: str
    proof_notes: str
    lineage_refs: List[str] = []

class KnowabilityRecord(BaseEpistemicRecord):
    target_unknown_id: str
    knowability_class: KnowabilityClass
    notes: str
    lineage_refs: List[str] = []

class BeliefRevisionRecord(BaseEpistemicRecord):
    target_claim_id: str
    revision_type: str # downgrade, upgrade, supersession, contradiction_driven
    proof_notes: str
    lineage_refs: List[str] = []

class ClaimLineageRecord(BaseEpistemicRecord):
    target_claim_id: str
    lineage_type: str # origin, revised, superseded, merged
    caveats: str

class EpistemicReadiness(BaseModel):
    claim_clarity: str
    evidence_sufficiency: str
    contradiction_cleanliness: str
    uncertainty_explicitness: str
    revision_discipline: str
    readiness_class: str

class EpistemicDebtRecord(BaseModel):
    debt_type: str
    severity: str
    description: str

class EpistemicForecastReport(BaseModel):
    contradiction_growth: str
    certainty_decay: str
    sufficiency_lag: str
    stale_claim: str

class EpistemicTrustVerdictRecord(BaseModel):
    verdict: EpistemicTrustVerdict
    factors: Dict[str, str]

class EpistemicEquivalenceReport(BaseModel):
    verdict: EpistemicEquivalenceVerdict
    divergence_sources: List[str]

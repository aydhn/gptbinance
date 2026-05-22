from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.adversarial_plane.enums import (
    AdversarialClass, ActorClass, IncentiveClass, SurfaceClass, ExploitClass,
    EvasionClass, GamingClass, PoisoningClass, SuspicionClass, ConfirmationClass,
    EquivalenceVerdict, TrustVerdict
)
import datetime

class AdversarialPlaneConfig(BaseModel):
    strict_mode: bool = True
    audit_trail_enabled: bool = True

class AdversarialObjectRef(BaseModel):
    adversarial_id: str
    adversarial_class: AdversarialClass

class AdversarialObject(BaseModel):
    adversarial_id: str
    adversarial_class: AdversarialClass
    name: str
    owner: str
    scope: str
    actor_posture: str
    exploit_posture: str
    created_at: str = Field(default_factory=lambda: datetime.datetime.utcnow().isoformat())

class ActorRecord(BaseModel):
    actor_id: str
    actor_class: ActorClass
    actor_posture_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class IncentiveRecord(BaseModel):
    incentive_id: str
    incentive_class: IncentiveClass
    ambiguity_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class AttackSurfaceRecord(BaseModel):
    surface_id: str
    surface_class: SurfaceClass
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ExploitRecord(BaseModel):
    exploit_id: str
    exploit_class: ExploitClass
    preconditions: List[str]
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class EvasionRecord(BaseModel):
    evasion_id: str
    evasion_class: EvasionClass
    caveats: str
    lineage_refs: List[str] = Field(default_factory=list)

class DeceptionRecord(BaseModel):
    deception_id: str
    deception_type: str # partial_truth, semantic, stale_as_fresh, proxy_safe
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ManipulationRecord(BaseModel):
    manipulation_id: str
    manipulation_type: str # metric, workflow, evidence_ordering, rollout_narrative
    caveats: str
    lineage_refs: List[str] = Field(default_factory=list)

class PoisoningRecord(BaseModel):
    poisoning_id: str
    poisoning_class: PoisoningClass
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class GamingRecord(BaseModel):
    gaming_id: str
    gaming_class: GamingClass
    caveats: str
    lineage_refs: List[str] = Field(default_factory=list)

class CircumventionRecord(BaseModel):
    circumvention_id: str
    bypass_type: str # control, policy, constitutional, scope
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class CollusionRecord(BaseModel):
    collusion_id: str
    collusion_type: str # human_human, human_agent, partner_local, tacit
    caveats: str
    lineage_refs: List[str] = Field(default_factory=list)

class SuspicionRecord(BaseModel):
    suspicion_id: str
    suspicion_class: SuspicionClass
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ConfirmationRecord(BaseModel):
    confirmation_id: str
    confirmation_class: ConfirmationClass
    scope: str
    stale_warning: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class RefutationRecord(BaseModel):
    refutation_id: str
    refutation_type: str # partial, full, scope_bounded
    unresolved_suspicion_caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class DetectabilityRecord(BaseModel):
    detectability_id: str
    detectability_level: str # easy, weak, stealthy, post_hoc
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ResistanceRecord(BaseModel):
    resistance_id: str
    resistance_level: str # strong, brittle, bypassable, layered
    sufficiency_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class PersistenceRecord(BaseModel):
    persistence_id: str
    persistence_level: str # one_shot, recurring, latent, normalized
    caveats: str
    lineage_refs: List[str] = Field(default_factory=list)

class BlastRadiusRecord(BaseModel):
    blast_radius_id: str
    radius_level: str # local, federated, delayed, hidden
    hidden_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class AdversarialComparisonRecord(BaseModel):
    comparison_id: str
    comparison_type: str # benign_vs_malicious, old_vs_hardened, exploit_a_vs_b, suspicion_vs_confirmation
    details: str
    lineage_refs: List[str] = Field(default_factory=list)

class AdversarialObservationReport(BaseModel):
    report_id: str
    observations: List[str]

class AdversarialForecastReport(BaseModel):
    forecast_id: str
    exploit_recurrence: str
    gaming_incentive_growth: str
    stealth_surface: str
    control_erosion: str
    uncertainty_classes: List[str]

class AdversarialDebtRecord(BaseModel):
    debt_id: str
    debt_type: str # bypassable_control, hidden_gaming, stale_suspicion, normalized_exploit, review_evasion
    severity: str
    interest: str

class AdversarialEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    blockers: List[str]

class AdversarialDivergenceReport(BaseModel):
    report_id: str
    divergences: List[str]
    severity: str

class AdversarialTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    caveats: List[str]
    blockers: List[str]

class AdversarialAuditRecord(BaseModel):
    audit_id: str
    action: str
    timestamp: str = Field(default_factory=lambda: datetime.datetime.utcnow().isoformat())
    details: Dict[str, Any]

class AdversarialArtifactManifest(BaseModel):
    manifest_id: str
    actors_refs: List[str]
    incentives_refs: List[str]
    surfaces_refs: List[str]
    exploits_refs: List[str]
    controls_refs: List[str]
    hash: str

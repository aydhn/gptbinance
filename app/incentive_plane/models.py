from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime
from app.incentive_plane.enums import (
    IncentiveClass, SubjectClass, TargetClass, LeverClass,
    RewardClass, PenaltyClass, FrictionClass, ClawbackClass,
    ConflictClass, GamingClass, EquivalenceVerdict, TrustVerdict
)

@dataclass
class IncentivePlaneConfig:
    strict_mode: bool = True

@dataclass
class IncentiveObjectRef:
    ref_id: str
    class_name: str

@dataclass
class IncentiveObject:
    id: str
    incentive_class: IncentiveClass
    owner: str
    scope: str
    behavioral_posture: str
    consequence_posture: str
    refs: List[IncentiveObjectRef] = field(default_factory=list)

@dataclass
class IncentiveRecord:
    id: str
    state: str
    proof_notes: List[str] = field(default_factory=list)
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveSubjectRecord:
    id: str
    subject_class: SubjectClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class BehavioralTargetRecord:
    id: str
    target_class: TargetClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveLeverRecord:
    id: str
    lever_class: LeverClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class RewardRecord:
    id: str
    reward_class: RewardClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class RewardFormulaRecord:
    id: str
    formula_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class DelayedRewardRecord:
    id: str
    status: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class PenaltyRecord:
    id: str
    penalty_class: PenaltyClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class PenaltyTriggerRecord:
    id: str
    trigger_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class FrictionControlRecord:
    id: str
    friction_class: FrictionClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class ClawbackRecord:
    id: str
    clawback_class: ClawbackClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class EscalationIncentiveRecord:
    id: str
    escalation_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class SurveillanceIncentiveRecord:
    id: str
    surveillance_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class SharedIncentiveRecord:
    id: str
    shared_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveConflictRecord:
    id: str
    conflict_class: ConflictClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class MoralHazardRecord:
    id: str
    hazard_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class ExternalityRecord:
    id: str
    externality_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class GamingSignalRecord:
    id: str
    gaming_class: GamingClass
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveReviewRecord:
    id: str
    review_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveRecalibrationRecord:
    id: str
    recalibration_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveComparisonRecord:
    id: str
    comparison_type: str
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IncentiveObservationReport:
    id: str
    report_data: Dict

@dataclass
class IncentiveForecastReport:
    id: str
    forecast_data: Dict

@dataclass
class IncentiveDebtRecord:
    id: str
    debt_type: str
    severity: str

@dataclass
class IncentiveEquivalenceReport:
    id: str
    verdict: EquivalenceVerdict

@dataclass
class IncentiveDivergenceReport:
    id: str
    divergence_type: str
    severity: str

@dataclass
class IncentiveTrustVerdict:
    id: str
    verdict: TrustVerdict
    factors: Dict[str, str]

@dataclass
class IncentiveAuditRecord:
    id: str
    audit_data: Dict

@dataclass
class IncentiveArtifactManifest:
    id: str
    manifest_data: Dict

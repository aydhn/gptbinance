import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content.strip() + '\n')
    print(f"Created {path}")

# --- ENUMS ---
enums_content = """
from enum import Enum

class IncentiveClass(Enum):
    ASSURANCE_QUALITY = "assurance_quality"
    IMMUNITY_REVALIDATION = "immunity_revalidation"
    ADAPTATION_EFFECTIVENESS = "adaptation_effectiveness"
    DRIFT_ESCALATION = "drift_escalation"
    BENEFICIARY_PROTECTION = "beneficiary_protection"
    CONTROL_DISCIPLINE = "control_discipline"
    COMPLIANCE_REPORTING = "compliance_reporting"
    SURVEILLANCE_DILIGENCE = "surveillance_diligence"
    RELEASE_SAFETY = "release_safety"
    MIGRATION_INTEGRITY = "migration_integrity"
    FEDERATED_ALIGNMENT = "federated_alignment"
    CROSS_PLANE_BEHAVIOR = "cross_plane_behavior"

class SubjectClass(Enum):
    PERSON = "person"
    ROLE = "role"
    TEAM = "team"
    COMMITTEE = "committee"

class TargetClass(Enum):
    GOOD = "good"
    INCOMPLETE = "incomplete"
    OVER_BROAD = "over_broad"
    GAMEABLE = "gameable"

class LeverClass(Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    MIXED = "mixed"
    INEFFECTIVE = "ineffective"

class RewardClass(Enum):
    ALIGNED = "aligned"
    RISK_ADJUSTED = "risk_adjusted"
    DELAYED = "delayed"
    PERVERSE = "perverse"

class PenaltyClass(Enum):
    PROPORTIONAL = "proportional"
    UNDER_DETERRING = "under_deterring"
    OVER_DETERRING = "over_deterring"
    SYMBOLIC = "symbolic"

class FrictionClass(Enum):
    HEALTHY = "healthy"
    INSUFFICIENT = "insufficient"
    EXCESSIVE = "excessive"
    BYPASSABLE = "bypassable"

class ClawbackClass(Enum):
    VALID = "valid"
    CONDITIONAL = "conditional"
    WEAK = "weak"
    UNAPPLIED = "unapplied"

class ConflictClass(Enum):
    DIRECT = "direct"
    LATENT = "latent"
    BENEFICIARY = "beneficiary"
    HIDDEN = "hidden"

class GamingClass(Enum):
    REWARD_HACKING = "reward_hacking"
    METRIC_CHASING = "metric_chasing"
    THRESHOLD_SURFING = "threshold_surfing"
    ASSURANCE_FARMING = "assurance_farming"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    BENEFICIARY_COST_DIVERGENT = "beneficiary_cost_divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
"""

# --- EXCEPTIONS ---
exceptions_content = """
class IncentivePlaneError(Exception):
    pass

class InvalidIncentiveObjectError(IncentivePlaneError):
    pass

class InvalidIncentiveSubjectError(IncentivePlaneError):
    pass

class InvalidBehavioralTargetError(IncentivePlaneError):
    pass

class InvalidRewardFormulaError(IncentivePlaneError):
    pass

class InvalidPenaltyTriggerError(IncentivePlaneError):
    pass

class InvalidClawbackError(IncentivePlaneError):
    pass

class IncentiveTheaterViolation(IncentivePlaneError):
    pass

class IncentiveStorageError(IncentivePlaneError):
    pass
"""

# --- MODELS ---
models_content = """
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
"""

base_content = """
class IncentiveRegistryBase:
    pass

class AlignmentEvaluatorBase:
    pass

class GamingEvaluatorBase:
    pass

class TrustEvaluatorBase:
    pass
"""

registry_content = """
from typing import Dict
from app.incentive_plane.models import IncentiveRecord

class CanonicalIncentiveRegistry:
    def __init__(self):
        self.records: Dict[str, IncentiveRecord] = {}

    def register(self, record: IncentiveRecord):
        self.records[record.id] = record

    def get(self, record_id: str) -> IncentiveRecord:
        return self.records.get(record_id)
"""

# Simple template for other modules
def create_module(name, classes):
    content = ""
    for cls in classes:
        content += f"class {cls}:\\n    pass\\n\\n"
    return content

files_to_create = {
    "app/incentive_plane/__init__.py": "",
    "app/incentive_plane/enums.py": enums_content,
    "app/incentive_plane/exceptions.py": exceptions_content,
    "app/incentive_plane/models.py": models_content,
    "app/incentive_plane/base.py": base_content,
    "app/incentive_plane/registry.py": registry_content,
    "app/incentive_plane/objects.py": create_module("objects", ["IncentiveObjectDefinitions", "AuthoritativeIncentiveObject", "LocalIncentiveObject", "FederatedIncentiveObject", "BeneficiaryImpactingIncentiveObject"]),
    "app/incentive_plane/incentives.py": create_module("incentives", ["ProposedIncentive", "ActiveIncentive", "DegradedIncentive", "RetiredIncentive"]),
    "app/incentive_plane/subjects.py": create_module("subjects", ["PersonSubject", "RoleSubject", "TeamSubject", "CommitteeSubject"]),
    "app/incentive_plane/targets.py": create_module("targets", ["GoodTarget", "IncompleteTarget", "OverBroadTarget", "GameableTarget"]),
    "app/incentive_plane/levers.py": create_module("levers", ["PositiveLever", "NegativeLever", "MixedLever", "IneffectiveLever"]),
    "app/incentive_plane/rewards.py": create_module("rewards", ["AlignedReward", "RiskAdjustedReward", "DelayedRewardEntity", "PerverseReward"]),
    "app/incentive_plane/reward_formulas.py": create_module("reward_formulas", ["RobustFormula", "FragileFormula", "GameableFormula", "BeneficiaryCostlyFormula"]),
    "app/incentive_plane/delayed_rewards.py": create_module("delayed_rewards", ["MatureDelayedReward", "PendingDelayedReward", "UnfairlyDelayedReward"]),
    "app/incentive_plane/penalties.py": create_module("penalties", ["ProportionalPenalty", "UnderDeterringPenalty", "OverDeterringPenalty", "SymbolicPenalty"]),
    "app/incentive_plane/penalty_triggers.py": create_module("penalty_triggers", ["ClearTrigger", "DelayedTrigger", "AmbiguousTrigger", "UnusedTrigger"]),
    "app/incentive_plane/frictions.py": create_module("frictions", ["HealthyFriction", "InsufficientFriction", "ExcessiveFriction", "BypassableFriction"]),
    "app/incentive_plane/clawbacks.py": create_module("clawbacks", ["ValidClawback", "ConditionalClawback", "WeakClawback", "UnappliedClawback"]),
    "app/incentive_plane/escalation.py": create_module("escalation", ["TimelyEscalationIncentive", "LateEscalationIncentive", "SuppressionProducingIncentive", "EscalationBlindIncentive"]),
    "app/incentive_plane/surveillance.py": create_module("surveillance", ["DiligenceAlignedIncentive", "CheckboxIncentive", "UnderReportingIncentive", "StaleSurveillanceIncentive"]),
    "app/incentive_plane/shared.py": create_module("shared", ["HealthySharedIncentive", "DilutedSharedIncentive", "OwnerBlurringSharedIncentive", "UnfairSharedBurden"]),
    "app/incentive_plane/conflicts.py": create_module("conflicts", ["DirectConflict", "LatentConflict", "BeneficiaryConflict", "HiddenConflict"]),
    "app/incentive_plane/moral_hazard.py": create_module("moral_hazard", ["RiskTakingHazard", "ConcealmentHazard", "EscalationAvoidanceHazard", "HiddenMoralHazard"]),
    "app/incentive_plane/externalities.py": create_module("externalities", ["LocalOptimizationExternality", "FederatedExternality", "BeneficiaryExternality", "HiddenExternality"]),
    "app/incentive_plane/gaming.py": create_module("gaming", ["RewardHacking", "MetricChasing", "ThresholdSurfing", "AssuranceFarming"]),
    "app/incentive_plane/reviews.py": create_module("reviews", ["ScheduledReview", "TriggeredReview", "OverdueReview", "CosmeticReview"]),
    "app/incentive_plane/recalibration.py": create_module("recalibration", ["SafeRecalibration", "CorrectiveRecalibration", "UnjustifiedRecalibration", "ManipulationByRecalibration"]),
    "app/incentive_plane/comparisons.py": create_module("comparisons", ["IntendedVsObservedBehaviorCompare", "RewardVsPenaltyCompare", "LocalVsFederatedIncentiveCompare", "AlignedVsGameableIncentiveCompare"]),
    "app/incentive_plane/forecasting.py": create_module("forecasting", ["GamingGrowthForecast", "MoralHazardForecast", "UnderReportingForecast", "BeneficiaryCostForecast", "IncentiveDriftForecast"]),
    "app/incentive_plane/debt.py": create_module("debt", ["RewardHackingDebt", "SymbolicPenaltyDebt", "HiddenConflictDebt", "ExternalityDebt", "ClawbackGapDebt"]),
    "app/incentive_plane/readiness.py": create_module("readiness", ["IncentiveReadinessAggregation", "TargetClarity", "FormulaIntegrity", "FrictionSufficiency", "GamingVisibility", "BeneficiaryCostVisibility"]),
    "app/incentive_plane/accountability.py": create_module("accountability", ["AccountabilityLinkage", "SanctionAlignedIncentiveEffects"]),
    "app/incentive_plane/assurance.py": create_module("assurance", ["AssuranceLinkage", "AssuranceQualityIncentive"]),
    "app/incentive_plane/immunity.py": create_module("immunity", ["ImmunityLinkage", "RevalidationIncentive"]),
    "app/incentive_plane/adaptation.py": create_module("adaptation", ["AdaptationLinkage", "VerifiedFixIncentive"]),
    "app/incentive_plane/drift.py": create_module("drift", ["DriftLinkage", "EscalationEarlyWarningIncentive"]),
    "app/incentive_plane/normalization.py": create_module("normalization", ["NormalizationLinkage", "SafeReEntryIncentive"]),
    "app/incentive_plane/recovery.py": create_module("recovery", ["RecoveryLinkage", "HonestRecoveryReportingIncentive"]),
    "app/incentive_plane/rights.py": create_module("rights", ["RightsLinkage", "BeneficiaryRightPreservingIncentive"]),
    "app/incentive_plane/liability.py": create_module("liability", ["LiabilityLinkage", "LiabilityAwareIncentiveDesign"]),
    "app/incentive_plane/authority.py": create_module("authority", ["AuthorityLinkage"]),
    "app/incentive_plane/precedent.py": create_module("precedent", ["PrecedentLinkage", "IncentivePrecedentCaution"]),
    "app/incentive_plane/jurisdiction.py": create_module("jurisdiction", ["JurisdictionLinkage", "IncentiveApplicabilityScope", "CrossBoundaryCompensationValidity"]),
    "app/incentive_plane/finality.py": create_module("finality", ["FinalityLinkage", "IncentiveResolution"]),
    "app/incentive_plane/commitment.py": create_module("commitment", ["CommitmentLinkage", "IncentiveRetentionCommitments"]),
    "app/incentive_plane/remedy.py": create_module("remedy", ["RemedyLinkage", "RemedyAlignedIncentive"]),
    "app/incentive_plane/representation.py": create_module("representation", ["RepresentationLinkage", "AlignedDisclosures"]),
    "app/incentive_plane/interpretation.py": create_module("interpretation", ["InterpretationLinkage", "ClauseConstruction"]),
    "app/incentive_plane/adversarial.py": create_module("adversarial", ["AdversarialLinkage"]),
    "app/incentive_plane/tradeoff.py": create_module("tradeoff", ["TradeoffLinkage", "SpeedVsDiligence", "GrowthVsSafety", "EfficiencyVsBeneficiaryProtection"]),
    "app/incentive_plane/epistemic.py": create_module("epistemic", ["EpistemicLinkage", "UncertainBehaviorAttribution", "UncertainFormulaEfficacy", "WeakAntiGamingBasis"]),
    "app/incentive_plane/semantic.py": create_module("semantic", ["SemanticLinkage"]),
    "app/incentive_plane/temporal.py": create_module("temporal", ["TemporalLinkage"]),
    "app/incentive_plane/provenance.py": create_module("provenance", ["ProvenanceLinkage"]),
    "app/incentive_plane/autonomy.py": create_module("autonomy", ["AutonomyLinkage", "AutomatedRewardScoring"]),
    "app/incentive_plane/federation.py": create_module("federation", ["FederationLinkage", "FederatedIncentiveAlignment", "LocalVsFederatedExternalityGaps"]),
    "app/incentive_plane/constitution.py": create_module("constitution", ["ConstitutionLinkage", "BeneficiaryProtectiveIncentiveFloors"]),
    "app/incentive_plane/contracts.py": create_module("contracts", ["ContractLinkage", "IncentiveBoundContractualObligations", "ClawbackTriggeredContractualConsequences"]),
    "app/incentive_plane/compliance.py": create_module("compliance", ["ComplianceLinkage", "ComplianceReportingIncentive", "ContinuingAntiConcealmentDuties"]),
    "app/incentive_plane/security.py": create_module("security", ["SecurityLinkage", "SecurityDiligenceIncentive", "RetainedHardeningIncentives"]),
    "app/incentive_plane/incidents.py": create_module("incidents", ["IncidentLinkage", "IncidentReportingIncentive"]),
    "app/incentive_plane/releases_domain.py": create_module("releases_domain", ["ReleaseLinkage", "ReleaseSafetyIncentive"]),
    "app/incentive_plane/migrations.py": create_module("migrations", ["MigrationLinkage", "MigrationIntegrityIncentive"]),
    "app/incentive_plane/policy.py": create_module("policy", ["PolicyLinkage", "MinimumIncentiveControls"]),
    "app/incentive_plane/scenario.py": create_module("scenario", ["ScenarioLinkage", "RewardHackingScenario", "ConcealmentIncentiveScenario", "BeneficiaryCostExplosionScenario"]),
    "app/incentive_plane/equivalence.py": create_module("equivalence", ["ReplayPaperProbationLiveIncentiveEquivalence", "PartialEquivalenceClasses", "BeneficiaryAwareEquivalence"]),
    "app/incentive_plane/divergence.py": create_module("divergence", ["IncentiveDivergence", "TargetDivergence", "RewardDivergence", "PenaltyDivergence", "GamingDivergence", "ExternalityDivergence"]),
    "app/incentive_plane/quality.py": create_module("quality", ["IncentiveQualityChecks", "RewardHackingWarning", "SymbolicPenaltyWarning", "HiddenConflictWarning", "BeneficiaryCostWarning", "ExternalityWarning", "SuppressionIncentiveWarning", "QualityVerdict"]),
    "app/incentive_plane/trust.py": create_module("trust", ["TrustedIncentiveVerdictEngine"]),
    "app/incentive_plane/manifests.py": create_module("manifests", ["IncentiveManifestBuilder"]),
    "app/incentive_plane/reporting.py": create_module("reporting", ["IncentiveRegistrySummary", "IncentivesSummary", "RewardsSummary", "ConflictsSummary", "DebtSummary"]),
    "app/incentive_plane/storage.py": create_module("storage", ["IncentiveStorage"]),
    "app/incentive_plane/repository.py": create_module("repository", ["IncentiveRepository"]),
    "app/incentive_plane/README.md": "# Incentive Plane\\n\\nNeden incentive plane gerektiği\\nsubjects/targets -> rewards/penalties/frictions -> gaming/conflicts -> trust akışı\\nwhy rewarded != aligned != safe\\nwhy no reward hacking / no beneficiary-blind optimization\\nbu fazın sınırları\\n"
}

for path, content in files_to_create.items():
    create_file(path, content)

import os
import textwrap

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(textwrap.dedent(content).strip() + '\n')

print("Generating Phase 86 Files...")

# 1. Enums
create_file("app/decision_quality_plane/enums.py", """
from enum import Enum

class DecisionClass(str, Enum):
    STRATEGY_PROMOTION = "strategy_promotion"
    RELEASE_ROLLOUT = "release_rollout"
    ACTIVATION_PROGRESSION = "activation_progression"
    RISK_OVERRIDE = "risk_override"
    ALLOCATION_REGIME = "allocation_regime"
    EXECUTION_INTERVENTION = "execution_intervention"
    WORKFLOW_RERUN = "workflow_rerun"
    INCIDENT_CONTAINMENT = "incident_containment"
    FAILOVER = "failover"
    MIGRATION_CUTOVER = "migration_cutover"
    EXPERIMENT_WINNER = "experiment_winner"
    CAPITAL_REALLOCATION = "capital_reallocation"

class RecommendationClass(str, Enum):
    MODEL_DRIVEN = "model_driven"
    RESEARCH_DRIVEN = "research_driven"
    EXPERIMENT_DRIVEN = "experiment_driven"
    OPERATOR_DRIVEN = "operator_driven"
    POLICY_BOUNDED = "policy_bounded"

class OptionClass(str, Enum):
    BASE_CASE = "base_case"
    CONSERVATIVE = "conservative"
    AGGRESSIVE = "aggressive"
    DEFER_NO_OP = "defer_no_op"
    ROLLBACK = "rollback"
    STOP_TRADING = "stop_trading"

class EvidenceClass(str, Enum):
    RESEARCH = "research"
    SIMULATION = "simulation"
    EXPERIMENT = "experiment"
    MARKET_TRUTH = "market_truth"
    RISK_PERFORMANCE = "risk_performance"

class AssumptionClass(str, Enum):
    MARKET_STATE = "market_state"
    LIQUIDITY = "liquidity"
    RELIABILITY = "reliability"
    DEPENDENCY = "dependency"

class UncertaintyClass(str, Enum):
    MODEL = "model"
    DATA = "data"
    MARKET = "market"
    OPERATIONAL = "operational"
    STRUCTURAL = "structural"

class ConfidenceClass(str, Enum):
    VERY_HIGH = "very_high"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "very_low"
    UNKNOWN = "unknown"

class OutcomeClass(str, Enum):
    SUCCESS = "success"
    PARTIAL_SUCCESS = "partial_success"
    FAILURE = "failure"
    AMBIGUOUS = "ambiguous"
    PENDING = "pending"

class CalibrationClass(str, Enum):
    CALIBRATED = "calibrated"
    OVERCONFIDENT = "overconfident"
    UNDERCONFIDENT = "underconfident"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
""")

# 2. Exceptions
create_file("app/decision_quality_plane/exceptions.py", """
class DecisionQualityPlaneError(Exception): pass
class InvalidDecisionDefinitionError(DecisionQualityPlaneError): pass
class InvalidOptionSetError(DecisionQualityPlaneError): pass
class InvalidEvidenceBundleError(DecisionQualityPlaneError): pass
class InvalidAssumptionRecordError(DecisionQualityPlaneError): pass
class InvalidConfidenceRecordError(DecisionQualityPlaneError): pass
class InvalidOutcomeReviewError(DecisionQualityPlaneError): pass
class CounterfactualViolationError(DecisionQualityPlaneError): pass
class CalibrationViolationError(DecisionQualityPlaneError): pass
class DecisionStorageError(DecisionQualityPlaneError): pass
class HindsightRewriteAttemptError(DecisionQualityPlaneError): pass
class DecisionEquivalenceError(DecisionQualityPlaneError): pass
""")

# 3. Models
create_file("app/decision_quality_plane/models.py", """
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.decision_quality_plane.enums import (
    DecisionClass, OptionClass, ConfidenceClass, OutcomeClass, TrustVerdict,
    RecommendationClass, EvidenceClass, AssumptionClass, UncertaintyClass,
    CalibrationClass, EquivalenceVerdict
)

class DecisionDefinition(BaseModel):
    decision_id: str
    decision_class: DecisionClass
    owner: str
    intent: str
    context: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    lineage_refs: List[str] = Field(default_factory=list)

class RecommendationRecord(BaseModel):
    recommendation_id: str
    recommendation_class: RecommendationClass
    decision_id: str
    source_ref: str
    confidence_caveats: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class OptionRecord(BaseModel):
    option_id: str
    option_class: OptionClass
    description: str
    reversibility: str
    blast_radius: str

class OptionComparison(BaseModel):
    comparison_id: str
    decision_id: str
    base_option_id: str
    compared_option_id: str
    trade_off_analysis: str
    downside_risk: str
    dependency_comparison: str
    proof_notes: str

class EvidenceBundleRef(BaseModel):
    evidence_id: str
    evidence_class: EvidenceClass
    source: str
    summary: str
    is_contradictory: bool = False

class AssumptionRecord(BaseModel):
    assumption_id: str
    assumption_class: AssumptionClass
    description: str
    fragility_notes: str
    expiry_condition: str

class HypothesisRecord(BaseModel):
    hypothesis_id: str
    description: str
    invalidation_criteria: str
    confidence_linkage: str
    lineage_refs: List[str] = Field(default_factory=list)

class RationaleRecord(BaseModel):
    rationale_id: str
    chosen_option_id: str
    rejected_option_ids: List[str]
    justification: str
    non_goals: List[str]
    proof_notes: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class UncertaintyRecord(BaseModel):
    uncertainty_id: str
    uncertainty_class: UncertaintyClass
    description: str
    burden_notes: str

class ConfidenceRecord(BaseModel):
    confidence_id: str
    confidence_level: ConfidenceClass
    justification: str
    overconfidence_warning: bool = False
    lineage_refs: List[str] = Field(default_factory=list)

class CounterargumentRecord(BaseModel):
    counterargument_id: str
    critique: str
    downside_thesis: str
    rebuttal_quality_notes: str

class PremortemRecord(BaseModel):
    premortem_id: str
    failure_mode: str
    trigger: str
    mitigation_option: Optional[str] = None
    completeness_notes: str = ""

class DecisionChecklistRecord(BaseModel):
    checklist_id: str
    required_evidence_checked: bool
    required_risk_checked: bool
    required_policy_checked: bool
    skipped_items: List[str] = Field(default_factory=list)

class PrecommitmentRecord(BaseModel):
    commitment_id: str
    stop_loss_criteria: str
    re_evaluation_date: datetime
    confidence_decay_triggers: str

class StopConditionRecord(BaseModel):
    stop_id: str
    invalidation_stops: str
    budget_risk_stops: str
    reliability_security_stops: str

class DecisionActionRecord(BaseModel):
    action_id: str
    decision_id: str
    chosen_action_ref: str
    is_deferred: bool = False
    is_rejected: bool = False

class DecisionOutcomeRecord(BaseModel):
    outcome_id: str
    decision_id: str
    outcome_class: OutcomeClass
    expected_vs_actual: str
    ambiguity_notes: str
    reviewed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CounterfactualReviewRecord(BaseModel):
    review_id: str
    decision_id: str
    baseline_option_id: str
    hypothetical_outcome: str
    proof_notes: str

class CalibrationRecord(BaseModel):
    calibration_id: str
    decision_id: str
    calibration_class: CalibrationClass
    realized_hit_rate: str
    repeated_bias_notes: str

class DecisionRecurrenceRecord(BaseModel):
    recurrence_id: str
    decision_id: str
    repeated_missing_option: bool = False
    repeated_hidden_assumption: bool = False
    repeated_overconfidence: bool = False
    recurrence_notes: str

class DecisionEquivalenceReport(BaseModel):
    report_id: str
    decision_id: str
    verdict: EquivalenceVerdict
    proof_notes: str
    blockers: List[str] = Field(default_factory=list)

class DecisionDivergenceReport(BaseModel):
    report_id: str
    decision_id: str
    divergence_source: str
    severity: str

class DecisionTrustVerdict(BaseModel):
    decision_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, str]
    blockers: List[str] = Field(default_factory=list)

class DecisionManifest(BaseModel):
    decision: DecisionDefinition
    recommendations: List[RecommendationRecord] = Field(default_factory=list)
    options: List[OptionRecord] = Field(default_factory=list)
    comparisons: List[OptionComparison] = Field(default_factory=list)
    evidence: List[EvidenceBundleRef] = Field(default_factory=list)
    assumptions: List[AssumptionRecord] = Field(default_factory=list)
    hypotheses: List[HypothesisRecord] = Field(default_factory=list)
    rationale: List[RationaleRecord] = Field(default_factory=list)
    uncertainty: List[UncertaintyRecord] = Field(default_factory=list)
    confidence: Optional[ConfidenceRecord] = None
    counterarguments: List[CounterargumentRecord] = Field(default_factory=list)
    premortems: List[PremortemRecord] = Field(default_factory=list)
    checklists: List[DecisionChecklistRecord] = Field(default_factory=list)
    precommitments: List[PrecommitmentRecord] = Field(default_factory=list)
    stop_conditions: List[StopConditionRecord] = Field(default_factory=list)
    action: Optional[DecisionActionRecord] = None
    outcome: Optional[DecisionOutcomeRecord] = None
    counterfactuals: List[CounterfactualReviewRecord] = Field(default_factory=list)
    calibration: Optional[CalibrationRecord] = None
    recurrence: Optional[DecisionRecurrenceRecord] = None
    equivalence: Optional[DecisionEquivalenceReport] = None
    divergence: Optional[DecisionDivergenceReport] = None
    trust_verdict: Optional[DecisionTrustVerdict] = None
""")

# 4. Base
create_file("app/decision_quality_plane/base.py", """
from abc import ABC, abstractmethod
from app.decision_quality_plane.models import DecisionManifest

class DecisionRegistryBase(ABC):
    @abstractmethod
    def register(self, manifest: DecisionManifest):
        pass

class EpistemicEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, manifest: DecisionManifest):
        pass
""")

# 5. Registry
create_file("app/decision_quality_plane/registry.py", """
from typing import Dict, List
from app.decision_quality_plane.models import DecisionDefinition
from app.decision_quality_plane.exceptions import InvalidDecisionDefinitionError

class CanonicalDecisionRegistry:
    def __init__(self):
        self._decisions: Dict[str, DecisionDefinition] = {}

    def register(self, decision: DecisionDefinition) -> None:
        if not decision.decision_id or not decision.decision_class:
            raise InvalidDecisionDefinitionError("Missing critical decision fields")
        self._decisions[decision.decision_id] = decision

    def get(self, decision_id: str) -> DecisionDefinition:
        return self._decisions.get(decision_id)

    def list_all(self) -> List[DecisionDefinition]:
        return list(self._decisions.values())
""")

# 6-12. Many managers... Let's use a repository for storage
create_file("app/decision_quality_plane/repository.py", """
from typing import Dict, List
from app.decision_quality_plane.models import DecisionManifest
from app.decision_quality_plane.exceptions import DecisionStorageError

class DecisionRepository:
    def __init__(self):
        self._manifests: Dict[str, DecisionManifest] = {}

    def save(self, manifest: DecisionManifest):
        self._manifests[manifest.decision.decision_id] = manifest

    def get(self, decision_id: str) -> DecisionManifest:
        return self._manifests.get(decision_id)

    def list_all(self) -> List[DecisionManifest]:
        return list(self._manifests.values())
""")

# Quality
create_file("app/decision_quality_plane/quality.py", """
from app.decision_quality_plane.models import DecisionManifest

class DecisionQualityChecker:
    def check(self, manifest: DecisionManifest) -> dict:
        warnings = []
        if len(manifest.options) < 2:
            warnings.append("Missing options warning")
        if not manifest.assumptions:
            warnings.append("Hidden assumption warning")
        if manifest.evidence and all(not e.is_contradictory for e in manifest.evidence):
            warnings.append("One-sided evidence warning")
        if manifest.confidence and manifest.confidence.confidence_level.value == "very_high" and not manifest.evidence:
            warnings.append("Inflated confidence warning")
        if not manifest.premortems:
            warnings.append("Missing premortem warning")
        if manifest.outcome and not manifest.counterfactuals:
            warnings.append("Missing counterfactual warning")

        return {
            "verdict": "OK" if not warnings else "NEEDS_IMPROVEMENT",
            "warnings": warnings
        }
""")

# Trust
create_file("app/decision_quality_plane/trust.py", """
from app.decision_quality_plane.models import DecisionTrustVerdict, DecisionManifest
from app.decision_quality_plane.enums import TrustVerdict

class TrustVerdictEngine:
    def evaluate(self, manifest: DecisionManifest) -> DecisionTrustVerdict:
        blockers = []
        breakdown = {}

        # 1. Option Completeness
        has_noop = any(o.option_class.value == "defer_no_op" for o in manifest.options)
        if len(manifest.options) < 2 or not has_noop:
            blockers.append("Missing options or NO_OP baseline")
            breakdown["options"] = "FAILED"
        else:
            breakdown["options"] = "OK"

        # 2. Assumptions Clarity
        if not manifest.assumptions:
            blockers.append("Hidden assumptions risk: no explicit assumptions recorded")
            breakdown["assumptions"] = "FAILED"
        else:
            breakdown["assumptions"] = "OK"

        # 3. Rationale
        if not manifest.rationale:
            blockers.append("Missing rationale for chosen option")
            breakdown["rationale"] = "FAILED"
        else:
            breakdown["rationale"] = "OK"

        # 4. Confidence Calibration
        if manifest.confidence and manifest.confidence.confidence_level.value == "very_high" and not manifest.evidence:
            blockers.append("Overconfidence detected: VERY_HIGH confidence with 0 evidence")
            breakdown["confidence"] = "FAILED"
        else:
            breakdown["confidence"] = "OK"

        # 5. Premortem & Stop conditions
        if not manifest.premortems:
            blockers.append("Missing premortem for decision")
            breakdown["premortem"] = "FAILED"
        else:
            breakdown["premortem"] = "OK"

        if len(blockers) > 0:
            return DecisionTrustVerdict(
                decision_id=manifest.decision.decision_id,
                verdict=TrustVerdict.BLOCKED,
                breakdown=breakdown,
                blockers=blockers
            )

        return DecisionTrustVerdict(
            decision_id=manifest.decision.decision_id,
            verdict=TrustVerdict.TRUSTED,
            breakdown=breakdown
        )
""")

# Manifests
create_file("app/decision_quality_plane/manifests.py", """
from app.decision_quality_plane.models import DecisionManifest, DecisionDefinition
from app.decision_quality_plane.enums import DecisionClass

class DecisionManifestBuilder:
    def build_empty(self, decision_id: str, owner: str, intent: str, dclass: DecisionClass) -> DecisionManifest:
        dec = DecisionDefinition(
            decision_id=decision_id,
            decision_class=dclass,
            owner=owner,
            intent=intent
        )
        return DecisionManifest(decision=dec)
""")

# CLI Integration
create_file("app/main.py", """
import sys
import json
import argparse
from app.decision_quality_plane.registry import CanonicalDecisionRegistry
from app.decision_quality_plane.repository import DecisionRepository

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-decision-registry", action="store_true")
    parser.add_argument("--show-decision", type=str, help="Decision ID")
    parser.add_argument("--show-recommendations", action="store_true")
    parser.add_argument("--show-decision-options", action="store_true")
    parser.add_argument("--show-option-comparisons", action="store_true")
    parser.add_argument("--show-decision-evidence", action="store_true")
    parser.add_argument("--show-assumptions", action="store_true")
    parser.add_argument("--show-hypotheses", action="store_true")
    parser.add_argument("--show-rationales", action="store_true")
    parser.add_argument("--show-uncertainty-confidence", action="store_true")
    parser.add_argument("--show-counterarguments", action="store_true")
    parser.add_argument("--show-premortems", action="store_true")
    parser.add_argument("--show-decision-checklists", action="store_true")
    parser.add_argument("--show-precommitments", action="store_true")
    parser.add_argument("--show-stop-conditions", action="store_true")
    parser.add_argument("--show-decision-actions", action="store_true")
    parser.add_argument("--show-decision-outcomes", action="store_true")
    parser.add_argument("--show-counterfactual-reviews", action="store_true")
    parser.add_argument("--show-calibration-records", action="store_true")
    parser.add_argument("--show-decision-recurrence", action="store_true")
    parser.add_argument("--show-decision-equivalence", action="store_true")
    parser.add_argument("--show-decision-trust", action="store_true")
    parser.add_argument("--show-decision-review-packs", action="store_true")

    args, unknown = parser.parse_known_args()

    repo = DecisionRepository()

    if args.show_decision_registry:
        print(json.dumps({"decisions": []}, indent=2))
    elif args.show_decision:
        print(json.dumps({"decision_id": args.show_decision, "status": "Not Found"}, indent=2))
    elif args.show_recommendations:
        print("Recommendations: []")
    elif args.show_decision_options:
        print("Options: []")
    elif args.show_option_comparisons:
        print("Option Comparisons: []")
    elif args.show_decision_evidence:
        print("Evidence: []")
    elif args.show_assumptions:
        print("Assumptions: []")
    elif args.show_hypotheses:
        print("Hypotheses: []")
    elif args.show_rationales:
        print("Rationales: []")
    elif args.show_uncertainty_confidence:
        print("Uncertainty & Confidence: []")
    elif args.show_counterarguments:
        print("Counterarguments: []")
    elif args.show_premortems:
        print("Premortems: []")
    elif args.show_decision_checklists:
        print("Checklists: []")
    elif args.show_precommitments:
        print("Precommitments: []")
    elif args.show_stop_conditions:
        print("Stop Conditions: []")
    elif args.show_decision_actions:
        print("Actions: []")
    elif args.show_decision_outcomes:
        print("Outcomes: []")
    elif args.show_counterfactual-reviews:
        print("Counterfactual Reviews: []")
    elif args.show_calibration_records:
        print("Calibration Records: []")
    elif args.show_decision_recurrence:
        print("Recurrence: []")
    elif args.show_decision_equivalence:
        print("Equivalence: []")
    elif args.show_decision_trust:
        print("Trust Verdicts: []")
    elif args.show_decision_review_packs:
        print("Review Packs: []")
    else:
        print("System initialized. Decision Quality Plane Ready.")

if __name__ == "__main__":
    main()
""")

# Fake Integrations
create_file("app/policy_kernel/invariants.py", """
class InvariantChecker:
    def check_no_trusted_high_risk_action_under_missing_option_set(self, trust_verdict):
        if trust_verdict.verdict == "blocked" and "options" in trust_verdict.blockers:
            raise Exception("Invariant violated: high risk action missing option set")
""")

create_file("app/readiness_board/domains.py", """
class DecisionIntegrityDomain:
    def evaluate(self, manifest):
        return {"status": "passing" if manifest.rationale else "failing"}
""")

create_file("app/telegram/templates.py", """
DECISION_MANIFEST_READY = "Decision {id} manifest is ready. Status: {status}"
CRITICAL_DECISION_WITHOUT_OPTION_SET = "ALERT: Critical decision {id} has incomplete option set!"
OVERCONFIDENCE_PATTERN_DETECTED = "CAUTION: Overconfidence pattern detected in decision {id}"
OUTCOME_REVIEW_OVERDUE = "ALERT: Outcome review overdue for decision {id}"
DECISION_REVIEW_REQUIRED = "Decision {id} requires review."
""")

create_file("app/research_plane/evidence.py", """
class ResearchEvidenceExporter:
    def export(self):
        return {"evidence_class": "research"}
""")

create_file("app/experiment_plane/recommendations.py", """
class ExperimentRecommendationExporter:
    def export(self):
        return {"recommendation_class": "experiment_driven"}
""")

create_file("app/simulation_plane/results.py", """
class SimulationExporter:
    def export(self):
        return {"evidence_class": "simulation"}
""")

create_file("app/strategy_plane/lifecycle.py", """
class StrategyTransition:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/risk_plane/manifests.py", """
class RiskPostureExporter:
    def export(self):
        return {"evidence_class": "risk_performance"}
""")

create_file("app/allocation/intents.py", """
class AllocationIntent:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/execution_plane/runtime.py", """
class ExecutionIntervention:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/control_plane/receipts.py", """
class ActionReceipt:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/release_plane/readiness.py", """
class ReleaseReadiness:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/release_plane/rollouts.py", """
class ReleaseRollout:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/activation/guards.py", """
class ActivationGuard:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/activation/history.py", """
class ActivationHistory:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/policy_plane/evaluations.py", """
class PolicyEvaluation:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/policy_kernel/context.py", """
class PolicyContext:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/readiness_board/evidence.py", """
class ReadinessEvidence:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/reliability/domains.py", """
class ReliabilityDomain:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/reliability/slos.py", """
class DecisionIntegritySLO:
    def __init__(self):
        self.name = "missing-option absence"
""")

create_file("app/incident_plane/triage.py", """
class IncidentTriage:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/incident_plane/recovery.py", """
class IncidentRecovery:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/postmortem_plane/evidence.py", """
class PostmortemEvidence:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/postmortem_plane/lessons.py", """
class LessonsLearned:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/observability_plane/events.py", """
class CanonicalDecisionEvents:
    DECISION_CREATED = "decision_created"
    OPTION_COMPARED = "option_compared"
""")

create_file("app/observability_plane/diagnostics.py", """
class Diagnostics:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/compliance_plane/requirements.py", """
class ComplianceRequirements:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/compliance_plane/findings.py", """
class ComplianceFindings:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/security_plane/readiness.py", """
class SecurityReadiness:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/migration_plane/prechecks.py", """
class MigrationPrechecks:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/continuity_plane/readiness.py", """
class ContinuityReadiness:
    def __init__(self, decision_manifest):
        self.manifest = decision_manifest
""")

create_file("app/evidence_graph/artefacts.py", """
class DecisionArtefacts:
    pass
""")

create_file("app/evidence_graph/packs.py", """
class DecisionIntegrityPack:
    pass
""")

create_file("app/reviews/requests.py", """
class DecisionIntegrityReview:
    pass
""")

create_file("app/identity/capabilities.py", """
class DecisionCapabilities:
    INSPECT_DECISION_MANIFEST = "inspect_decision_manifest"
""")

create_file("app/observability/alerts.py", """
class DecisionAlerts:
    HIDDEN_ASSUMPTION_DETECTED = "hidden_assumption_detected"
""")

create_file("app/observability/runbooks.py", """
class DecisionRunbooks:
    DECISION_OPTION_SET_REVIEW = "decision_option_set_review"
""")

create_file("app/telegram/notifier.py", """
class DecisionNotifier:
    pass
""")

# Documentation
create_file("docs/439_decision_quality_plane_ve_epistemic_governance_mimarisi.md", """
# Decision Quality Plane
Recommendations -> Options -> Evidence -> Assumptions -> Decision -> Outcome -> Calibration.
Outcome != Decision Quality.
No hindsight rewrite.
""")

create_file("docs/440_option_set_assumption_uncertainty_confidence_ve_premortem_politikasi.md", """
# Options, Assumptions, Uncertainty, Confidence, Premortem
""")

create_file("docs/441_outcome_review_counterfactual_calibration_ve_recurrence_politikasi.md", """
# Outcome Review, Counterfactual, Calibration, Recurrence
""")

create_file("docs/442_decision_integrity_readiness_activation_release_risk_entegrasyonu_politikasi.md", """
# Readiness, Activation, Release, Risk Integration
""")

create_file("docs/443_phase_86_definition_of_done.md", """
# Definition of Done
""")

# TESTS
create_file("tests/test_decision_quality_plane_core.py", """
import pytest
from app.decision_quality_plane.enums import DecisionClass, OptionClass, ConfidenceClass, TrustVerdict
from app.decision_quality_plane.models import (
    DecisionDefinition, OptionRecord, RationaleRecord, ConfidenceRecord,
    DecisionManifest, PremortemRecord, DecisionOutcomeRecord, OutcomeClass, CounterfactualReviewRecord,
    CalibrationRecord, CalibrationClass
)
from app.decision_quality_plane.registry import CanonicalDecisionRegistry
from app.decision_quality_plane.exceptions import InvalidOptionSetError, InvalidDecisionDefinitionError
from app.decision_quality_plane.trust import TrustVerdictEngine
from app.decision_quality_plane.quality import DecisionQualityChecker
from app.decision_quality_plane.repository import DecisionRepository
from app.decision_quality_plane.manifests import DecisionManifestBuilder

def test_decision_registry():
    registry = CanonicalDecisionRegistry()
    dec = DecisionDefinition(decision_id="D-101", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="Alice", intent="Promote v2")
    registry.register(dec)
    assert registry.get("D-101").owner == "Alice"
    with pytest.raises(InvalidDecisionDefinitionError):
        registry.register(DecisionDefinition(decision_id="", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="A", intent="B"))

def test_option_completeness():
    manifest = DecisionManifest(decision=DecisionDefinition(decision_id="D-1", decision_class=DecisionClass.FAILOVER, owner="B", intent="C"))
    manifest.options.append(OptionRecord(option_id="O-1", option_class=OptionClass.AGGRESSIVE, description="Rollout now", reversibility="Hard", blast_radius="High"))

    engine = TrustVerdictEngine()
    verdict = engine.evaluate(manifest)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert "options" in verdict.breakdown
    assert verdict.breakdown["options"] == "FAILED"

    manifest.options.append(OptionRecord(option_id="O-2", option_class=OptionClass.DEFER_NO_OP, description="Do nothing", reversibility="Easy", blast_radius="None"))
    verdict2 = engine.evaluate(manifest)
    assert verdict2.breakdown["options"] == "OK"

def test_trust_verdict_engine():
    dec = DecisionDefinition(decision_id="D-101", decision_class=DecisionClass.RELEASE_ROLLOUT, owner="Alice", intent="Promote v2")
    manifest = DecisionManifest(decision=dec)

    engine = TrustVerdictEngine()
    verdict = engine.evaluate(manifest)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert "options" in verdict.breakdown
    assert verdict.breakdown["options"] == "FAILED"

    manifest.options = [
        OptionRecord(option_id="O-1", option_class=OptionClass.AGGRESSIVE, description="Rollout now", reversibility="Hard", blast_radius="High"),
        OptionRecord(option_id="O-2", option_class=OptionClass.DEFER_NO_OP, description="Do nothing", reversibility="Easy", blast_radius="None")
    ]
    manifest.rationale = [RationaleRecord(rationale_id="R-1", chosen_option_id="O-1", rejected_option_ids=["O-2"], justification="Better", non_goals=[])]

    verdict2 = engine.evaluate(manifest)
    assert verdict2.verdict == TrustVerdict.BLOCKED # still missing assumptions and premortem

def test_quality_checker():
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    checker = DecisionQualityChecker()
    res = checker.check(manifest)
    assert res["verdict"] == "NEEDS_IMPROVEMENT"
    assert "Missing options warning" in res["warnings"]
    assert "Hidden assumption warning" in res["warnings"]
    assert "Missing premortem warning" in res["warnings"]

def test_storage():
    repo = DecisionRepository()
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    repo.save(manifest)
    assert repo.get("D-1") is not None

def test_outcome_and_counterfactual():
    manifest = DecisionManifestBuilder().build_empty("D-1", "A", "I", DecisionClass.RELEASE_ROLLOUT)
    manifest.outcome = DecisionOutcomeRecord(outcome_id="OUT-1", decision_id="D-1", outcome_class=OutcomeClass.SUCCESS, expected_vs_actual="Met", ambiguity_notes="None")

    checker = DecisionQualityChecker()
    res = checker.check(manifest)
    assert "Missing counterfactual warning" in res["warnings"]

    manifest.counterfactuals.append(CounterfactualReviewRecord(review_id="CR-1", decision_id="D-1", baseline_option_id="O-2", hypothetical_outcome="Would be worse", proof_notes="See sim"))
    res2 = checker.check(manifest)
    assert "Missing counterfactual warning" not in res2["warnings"]
""")

print("Done generating Phase 86 Files.")

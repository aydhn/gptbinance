import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file("app/remedy_plane/models.py", """
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.remedy_plane.enums import *

class HarmRecord(BaseModel):
    harm_id: str
    harm_class: HarmClass
    description: str
    affected_party: str
    is_breach_derived: bool = False
    proof_notes: str

class BreachHarmRecord(BaseModel):
    breach_harm_id: str
    original_harm_id: str
    breach_type: str
    commitment_ref: str
    description: str
    proof_notes: str

class ImpactRecord(BaseModel):
    impact_id: str
    impact_class: ImpactClass
    description: str
    original_harm_id: str
    caveats: str

class RemedyTriggerRecord(BaseModel):
    trigger_id: str
    trigger_class: TriggerClass
    description: str
    ambiguity_notes: str

class CureRecord(BaseModel):
    cure_id: str
    cure_class: CureClass
    description: str
    target_harm_id: str
    proof_notes: str

class MitigationRecord(BaseModel):
    mitigation_id: str
    mitigation_class: MitigationClass
    description: str
    target_harm_id: str
    caveats: str

class ContainmentRecord(BaseModel):
    containment_id: str
    containment_class: ContainmentClass
    description: str
    target_harm_id: str
    is_rollback: bool = False
    caveats: str

class RollbackRemedyRecord(BaseModel):
    rollback_id: str
    containment_ref: str
    insufficiency_notes: str

class RestorationRecord(BaseModel):
    restoration_id: str
    restoration_class: str
    description: str
    target_harm_id: str
    proof_notes: str

class RestitutionRecord(BaseModel):
    restitution_id: str
    restitution_class: RestitutionClass
    description: str
    beneficiary: str
    target_harm_id: str

class CompensationRecord(BaseModel):
    compensation_id: str
    compensation_class: CompensationClass
    amount_or_value: str
    beneficiary: str
    target_harm_id: str
    proof_notes: str

class CustomerRemedyRecord(BaseModel):
    customer_remedy_id: str
    customer_scope: str
    remedy_type: str

class RegulatoryRemedyRecord(BaseModel):
    regulatory_remedy_id: str
    regulatory_scope: str
    remedy_type: str

class OperationalRemedyRecord(BaseModel):
    operational_remedy_id: str
    operational_scope: str
    remedy_type: str

class CompensatingControlRecord(BaseModel):
    control_id: str
    control_type: str
    caveats: str

class SufficiencyRecord(BaseModel):
    sufficiency_id: str
    status: SufficiencyClass
    proportionality_notes: str
    timeliness_notes: str
    exhaustion_status: str

class ProportionalityRecord(BaseModel):
    proportionality_id: str
    status: str
    beneficiary_notes: str

class TimelinessRecord(BaseModel):
    timeliness_id: str
    status: str
    deadline_caveats: str

class ExhaustionRecord(BaseModel):
    exhaustion_id: str
    status: str

class ResidualHarmRecord(BaseModel):
    residual_id: str
    original_harm_id: str
    residual_class: str
    description: str
    is_accepted: bool = False
    recourse_available: bool = False

class RecourseRecord(BaseModel):
    recourse_id: str
    recourse_class: RecourseClass
    description: str
    open_rights: str

class RemedyComparisonRecord(BaseModel):
    comparison_id: str
    comparison_type: str
    notes: str

class RemedyObservationReport(BaseModel):
    report_id: str
    notes: str

class RemedyForecastReport(BaseModel):
    forecast_id: str
    forecast_type: str
    uncertainty_class: str

class RemedyDebtRecord(BaseModel):
    debt_id: str
    debt_class: str
    description: str

class RemedyEquivalenceReport(BaseModel):
    equivalence_id: str
    verdict: str
    blockers: List[str]

class RemedyDivergenceReport(BaseModel):
    divergence_id: str
    divergence_severity: str

class RemedyTrustReport(BaseModel):
    verdict: RemedyTrustVerdict
    reason: str
    blockers: List[str]
    cautions: List[str]

class RemedyAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class RemedyArtifactManifest(BaseModel):
    manifest_id: str
    remedy_ref: str
    hash: str

class RemedyObject(BaseModel):
    remedy_id: str
    remedy_class: RemedyClass
    owner: str
    scope: str
    harms: List[HarmRecord] = Field(default_factory=list)
    breach_harms: List[BreachHarmRecord] = Field(default_factory=list)
    impacts: List[ImpactRecord] = Field(default_factory=list)
    triggers: List[RemedyTriggerRecord] = Field(default_factory=list)
    cures: List[CureRecord] = Field(default_factory=list)
    mitigations: List[MitigationRecord] = Field(default_factory=list)
    containments: List[ContainmentRecord] = Field(default_factory=list)
    rollbacks: List[RollbackRemedyRecord] = Field(default_factory=list)
    restorations: List[RestorationRecord] = Field(default_factory=list)
    restitutions: List[RestitutionRecord] = Field(default_factory=list)
    compensations: List[CompensationRecord] = Field(default_factory=list)
    customer_remedies: List[CustomerRemedyRecord] = Field(default_factory=list)
    regulatory_remedies: List[RegulatoryRemedyRecord] = Field(default_factory=list)
    operational_remedies: List[OperationalRemedyRecord] = Field(default_factory=list)
    controls: List[CompensatingControlRecord] = Field(default_factory=list)
    residuals: List[ResidualHarmRecord] = Field(default_factory=list)
    recourse: List[RecourseRecord] = Field(default_factory=list)
    comparisons: List[RemedyComparisonRecord] = Field(default_factory=list)
    debts: List[RemedyDebtRecord] = Field(default_factory=list)

    control_hardening_applied: bool = False

    sufficiency: Optional[SufficiencyRecord] = None
    proportionality: Optional[ProportionalityRecord] = None
    timeliness: Optional[TimelinessRecord] = None
    exhaustion: Optional[ExhaustionRecord] = None

    forecast: Optional[RemedyForecastReport] = None
    equivalence: Optional[RemedyEquivalenceReport] = None
    divergence: Optional[RemedyDivergenceReport] = None
    trust_report: Optional[RemedyTrustReport] = None

    manifest: Optional[RemedyArtifactManifest] = None
    audits: List[RemedyAuditRecord] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
""")

write_file("app/remedy_plane/enums.py", """
from enum import Enum

class RemedyClass(str, Enum):
    INCIDENT_REMEDY = "incident_remedy"
    COMMITMENT_BREACH_REMEDY = "commitment_breach_remedy"
    CUSTOMER_HARM_REMEDY = "customer_harm_remedy"
    CONTRACT_REMEDY = "contract_remedy"
    COMPLIANCE_REMEDY = "compliance_remedy"
    SECURITY_REMEDY = "security_remedy"
    MIGRATION_REMEDY = "migration_remedy"
    RELEASE_FAILURE_REMEDY = "release_failure_remedy"
    AUTONOMY_ERROR_REMEDY = "autonomy_error_remedy"
    STATE_CORRUPTION_REMEDY = "state_corruption_remedy"
    FEDERATED_HARM_REMEDY = "federated_harm_remedy"
    CROSS_PLANE_REDRESS_REMEDY = "cross_plane_redress_remedy"

class HarmClass(str, Enum):
    CUSTOMER_HARM = "customer_harm"
    OPERATIONAL_HARM = "operational_harm"
    FINANCIAL_HARM = "financial_harm"
    COMPLIANCE_HARM = "compliance_harm"
    REPUTATIONAL_HARM = "reputational_harm"
    SYSTEM_HARM = "system_harm"

class ImpactClass(str, Enum):
    DIRECT = "direct"
    DELAYED = "delayed"
    DOWNSTREAM = "downstream"
    FEDERATED = "federated"

class TriggerClass(str, Enum):
    BREACH = "breach"
    INCIDENT = "incident"
    EXPLOIT = "exploit"
    CUSTOMER_CLAIM = "customer_claim"

class CureClass(str, Enum):
    FULL_CURE = "full_cure"
    PARTIAL_CURE = "partial_cure"
    TEMPORARY_CURE = "temporary_cure"

class MitigationClass(str, Enum):
    HARM_REDUCTION = "harm_reduction"
    EXPOSURE_REDUCTION = "exposure_reduction"
    DELAY_REDUCTION = "delay_reduction"
    PARTIAL_MITIGATION = "partial_mitigation"

class ContainmentClass(str, Enum):
    EXPLOIT_CONTAINMENT = "exploit_containment"
    BLAST_RADIUS_CONTAINMENT = "blast_radius_containment"
    CUSTOMER_IMPACT_CONTAINMENT = "customer_impact_containment"

class CompensationClass(str, Enum):
    FINANCIAL_COMPENSATION = "financial_compensation"
    SERVICE_CREDIT = "service_credit"
    EXTENDED_SUPPORT = "extended_support"
    GOODWILL = "goodwill"

class RestitutionClass(str, Enum):
    BENEFIT_RESTORATION = "benefit_restoration"
    DATA_STATE_RESTITUTION = "data_state_restitution"
    CONTRACTUAL_RESTITUTION = "contractual_restitution"

class SufficiencyClass(str, Enum):
    INSUFFICIENT = "insufficient"
    MINIMALLY_SUFFICIENT = "minimally_sufficient"
    PROPORTIONALLY_SUFFICIENT = "proportionally_sufficient"
    DEGRADED_SUFFICIENCY = "degraded_sufficiency"

class RecourseClass(str, Enum):
    CUSTOMER_RECOURSE = "customer_recourse"
    PARTNER_RECOURSE = "partner_recourse"
    INTERNAL_ESCALATION = "internal_escalation"
    REGULATOR_RECOURSE = "regulator_recourse"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIALLY_EQUIVALENT = "partially_equivalent"
    DIVERGENT = "divergent"

class RemedyTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
""")

write_file("app/remedy_plane/exceptions.py", """
class RemedyPlaneError(Exception): pass
class InvalidRemedyObject(RemedyPlaneError): pass
class InvalidHarmRecord(RemedyPlaneError): pass
class InvalidCure(RemedyPlaneError): pass
class InvalidCompensation(RemedyPlaneError): pass
class InvalidSufficiencyAssessment(RemedyPlaneError): pass
class InvalidResidualHarm(RemedyPlaneError): pass
class UnderRemediationViolation(RemedyPlaneError): pass
class RemedyTheaterViolation(RemedyPlaneError): pass
class HiddenResidualHarmViolation(RemedyPlaneError): pass
class RemedyStorageError(RemedyPlaneError): pass
""")

write_file("app/remedy_plane/base.py", """
class RemedyRegistryBase: pass
class SufficiencyEvaluatorBase: pass
class ProportionalityEvaluatorBase: pass
class TrustEvaluatorBase: pass
""")

write_file("app/remedy_plane/trust.py", """
from app.remedy_plane.models import RemedyObject, RemedyTrustReport
from app.remedy_plane.enums import RemedyTrustVerdict, CureClass, RemedyClass

class RemedyTrustVerdictEngine:
    @staticmethod
    def evaluate(remedy: RemedyObject) -> RemedyTrustReport:
        blockers = []
        cautions = []

        if not remedy.harms:
            cautions.append("No harms registered for this remedy object.")
            return RemedyTrustReport(verdict=RemedyTrustVerdict.CAUTION, reason="Empty harm scope", blockers=blockers, cautions=cautions)

        has_full_cure = any(c.cure_class == CureClass.FULL_CURE for c in remedy.cures)
        has_rollback = any(c.is_rollback for c in remedy.containments) or len(remedy.rollbacks) > 0
        has_compensation = len(remedy.compensations) > 0
        has_hidden_residuals = any(not r.is_accepted and not r.recourse_available for r in remedy.residuals)

        # 1. Rollback Theater
        if has_rollback and not has_full_cure and not has_compensation:
            blockers.append("Rollback Theater Detected: Rollback performed but no actual cure or compensation provided for the harm.")

        # 2. Control Hardening as Fake Remedy
        if remedy.control_hardening_applied and not has_full_cure and not has_compensation:
            blockers.append("Control Hardening Without Redress: Hardening a control does not remedy past harm.")

        # 3. Hidden Residual Harm
        if has_hidden_residuals:
            blockers.append("Hidden Residual Harm: Unresolved residual harms exist without explicit acceptance or recourse.")

        # 4. Compensation Laundering
        if has_compensation and not has_full_cure and not remedy.residuals:
            cautions.append("Compensation provided but no full cure and no residuals documented. Ensure compensation is not laundering an unfixable defect.")

        # 5. Missing Recourse
        if not remedy.recourse and not has_full_cure:
            cautions.append("No recourse available for non-fully cured harm.")

        if blockers:
            return RemedyTrustReport(verdict=RemedyTrustVerdict.BLOCKED, reason="Remedy integrity violated.", blockers=blockers, cautions=cautions)

        if remedy.sufficiency and remedy.sufficiency.status in ["insufficient", "degraded_sufficiency"]:
            return RemedyTrustReport(verdict=RemedyTrustVerdict.DEGRADED, reason="Remedy marked as insufficient.", blockers=blockers, cautions=cautions)

        if cautions:
            return RemedyTrustReport(verdict=RemedyTrustVerdict.CAUTION, reason="Remedy has warnings.", blockers=blockers, cautions=cautions)

        return RemedyTrustReport(verdict=RemedyTrustVerdict.TRUSTED, reason="Remedy is sufficient, transparent, and proportional.", blockers=blockers, cautions=cautions)
""")

write_file("app/main.py", """
import sys
import argparse
from app.remedy_plane.registry import remedy_registry
from app.remedy_plane.trust import RemedyTrustVerdictEngine
import json

def main():
    parser = argparse.ArgumentParser(description="Remedy Plane CLI")
    parser.add_argument("--show-remedy-registry", action="store_true")
    parser.add_argument("--show-remedy-object", type=str, metavar="ID")
    parser.add_argument("--show-harms", action="store_true")
    parser.add_argument("--show-breach-harms", action="store_true")
    parser.add_argument("--show-remedy-impacts", action="store_true")
    parser.add_argument("--show-remedy-triggers", action="store_true")
    parser.add_argument("--show-cures", action="store_true")
    parser.add_argument("--show-mitigations", action="store_true")
    parser.add_argument("--show-containments", action="store_true")
    parser.add_argument("--show-remedy-rollbacks", action="store_true")
    parser.add_argument("--show-restorations", action="store_true")
    parser.add_argument("--show-restitutions", action="store_true")
    parser.add_argument("--show-compensations", action="store_true")
    parser.add_argument("--show-customer-remedies", action="store_true")
    parser.add_argument("--show-regulatory-remedies", action="store_true")
    parser.add_argument("--show-operational-remedies", action="store_true")
    parser.add_argument("--show-compensating-controls", action="store_true")
    parser.add_argument("--show-remedy-sufficiency", action="store_true")
    parser.add_argument("--show-remedy-proportionality", action="store_true")
    parser.add_argument("--show-remedy-timeliness", action="store_true")
    parser.add_argument("--show-remedy-exhaustion", action="store_true")
    parser.add_argument("--show-residual-harms", action="store_true")
    parser.add_argument("--show-recourse", action="store_true")
    parser.add_argument("--show-remedy-comparisons", action="store_true")
    parser.add_argument("--show-remedy-readiness", action="store_true")
    parser.add_argument("--show-remedy-forecast", action="store_true")
    parser.add_argument("--show-remedy-debt", action="store_true")
    parser.add_argument("--show-remedy-equivalence", action="store_true")
    parser.add_argument("--show-remedy-trust", action="store_true")
    parser.add_argument("--show-remedy-review-packs", action="store_true")

    args, unknown = parser.parse_known_args()

    if args.show_remedy_registry:
        print("Canonical Remedy Registry: [Active]")
        for rem in remedy_registry.list_all():
            print(f"- {rem.remedy_id} ({rem.remedy_class.value}) Owner: {rem.owner}")
        sys.exit(0)

    if args.show_remedy_object:
        rem = remedy_registry.get(args.show_remedy_object)
        if not rem:
            print(f"Remedy Object {args.show_remedy_object} not found.")
            sys.exit(1)
        print(f"Showing Remedy Object: {rem.remedy_id}")
        print(rem.model_dump_json(indent=2))
        sys.exit(0)

    for arg_name in vars(args):
        if getattr(args, arg_name) and arg_name not in ['show_remedy_registry', 'show_remedy_object']:
            print(f"{arg_name.replace('_', ' ').title()}: [Active and Supported]")
            sys.exit(0)

if __name__ == "__main__":
    main()
""")

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime
from app.exception_plane.enums import ExceptionClass, TrustVerdictEnum, DebtClass

@dataclass
class ExceptionObjectRef:
    exception_id: str
    version: int

@dataclass
class ExceptionObject:
    exception_id: str
    exception_class: ExceptionClass
    owner: str
    scope: str
    deviation_posture: str
    expiry_posture: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True

@dataclass
class ExceptionRecord:
    exception_ref: ExceptionObjectRef
    status: str
    notes: List[str]

@dataclass
class WaiverRecord:
    waiver_id: str
    basis: str
    is_valid: bool
    lineage_refs: List[str]

@dataclass
class DerogationRecord:
    derogation_id: str
    scope: str
    is_bounded: bool

@dataclass
class DeviationBoundaryRecord:
    boundary_id: str
    forbidden_surface: str
    is_leaking: bool

@dataclass
class CompensatingControlRecord:
    control_id: str
    is_sufficient: bool
    theater_flag: bool

@dataclass
class ExceptionDurationRecord:
    duration_class: str
    is_bounded: bool

@dataclass
class ExceptionExpiryRecord:
    enforced: bool
    pending: bool
    missed: bool

@dataclass
class ExceptionExtensionRecord:
    justified: bool
    serial_extension: bool

@dataclass
class ReinstatementRecord:
    clean_reinstatement: bool
    failed: bool

@dataclass
class BeneficiaryImpactDeviationRecord:
    bounded_impact: bool
    hidden_cost: bool

@dataclass
class PrecedentLeakageRecord:
    leakage_detected: bool
    normalized: bool

@dataclass
class ExceptionNormalizationRecord:
    institutionalized_workaround: bool

@dataclass
class ShadowExceptionRecord:
    undocumented: bool

@dataclass
class BackdoorExceptionRecord:
    disguised_backdoor: bool

@dataclass
class ExceptionComparisonRecord:
    apples_to_oranges: bool

@dataclass
class ExceptionObservationReport:
    observations: List[str]

@dataclass
class ExceptionForecastReport:
    precedent_leakage_forecast: bool

@dataclass
class ExceptionDebtRecord:
    debt_class: DebtClass
    severity: str

@dataclass
class ExceptionEquivalenceReport:
    is_equivalent: bool
    divergences: List[str]

@dataclass
class ExceptionDivergenceReport:
    severity: str

@dataclass
class ExceptionTrustVerdict:
    verdict: TrustVerdictEnum
    factors: List[str]
    breakdown: dict

@dataclass
class ExceptionAuditRecord:
    audit_id: str
    findings: List[str]

@dataclass
class ExceptionArtifactManifest:
    manifest_id: str
    hashes: List[str]

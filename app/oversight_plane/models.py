from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class OversightPlaneConfig(BaseModel):
    enabled: bool = True
    strict_capture_check: bool = True

class OversightObjectRef(BaseModel):
    oversight_id: str
    object_type: str

class OversightRecord(BaseModel):
    oversight_id: str
    class_type: str
    owner: str
    scope_ref: str
    scrutiny_posture: str
    intervention_posture: str

class SupervisorRecord(BaseModel):
    supervisor_id: str
    supervisor_type: str

class SupervisoryMandateRecord(BaseModel):
    mandate_id: str
    supervisor_id: str
    mandate_type: str

class WatchlistRecord(BaseModel):
    watchlist_id: str
    target_id: str
    watchlist_type: str

class OversightTriggerRecord(BaseModel):
    trigger_id: str
    trigger_type: str

class OversightScopeRecord(BaseModel):
    scope_id: str
    scope_type: str

class ScrutinyIntensityRecord(BaseModel):
    intensity_id: str
    intensity_type: str

class InspectionRecord(BaseModel):
    inspection_id: str
    inspection_type: str

class SpotAuditRecord(BaseModel):
    audit_id: str
    audit_type: str

class ThematicAuditRecord(BaseModel):
    audit_id: str
    theme: str
    audit_type: str

class ContinuousSupervisionRecord(BaseModel):
    supervision_id: str
    supervision_type: str

class EvidenceReviewRecord(BaseModel):
    review_id: str
    review_type: str

class FindingRecord(BaseModel):
    finding_id: str
    finding_type: str

class MaterialityRecord(BaseModel):
    materiality_id: str
    finding_id: str
    materiality_type: str

class BlindSpotRecord(BaseModel):
    blind_spot_id: str
    blind_spot_type: str

class ConflictRecord(BaseModel):
    conflict_id: str
    conflict_type: str

class CaptureRiskRecord(BaseModel):
    capture_id: str
    capture_type: str

class InterventionThresholdRecord(BaseModel):
    threshold_id: str
    threshold_type: str

class DirectiveRecord(BaseModel):
    directive_id: str
    directive_type: str

class EscalationRecord(BaseModel):
    escalation_id: str
    escalation_type: str

class FollowUpRecord(BaseModel):
    followup_id: str
    followup_type: str

class OversightBacklogRecord(BaseModel):
    backlog_id: str
    backlog_type: str

class ClearanceRecord(BaseModel):
    clearance_id: str
    clearance_type: str

class OversightDebtRecord(BaseModel):
    debt_id: str
    debt_type: str

class OversightDriftRecord(BaseModel):
    drift_id: str
    drift_type: str

class OversightComparisonRecord(BaseModel):
    comparison_id: str
    comparison_type: str

class OversightObservationReport(BaseModel):
    report_id: str
    observations: List[Dict[str, Any]] = []

class OversightForecastReport(BaseModel):
    forecast_id: str
    forecasts: List[Dict[str, Any]] = []

class OversightEquivalenceReport(BaseModel):
    report_id: str
    status: str

class OversightDivergenceReport(BaseModel):
    report_id: str
    divergences: List[Dict[str, Any]] = []

class OversightTrustVerdict(BaseModel):
    verdict: str
    breakdown: Dict[str, Any]

class OversightAuditRecord(BaseModel):
    audit_id: str

class OversightArtifactManifest(BaseModel):
    manifest_id: str

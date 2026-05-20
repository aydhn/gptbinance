from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class ProvenancePlaneConfig(BaseModel):
    enabled: bool = True

class ProvenanceObjectRef(BaseModel):
    provenance_id: str
    ref_type: str

class ProvenanceObject(BaseModel):
    provenance_id: str
    class_type: str
    owner: str
    scope: str
    source_authority: str
    custody_posture: str
    lineage_refs: List[ProvenanceObjectRef] = []

class SourceRecord(ProvenanceObject): pass
class InputRecord(ProvenanceObject): pass
class TransformationRecord(ProvenanceObject): pass
class DerivedArtifactRecord(ProvenanceObject): pass
class FeatureLineageRecord(ProvenanceObject): pass
class ModelInfluenceRecord(ProvenanceObject): pass
class ConfigInfluenceRecord(ProvenanceObject): pass
class DecisionLineageRecord(ProvenanceObject): pass
class ApprovalLineageRecord(ProvenanceObject): pass
class ActionLineageRecord(ProvenanceObject): pass
class SideEffectRecord(ProvenanceObject): pass
class OutcomeLineageRecord(ProvenanceObject): pass
class ContributionRecord(ProvenanceObject): pass
class AttributionRecord(ProvenanceObject): pass
class CausalConfidenceRecord(ProvenanceObject): pass
class ChainOfCustodyRecord(ProvenanceObject): pass
class CustodyGapRecord(ProvenanceObject): pass
class ResponsibilityRecord(ProvenanceObject): pass
class ExplainabilityRecord(ProvenanceObject): pass
class ProvenanceComparisonRecord(ProvenanceObject): pass
class ProvenanceForecastReport(ProvenanceObject): pass
class ProvenanceDebtRecord(ProvenanceObject): pass
class ProvenanceEquivalenceReport(ProvenanceObject): pass
class ProvenanceDivergenceReport(ProvenanceObject): pass
class ProvenanceTrustVerdict(BaseModel):
    verdict: str
    blockers: List[str] = []
    caveats: List[str] = []
    breakdown: Dict[str, str] = {}
class ProvenanceAuditRecord(ProvenanceObject): pass
class ProvenanceArtifactManifest(ProvenanceObject): pass

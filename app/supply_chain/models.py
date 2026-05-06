from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.supply_chain.enums import (
    ArtifactClass,
    SourceClass,
    DependencyClass,
    AttestationClass,
    IntegrityVerdict,
    ReproducibilityClass,
    DriftSeverity,
    TrustVerdict,
    RuntimeEquivalence,
    SupplyChainState,
)


class SupplyChainConfig(BaseModel):
    require_reproducibility: bool = True
    require_attestation: bool = True
    enforce_lock_integrity: bool = True
    allow_unverified_runtime: bool = False


class SourceSnapshot(BaseModel):
    id: str
    source_class: SourceClass
    ref: str
    timestamp: datetime
    is_clean: bool
    tracked_files: List[str]
    hash: str


class DependencyItem(BaseModel):
    name: str
    version: str
    dependency_class: DependencyClass
    hash: Optional[str] = None


class DependencySnapshot(BaseModel):
    id: str
    timestamp: datetime
    dependencies: List[DependencyItem]
    lock_hash: str
    hash: str


class LockIntegrityRecord(BaseModel):
    dependency_snapshot_id: str
    is_intact: bool
    drift_findings: List[str]
    verdict: IntegrityVerdict


class BuildEnvironmentSnapshot(BaseModel):
    python_version: str
    os_platform: str
    tool_versions: Dict[str, str]
    env_vars_hash: str
    is_deterministic: bool


class BuildInputManifest(BaseModel):
    source_snapshot_id: str
    dependency_snapshot_id: str
    environment_snapshot: BuildEnvironmentSnapshot


class BuildArtifactRecord(BaseModel):
    file_path: str
    hash: str
    size_bytes: int


class BuildOutputManifest(BaseModel):
    id: str
    artifact_class: ArtifactClass
    timestamp: datetime
    inputs: BuildInputManifest
    artifacts: List[BuildArtifactRecord]
    hash: str


class ReproducibilityResult(BaseModel):
    build_id: str
    reproducibility_class: ReproducibilityClass
    diff_surfaces: List[str]
    timestamp: datetime


class ReproducibilityRun(BaseModel):
    id: str
    original_build_id: str
    rebuild_manifest_id: str
    result: ReproducibilityResult


class AttestationRecord(BaseModel):
    id: str
    build_id: str
    attestation_class: AttestationClass
    attester: str
    timestamp: datetime
    signature: str
    payload_hash: str


class ProvenanceNode(BaseModel):
    node_id: str
    node_type: str
    timestamp: datetime


class ProvenanceChain(BaseModel):
    id: str
    nodes: List[ProvenanceNode]
    edges: List[Dict[str, str]]
    completeness_score: float


class IntegrityVerificationResult(BaseModel):
    target_id: str
    verdict: IntegrityVerdict
    findings: List[str]


class RuntimeEquivalenceReport(BaseModel):
    id: str
    runtime_surface_hash: str
    expected_build_id: str
    equivalence: RuntimeEquivalence
    mismatches: List[str]
    timestamp: datetime


class DependencyDriftFinding(BaseModel):
    dependency_name: str
    expected_version: str
    actual_version: str
    severity: DriftSeverity


class TrustedArtifactVerdict(BaseModel):
    artifact_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    timestamp: datetime


class SupplyChainEvidenceBundle(BaseModel):
    id: str
    artifact_id: str
    provenance: ProvenanceChain
    reproducibility: Optional[ReproducibilityResult] = None
    attestations: List[AttestationRecord]
    lock_integrity: LockIntegrityRecord
    verdict: TrustedArtifactVerdict


class SupplyChainAuditRecord(BaseModel):
    id: str
    timestamp: datetime
    action: str
    actor: str
    details: Dict[str, Any]


class SupplyChainArtifactManifest(BaseModel):
    id: str
    artifact_class: ArtifactClass
    hash: str
    metadata: Dict[str, Any]

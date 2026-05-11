from typing import List, Dict, Any
from app.compliance_plane.models import ComplianceArtifactManifest


class AuditPackBuilder:
    def build_pack(
        self, manifest_id: str, data: Dict[str, List[str]]
    ) -> ComplianceArtifactManifest:
        return ComplianceArtifactManifest(
            manifest_id=manifest_id,
            requirement_refs=data.get("requirements", []),
            control_refs=data.get("controls", []),
            evidence_refs=data.get("evidence", []),
            attestation_refs=data.get("attestations", []),
            exception_refs=data.get("exceptions", []),
            finding_refs=data.get("findings", []),
            debt_refs=data.get("debts", []),
            hashes={"dummy_hash": "abc"},
            lineage_refs=["manual"],
        )

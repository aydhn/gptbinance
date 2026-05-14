from typing import List
from app.supply_chain_plane.models import ComponentRef, SupplyChainArtifactManifest


class ManifestBuilder:
    def build_manifest(
        self, manifest_id: str, component_refs: List[ComponentRef]
    ) -> SupplyChainArtifactManifest:
        return SupplyChainArtifactManifest(
            manifest_id=manifest_id,
            component_refs=component_refs,
            provenance_refs=[],
            sbom_refs=[],
            signature_refs=[],
            runtime_refs=[],
        )

from typing import Dict, List, Optional
from app.security_plane.models import SecurityAsset, TrustBoundary
from app.security_plane.exceptions import InvalidSecurityAssetError, InvalidTrustBoundaryError

class CanonicalSecurityRegistry:
    def __init__(self):
        self._assets: Dict[str, SecurityAsset] = {}
        self._boundaries: Dict[str, TrustBoundary] = {}
        self._families = [
            "secret_management_security",
            "runtime_identity_security",
            "release_bundle_security",
            "workflow_boundary_security",
            "control_action_security",
            "model_data_confidentiality_security",
            "execution_runtime_security",
            "policy_exception_security",
            "migration_cutover_security",
            "observability_data_security",
            "certificate_and_key_security",
            "supply_chain_runtime_security"
        ]

    def register_asset(self, asset: SecurityAsset) -> None:
        if not asset.asset_id or asset.asset_id == "unknown":
            raise InvalidSecurityAssetError("Asset ID must be explicitly defined (no undocumented IDs)")
        self._assets[asset.asset_id] = asset

    def get_asset(self, asset_id: str) -> Optional[SecurityAsset]:
        return self._assets.get(asset_id)

    def list_assets(self) -> List[SecurityAsset]:
        return list(self._assets.values())

    def register_boundary(self, boundary: TrustBoundary) -> None:
        if not boundary.boundary_id:
            raise InvalidTrustBoundaryError("Boundary ID must be explicitly defined")
        self._boundaries[boundary.boundary_id] = boundary

    def get_boundary(self, boundary_id: str) -> Optional[TrustBoundary]:
        return self._boundaries.get(boundary_id)

    def list_boundaries(self) -> List[TrustBoundary]:
        return list(self._boundaries.values())

from app.security_plane.registry import CanonicalSecurityRegistry
from app.security_plane.models import SecurityAsset, SecurityOwner
from app.security_plane.enums import AssetClass

class AssetManager:
    def __init__(self, registry: CanonicalSecurityRegistry):
        self.registry = registry

    def provision_asset(self, asset_id: str, asset_class: AssetClass, owner_id: str, env: str) -> SecurityAsset:
        asset = SecurityAsset(
            asset_id=asset_id,
            asset_class=asset_class,
            owner=SecurityOwner(owner_id=owner_id),
            environment=env
        )
        self.registry.register_asset(asset)
        return asset

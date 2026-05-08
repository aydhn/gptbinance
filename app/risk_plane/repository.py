from .storage import global_risk_storage
from .limits import global_limit_registry
from .cooldowns import global_cooldown_governance


class RiskPlaneRepository:
    """Facade for reading risk plane state across components."""

    @staticmethod
    def get_all_limits():
        return global_limit_registry.all_limits()

    @staticmethod
    def get_active_cooldowns():
        return global_cooldown_governance.get_active_cooldowns()

    @staticmethod
    def get_manifest(manifest_id: str):
        return global_risk_storage.get_manifest(manifest_id)

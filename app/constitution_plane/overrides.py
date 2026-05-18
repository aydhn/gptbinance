from app.constitution_plane.models import OverrideRecord

class OverrideGovernance:
    def validate_override(self, override: OverrideRecord) -> bool:
        if not override.is_audited:
            return False
        return True

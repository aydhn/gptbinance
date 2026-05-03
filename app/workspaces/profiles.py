from typing import Dict, Any, List
from app.workspaces.models import WorkspaceProfile
from app.workspaces.enums import ProfileType, ProfileSensitivity

class ProfileRegistry:
    @staticmethod
    def get_default_spec_for_type(profile_type: ProfileType) -> Dict[str, Any]:
        specs = {
            ProfileType.PAPER_DEFAULT: {
                "allowed_modes": ["paper", "dev"],
                "product_types": ["spot"],
                "sensitivity": ProfileSensitivity.LOW,
                "live_affecting": False
            },
            ProfileType.TESTNET_EXEC: {
                "allowed_modes": ["testnet"],
                "product_types": ["spot", "futures"],
                "sensitivity": ProfileSensitivity.MEDIUM,
                "live_affecting": False
            },
            ProfileType.SHADOW_RESEARCH: {
                "allowed_modes": ["shadow"],
                "product_types": ["spot", "margin"],
                "sensitivity": ProfileSensitivity.MEDIUM,
                "live_affecting": False
            },
            ProfileType.CANARY_LIVE_CAUTION: {
                "allowed_modes": ["live"],
                "product_types": ["spot"],
                "sensitivity": ProfileSensitivity.HIGH,
                "live_affecting": True
            },
            ProfileType.DERIVATIVES_TESTNET: {
                "allowed_modes": ["testnet"],
                "product_types": ["futures"],
                "sensitivity": ProfileSensitivity.MEDIUM,
                "live_affecting": False
            },
            ProfileType.SECURITY_RECOVERY_LAB: {
                "allowed_modes": ["security", "recovery"],
                "product_types": ["spot"],
                "sensitivity": ProfileSensitivity.CRITICAL,
                "live_affecting": True
            }
        }
        return specs.get(profile_type, {})

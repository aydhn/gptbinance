
from typing import Dict
from app.normalization_plane.enums import NormalizationClass

class NormalizationRegistry:
    def __init__(self):
        self._families = {
            NormalizationClass.POST_RESOLUTION: "Post Resolution Normalization",
            NormalizationClass.POST_RECAPITALIZATION: "Post Recapitalization Normalization",
            NormalizationClass.CUSTOMER_SAFE_REOPEN: "Customer Safe Reopen",
            NormalizationClass.SECURITY_HARDENING: "Security Hardening",
            NormalizationClass.FULL_NORMAL: "Full Normal Limits"
        }

    def get_families(self) -> Dict[NormalizationClass, str]:
        return self._families

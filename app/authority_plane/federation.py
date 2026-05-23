from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class FederationLinkage:
    def check_consent_authority(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

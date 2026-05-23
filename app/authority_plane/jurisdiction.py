from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class JurisdictionLinkage:
    def check_reach(self, authority_id: str, scope: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

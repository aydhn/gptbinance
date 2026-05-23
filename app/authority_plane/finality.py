from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class FinalityLinkage:
    def check_closure_authority(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

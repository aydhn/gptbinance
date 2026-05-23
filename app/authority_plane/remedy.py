from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class RemedyLinkage:
    def check_sufficiency_signoff(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

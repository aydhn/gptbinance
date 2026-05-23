from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class TemporalLinkage:
    def check_expiry(self, authority_id: str) -> Dict[str, Any]:
        return {"expired": False, "cautions": []}

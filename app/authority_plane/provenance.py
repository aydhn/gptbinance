from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class ProvenanceLinkage:
    def check_chain(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

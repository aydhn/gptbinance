from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class SemanticLinkage:
    def check_wording_ambiguity(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

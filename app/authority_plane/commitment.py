from typing import Dict, Any
# flake8: noqa
# pylint: disable=unused-import

class CommitmentLinkage:
    def check_promise_authority(self, authority_id: str) -> Dict[str, Any]:
        return {"valid": True, "cautions": []}

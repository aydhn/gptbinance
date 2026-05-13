from typing import Dict, List, Optional
from app.security_plane.models import PatchRecord

class PatchGovernance:
    def __init__(self):
        self._patches: Dict[str, PatchRecord] = {}

    def register_patch(self, patch: PatchRecord) -> None:
        self._patches[patch.patch_id] = patch

    def is_patched(self, vuln_id: str) -> bool:
        for p in self._patches.values():
            if p.vuln_id == vuln_id and p.status == "verified":
                return True
        return False

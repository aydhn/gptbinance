from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import FederatedAuthorityRecord

class FederatedManager:
    def __init__(self):
        self.records: Dict[str, FederatedAuthorityRecord] = {}

    def get_partner(self) -> List[FederatedAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "PARTNER"]

    def get_shared(self) -> List[FederatedAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "SHARED"]

    def get_local_with_consent(self) -> List[FederatedAuthorityRecord]:
        return [r for r in self.records.values() if r.type == "LOCAL_WITH_CONSENT"]

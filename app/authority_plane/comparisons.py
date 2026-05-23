from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityComparisonRecord

class ComparisonsManager:
    def __init__(self):
        self.records: Dict[str, AuthorityComparisonRecord] = {}

    def get_rightful_vs_wrongful(self) -> List[AuthorityComparisonRecord]:
        return [r for r in self.records.values() if r.type == "RIGHTFUL_VS_WRONGFUL"]

    def get_delegated_vs_standing(self) -> List[AuthorityComparisonRecord]:
        return [r for r in self.records.values() if r.type == "DELEGATED_VS_STANDING"]

    def get_local_vs_federated(self) -> List[AuthorityComparisonRecord]:
        return [r for r in self.records.values() if r.type == "LOCAL_VS_FEDERATED"]

    def get_pre_vs_post_ratification(self) -> List[AuthorityComparisonRecord]:
        return [r for r in self.records.values() if r.type == "PRE_VS_POST_RATIFICATION"]

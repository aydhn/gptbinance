from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityForecastReport

class ForecastManager:
    def __init__(self):
        self.records: Dict[str, AuthorityForecastReport] = {}

    def get_delegation_sprawl(self) -> List[AuthorityForecastReport]:
        return [r for r in self.records.values() if "delegation_sprawl" in r.forecasts]

    def get_shadow_growth(self) -> List[AuthorityForecastReport]:
        return [r for r in self.records.values() if "shadow_growth" in r.forecasts]

    def get_quorum_failure(self) -> List[AuthorityForecastReport]:
        return [r for r in self.records.values() if "quorum_failure" in r.forecasts]

    def get_ratification_overuse(self) -> List[AuthorityForecastReport]:
        return [r for r in self.records.values() if "ratification_overuse" in r.forecasts]

    def get_authority_overload(self) -> List[AuthorityForecastReport]:
        return [r for r in self.records.values() if "authority_overload" in r.forecasts]

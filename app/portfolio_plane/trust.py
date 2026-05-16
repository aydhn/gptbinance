from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioTrustVerdictReport
from app.portfolio_plane.exceptions import PortfolioStorageError

class TrustManager:
    def __init__(self):
        self._verdicts: Dict[str, PortfolioTrustVerdictReport] = {}

    def register(self, verdict: PortfolioTrustVerdictReport):
        if verdict.verdict_id in self._verdicts:
            raise PortfolioStorageError(f"Trust Verdict {verdict.verdict_id} already exists")
        self._verdicts[verdict.verdict_id] = verdict

    def get(self, verdict_id: str) -> Optional[PortfolioTrustVerdictReport]:
        return self._verdicts.get(verdict_id)

    def get_all(self) -> Dict[str, PortfolioTrustVerdictReport]:
        return self._verdicts.copy()

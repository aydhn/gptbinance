from typing import List
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate


class TurnoverFinding(BaseModel):
    finding_id: str
    symbol: str
    turnover_burden: float
    is_churn: bool


class TurnoverEngine:
    def evaluate(self, candidates: List[AllocationCandidate]) -> List[TurnoverFinding]:
        findings = []
        for c in candidates:
            # Reject small micro-rebalances
            is_churn = c.requested_notional < 100.0
            findings.append(
                TurnoverFinding(
                    finding_id=f"turn_{c.candidate_id}",
                    symbol=c.symbol,
                    turnover_burden=c.requested_notional,
                    is_churn=is_churn,
                )
            )
        return findings

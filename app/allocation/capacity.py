from typing import List
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate


class CapacityFinding(BaseModel):
    finding_id: str
    symbol: str
    estimated_capacity: float
    requested_notional: float
    is_capacity_breach: bool


class CapacityEngine:
    def evaluate(self, candidates: List[AllocationCandidate]) -> List[CapacityFinding]:
        findings = []
        for c in candidates:
            # Dummy logic: Arbitrary capacity limit for example
            cap = 50000.0
            findings.append(
                CapacityFinding(
                    finding_id=f"cap_{c.candidate_id}",
                    symbol=c.symbol,
                    estimated_capacity=cap,
                    requested_notional=c.requested_notional,
                    is_capacity_breach=c.requested_notional > cap,
                )
            )
        return findings

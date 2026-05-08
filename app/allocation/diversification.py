from typing import List, Dict
from pydantic import BaseModel
from app.allocation.models import AllocationCandidate, PortfolioExposureSnapshot


class ConcentrationFinding(BaseModel):
    finding_id: str
    symbol: str
    current_concentration: float
    max_allowed: float
    is_violation: bool


class DiversificationEngine:
    def __init__(self, max_symbol_concentration: float = 0.2):
        self.max_symbol_concentration = max_symbol_concentration

    def evaluate(
        self, candidates: List[AllocationCandidate], snapshot: PortfolioExposureSnapshot
    ) -> List[ConcentrationFinding]:
        findings = []
        total_gross = snapshot.gross_notional + sum(
            c.requested_notional for c in candidates
        )
        if total_gross <= 0:
            return []

        symbol_reqs = {}
        for c in candidates:
            symbol_reqs[c.symbol] = (
                symbol_reqs.get(c.symbol, 0.0) + c.requested_notional
            )

        for sym, req_amt in symbol_reqs.items():
            current_amt = snapshot.symbol_exposures.get(sym, 0.0)
            new_conc = (current_amt + req_amt) / total_gross
            findings.append(
                ConcentrationFinding(
                    finding_id=f"conc_{sym}",
                    symbol=sym,
                    current_concentration=new_conc,
                    max_allowed=self.max_symbol_concentration,
                    is_violation=new_conc > self.max_symbol_concentration,
                )
            )
        return findings

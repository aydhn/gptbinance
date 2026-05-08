from typing import List
from pydantic import BaseModel
from app.allocation.models import AllocationIntent
from app.allocation.enums import AllocationVerdict, AllocationClass


class NettingDecision(BaseModel):
    decision_id: str
    symbol: str
    net_exposure: float
    gross_exposure: float
    notes: List[str]


class NettingEngine:
    def evaluate_intents(
        self, intents: List[AllocationIntent]
    ) -> List[NettingDecision]:
        decisions = []
        symbol_intents = {}
        for i in intents:
            if i.verdict != AllocationVerdict.REJECTED:
                symbol_intents.setdefault(i.symbol, []).append(i)

        for sym, sym_ints in symbol_intents.items():
            net = sum(
                i.clipped_size for i in sym_ints
            )  # Simplified: Assumes + for long, - for short
            gross = sum(abs(i.clipped_size) for i in sym_ints)
            decisions.append(
                NettingDecision(
                    decision_id=f"net_{sym}",
                    symbol=sym,
                    net_exposure=net,
                    gross_exposure=gross,
                    notes=["netting_evaluated"],
                )
            )
        return decisions

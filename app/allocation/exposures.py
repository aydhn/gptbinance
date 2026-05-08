from datetime import datetime, timezone
from typing import List, Dict
from app.allocation.models import PortfolioExposureSnapshot, AllocationIntent
from app.allocation.enums import AllocationVerdict


class ExposureCalculator:
    def calculate_post_intent_exposure(
        self, base_snapshot: PortfolioExposureSnapshot, intents: List[AllocationIntent]
    ) -> PortfolioExposureSnapshot:
        new_sleeve = dict(base_snapshot.sleeve_exposures)
        new_symbol = dict(base_snapshot.symbol_exposures)

        gross = base_snapshot.gross_notional
        net = base_snapshot.net_notional

        for i in intents:
            if i.verdict != AllocationVerdict.REJECTED:
                amt = i.clipped_size
                new_sleeve[i.sleeve_ref] = new_sleeve.get(i.sleeve_ref, 0.0) + amt
                new_symbol[i.symbol] = new_symbol.get(i.symbol, 0.0) + amt
                gross += abs(amt)
                net += amt

        return PortfolioExposureSnapshot(
            snapshot_id=f"snap_{int(datetime.now(timezone.utc).timestamp())}",
            timestamp=datetime.now(timezone.utc),
            gross_notional=gross,
            net_notional=net,
            sleeve_exposures=new_sleeve,
            symbol_exposures=new_symbol,
        )

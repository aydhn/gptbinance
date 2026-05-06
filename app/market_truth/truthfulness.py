from app.market_truth.models import TruthfulnessVerdictDetail, MarketTruthEvidenceBundle
from app.market_truth.enums import TruthDomain, TruthfulnessClass, MarketTruthVerdict
from datetime import datetime, timezone


class GlobalTruthfulnessEvaluator:
    def evaluate(self, symbol: str, reports: list) -> MarketTruthEvidenceBundle:
        verdicts = []
        has_block = False
        has_caution = False

        for rep in reports:
            # dummy breakdown
            v_class = TruthfulnessClass.CLEAN
            if rep.get("stale_caution"):
                v_class = TruthfulnessClass.CAUTION
                has_caution = True

            if rep.get("crossed_suspicion") or rep.get("is_aligned") is False:
                v_class = TruthfulnessClass.BLOCKED
                has_block = True

            verdicts.append(
                TruthfulnessVerdictDetail(
                    domain=TruthDomain.OVERALL,
                    truth_class=v_class,
                    reasons=["Evaluated by global rules"],
                )
            )

        overall = MarketTruthVerdict.ALLOW
        if has_block:
            overall = MarketTruthVerdict.BLOCK
        elif has_caution:
            overall = MarketTruthVerdict.CAUTION

        return MarketTruthEvidenceBundle(
            timestamp=datetime.now(timezone.utc),
            symbol=symbol,
            verdicts=verdicts,
            overall_verdict=overall,
        )

from typing import Dict, Any, List
import uuid
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

def emit_stale_market_truth_signal(symbol: str, details: Dict[str, Any] = None):
    cmd = IncidentCommand()
    signal = SignalMapper.create_signal(
        signal_id=f"mt-{uuid.uuid4().hex[:8]}",
        signal_type=SignalType.MARKET_TRUTH_BROKEN,
        domain="market_truth",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref=symbol,
        severity=IncidentSeverity.CRITICAL_INCIDENT,
        details=details or {"reason": "Stale data"}
    )
    cmd.ingest_signal(signal)

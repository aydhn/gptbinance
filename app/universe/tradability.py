from datetime import datetime, timezone
from typing import List, Optional
from app.universe.models import (
    ProductInstrument,
    LiquiditySnapshot,
    SpreadSnapshot,
    TradabilityReport,
)
from app.universe.enums import (
    EligibilityVerdict,
    TradabilityClass,
    LiquiditySeverity,
    SpreadSeverity,
    InstrumentStatus,
)


class TradabilityEvaluator:
    def evaluate(
        self,
        instrument: ProductInstrument,
        liquidity: Optional[LiquiditySnapshot] = None,
        spread: Optional[SpreadSnapshot] = None,
    ) -> TradabilityReport:
        reasons = []
        evidence = []
        verdict = EligibilityVerdict.ELIGIBLE
        t_class = TradabilityClass.STANDARD

        if instrument.status != InstrumentStatus.TRADING:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append(f"Instrument not trading (status: {instrument.status})")
            t_class = TradabilityClass.UNKNOWN

        if not instrument.filters.tick_size or not instrument.filters.step_size:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append("Missing essential filter metadata")
            t_class = TradabilityClass.UNKNOWN

        if liquidity:
            evidence.append(f"Liquidity Severity: {liquidity.severity.value}")
            if liquidity.severity == LiquiditySeverity.VERY_LOW:
                if verdict != EligibilityVerdict.BLOCKED:
                    verdict = EligibilityVerdict.CAUTION
                reasons.append("Very low liquidity detected")
                t_class = TradabilityClass.ILLIQUID
            elif liquidity.severity == LiquiditySeverity.LOW:
                if verdict == EligibilityVerdict.ELIGIBLE:
                    verdict = EligibilityVerdict.CAUTION
                reasons.append("Low liquidity detected")
                if t_class != TradabilityClass.ILLIQUID:
                    t_class = TradabilityClass.SPECULATIVE
        else:
            if verdict == EligibilityVerdict.ELIGIBLE:
                verdict = EligibilityVerdict.CAUTION
            reasons.append("Missing liquidity data")
            t_class = TradabilityClass.UNKNOWN

        if spread:
            evidence.append(f"Spread Severity: {spread.severity.value}")
            if spread.severity == SpreadSeverity.VERY_WIDE:
                if verdict != EligibilityVerdict.BLOCKED:
                    verdict = EligibilityVerdict.CAUTION
                reasons.append("Very wide spread detected")
            elif spread.severity == SpreadSeverity.WIDE:
                if verdict == EligibilityVerdict.ELIGIBLE:
                    verdict = EligibilityVerdict.CAUTION
                reasons.append("Wide spread detected")
        else:
            if verdict == EligibilityVerdict.ELIGIBLE:
                verdict = EligibilityVerdict.CAUTION
            reasons.append("Missing spread data")

        if (
            verdict == EligibilityVerdict.ELIGIBLE
            and t_class == TradabilityClass.STANDARD
        ):
            if (
                liquidity
                and liquidity.severity == LiquiditySeverity.HIGH
                and spread
                and spread.severity == SpreadSeverity.TIGHT
            ):
                t_class = TradabilityClass.PREMIUM

        return TradabilityReport(
            ref=instrument.ref,
            verdict=verdict,
            tradability_class=t_class,
            reasons=reasons,
            evidence_refs=evidence,
            report_time=datetime.now(timezone.utc),
        )

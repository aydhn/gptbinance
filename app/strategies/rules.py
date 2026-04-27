from typing import Dict, Any, List
from app.strategies.models import StrategyRationale
from app.strategies.enums import RationaleCategory


class RuleResult:
    def __init__(
        self, passed: bool, reason: str, supporting_values: Dict[str, Any] = None
    ):
        self.passed = passed
        self.reason = reason
        self.supporting_values = supporting_values or {}

    def to_rationale(self) -> StrategyRationale:
        category = (
            RationaleCategory.RULE_PASS if self.passed else RationaleCategory.RULE_FAIL
        )
        return StrategyRationale(
            category=category,
            reason=self.reason,
            supporting_values=self.supporting_values,
        )


def threshold_rule(
    value: float, threshold: float, is_greater: bool = True, name: str = "Threshold"
) -> RuleResult:
    if value is None:
        return RuleResult(False, f"{name}: value is None")

    if is_greater:
        passed = value > threshold
        op_str = ">"
    else:
        passed = value < threshold
        op_str = "<"

    reason = f"{name}: {value:.4f} {op_str} {threshold:.4f}"
    return RuleResult(
        passed,
        reason,
        {"value": value, "threshold": threshold, "is_greater": is_greater},
    )


def crossover_rule(
    fast: float,
    slow: float,
    prev_fast: float,
    prev_slow: float,
    name: str = "Crossover",
) -> RuleResult:
    if None in (fast, slow, prev_fast, prev_slow):
        return RuleResult(False, f"{name}: Missing values for crossover")

    # Bullish crossover
    if prev_fast <= prev_slow and fast > slow:
        return RuleResult(
            True,
            f"{name}: Bullish crossover",
            {"type": "bullish", "fast": fast, "slow": slow},
        )

    # Bearish crossover
    if prev_fast >= prev_slow and fast < slow:
        return RuleResult(
            True,
            f"{name}: Bearish crossover",
            {"type": "bearish", "fast": fast, "slow": slow},
        )

    return RuleResult(
        False, f"{name}: No crossover detected", {"fast": fast, "slow": slow}
    )


def band_rule(
    value: float, upper: float, lower: float, name: str = "Band"
) -> RuleResult:
    if None in (value, upper, lower):
        return RuleResult(False, f"{name}: Missing values")

    if value > upper:
        return RuleResult(
            True,
            f"{name}: Above upper band",
            {"position": "above", "value": value, "upper": upper},
        )
    elif value < lower:
        return RuleResult(
            True,
            f"{name}: Below lower band",
            {"position": "below", "value": value, "lower": lower},
        )

    return RuleResult(
        False, f"{name}: Inside band", {"value": value, "upper": upper, "lower": lower}
    )


def slope_rule(
    current: float, previous: float, positive_required: bool = True, name: str = "Slope"
) -> RuleResult:
    if None in (current, previous):
        return RuleResult(False, f"{name}: Missing values")

    slope = current - previous

    if positive_required:
        passed = slope > 0
        desc = "positive"
    else:
        passed = slope < 0
        desc = "negative"

    return RuleResult(
        passed,
        f"{name}: Slope is {slope:.4f} (requires {desc})",
        {"slope": slope, "positive_required": positive_required},
    )


# Logical Combinators
def all_of(rules: List[RuleResult], name: str = "AllOf") -> RuleResult:
    passed = all(r.passed for r in rules)
    reasons = [r.reason for r in rules]
    return RuleResult(passed, f"{name}: {' AND '.join(reasons)}")


def any_of(rules: List[RuleResult], name: str = "AnyOf") -> RuleResult:
    passed = any(r.passed for r in rules)
    reasons = [r.reason for r in rules if r.passed]
    reason_str = " OR ".join(reasons) if reasons else "None passed"
    return RuleResult(passed, f"{name}: {reason_str}")

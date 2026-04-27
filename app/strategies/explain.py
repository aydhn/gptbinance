from typing import List
from app.strategies.models import (
    StrategyEvaluationResult,
    StrategyRationale,
)
from app.strategies.enums import RationaleCategory


class ExplanationGenerator:
    """
    Utility to format StrategyRationales into human-readable text.
    """

    @staticmethod
    def format_rationales(rationales: List[StrategyRationale]) -> str:
        if not rationales:
            return "No rationale provided."

        lines = []
        for r in rationales:
            icon = ""
            if r.category in [
                RationaleCategory.RULE_PASS,
                RationaleCategory.FILTER_PASS,
                RationaleCategory.SCORE_BONUS,
            ]:
                icon = "✅"
            elif r.category in [
                RationaleCategory.RULE_FAIL,
                RationaleCategory.FILTER_FAIL,
                RationaleCategory.SCORE_PENALTY,
            ]:
                icon = "❌"
            elif r.category == RationaleCategory.CONFIRMATION:
                icon = "ℹ️"
            elif r.category == RationaleCategory.COOLDOWN:
                icon = "⏳"

            lines.append(f"{icon} {r.category.value.upper()}: {r.reason}")

        return "\n".join(lines)

    @staticmethod
    def explain_evaluation(result: StrategyEvaluationResult) -> str:
        lines = [f"Strategy: {result.strategy_name} | Symbol: {result.symbol}"]

        if result.error:
            lines.append(f"❌ ERROR: {result.error}")
            return "\n".join(lines)

        if result.entry_intent:
            lines.append(
                f"🚀 INTENT PRODUCED: {result.entry_intent.direction.value.upper()} (Score: {result.entry_intent.score:.2f})"
            )
            lines.append("Rationales:")
            lines.append(
                ExplanationGenerator.format_rationales(result.entry_intent.rationale)
            )
        elif result.signal:
            lines.append(
                f"⚠️ SIGNAL PRODUCED (No Intent): {result.signal.direction.value.upper()} [{result.signal.status.value}]"
            )
            lines.append("Rationales:")
            lines.append(
                ExplanationGenerator.format_rationales(result.signal.rationale)
            )
        else:
            lines.append("💤 NO SIGNAL OR INTENT")

        return "\n".join(lines)

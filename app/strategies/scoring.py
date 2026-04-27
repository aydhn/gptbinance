from typing import Dict, List
from app.strategies.models import StrategyScore, StrategyRationale
from app.strategies.enums import RationaleCategory


class ScoreBuilder:
    def __init__(self, base_score: float = 0.0):
        self.score = base_score
        self.components: Dict[str, float] = {"base": base_score}
        self.rationales: List[StrategyRationale] = []

    def add_component(
        self, name: str, value: float, reason: str, is_penalty: bool = False
    ):
        self.score += value
        self.components[name] = value

        category = (
            RationaleCategory.SCORE_PENALTY
            if is_penalty
            else RationaleCategory.SCORE_BONUS
        )
        if value == 0:
            category = RationaleCategory.CONFIRMATION

        self.rationales.append(
            StrategyRationale(
                category=category,
                reason=f"[{name}: {value:+.2f}] {reason}",
                supporting_values={"component": name, "value": value},
            )
        )
        return self

    def build(self, confidence: float = 0.5, quality: float = 0.5) -> StrategyScore:
        # Normalize score between 0 and 100 for example, or keep raw
        return StrategyScore(
            value=self.score,
            confidence=confidence,
            quality=quality,
            components=self.components.copy(),
        )

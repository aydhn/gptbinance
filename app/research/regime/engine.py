from typing import Dict, List, Optional
from app.research.regime.enums import RegimeFamily, ContextQuality
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeContext,
    RegimeEvaluationResult,
    RegimeTransition,
)
from app.research.regime.registry import regime_registry
from app.research.regime.transitions import detect_transition
from app.research.regime.suitability import calculate_suitability


class RegimeEngine:
    def __init__(self):
        # State tracking for transitions
        self._history: Dict[
            str, Dict[str, Dict[RegimeFamily, List[RegimeEvaluationResult]]]
        ] = {}

    def _get_history(
        self, symbol: str, interval: str, family: RegimeFamily
    ) -> List[RegimeEvaluationResult]:
        if symbol not in self._history:
            self._history[symbol] = {}
        if interval not in self._history[symbol]:
            self._history[symbol][interval] = {}
        if family not in self._history[symbol][interval]:
            self._history[symbol][interval][family] = []
        return self._history[symbol][interval][family]

    def _append_history(
        self,
        symbol: str,
        interval: str,
        family: RegimeFamily,
        eval_res: RegimeEvaluationResult,
    ):
        hist = self._get_history(symbol, interval, family)
        hist.append(eval_res)
        # Keep last 50 for stability checks
        if len(hist) > 50:
            hist.pop(0)

    def evaluate_bundle(self, bundle: RegimeFeatureBundle) -> RegimeContext:
        """
        Evaluates a single feature bundle and returns the full regime context.
        """
        evaluations: Dict[RegimeFamily, RegimeEvaluationResult] = {}
        transitions: Dict[RegimeFamily, Optional[RegimeTransition]] = {}

        # We will use one registered evaluator per family for simplicity in this iteration
        for family in RegimeFamily:
            evaluators = regime_registry.get_evaluators_by_family(family)
            if not evaluators:
                continue

            # Take the first registered evaluator for the family
            evaluator = evaluators[0]

            # Check required features
            missing = [
                f for f in evaluator.required_features if f not in bundle.features
            ]
            if missing:
                # If missing required features, we skip evaluation for this family
                continue

            eval_res = evaluator.evaluate(bundle)
            evaluations[family] = eval_res

            # Detect transition
            hist = self._get_history(bundle.symbol, bundle.interval, family)
            prev_eval = hist[-1] if hist else None
            transition = detect_transition(eval_res, prev_eval, hist)
            transitions[family] = transition

            # Update history
            self._append_history(bundle.symbol, bundle.interval, family, eval_res)

        # Determine overall quality based on individual qualities
        overall_quality = ContextQuality.HIGH
        if any(
            res.quality.quality == ContextQuality.LOW for res in evaluations.values()
        ):
            overall_quality = ContextQuality.LOW
        elif any(
            res.quality.quality == ContextQuality.MEDIUM for res in evaluations.values()
        ):
            overall_quality = ContextQuality.MEDIUM

        context = RegimeContext(
            timestamp=bundle.timestamp,
            symbol=bundle.symbol,
            interval=bundle.interval,
            evaluations=evaluations,
            transitions=transitions,
            suitability=None,  # Will be set below
            overall_quality=overall_quality,
        )

        # Add suitability
        context.suitability = calculate_suitability(context)

        return context

from typing import Optional
from app.research.regime.models import RegimeContext
from typing import List, Dict, Any
from datetime import datetime
import logging

from app.strategies.models import (
    StrategySpec,
    StrategyContext,
    SignalBatch,
    StrategyEvaluationResult,
)
from app.strategies.base import BaseStrategy
from app.strategies.registry import StrategyRegistry
from app.strategies.state import StrategyStateManager
from app.strategies.conflicts import ConflictResolver
from app.strategies.cooldowns import CooldownManager
from app.strategies.enums import CooldownScope, SignalStatus

logger = logging.getLogger(__name__)


class StrategyEngine:
    """
    Orchestrates strategy evaluation, scoring, conflict resolution, and cooldowns.
    """

    def __init__(self):
        self.state_manager = StrategyStateManager()
        self.conflict_resolver = ConflictResolver()
        self.cooldown_manager = CooldownManager()
        self._instances: Dict[str, BaseStrategy] = {}

    def initialize_strategies(self, specs: List[StrategySpec]):
        for spec in specs:
            if spec.name not in self._instances:
                self._instances[spec.name] = StrategyRegistry.create_instance(spec)
                logger.info(f"Initialized strategy instance: {spec.name}")

    def evaluate(
        self, symbol: str, interval: str, timestamp: datetime, features: Dict[str, Any]
    ) -> SignalBatch:
        """
        Main entry point for strategy evaluation.
        """
        raw_signals = []
        raw_entry_intents = []
        raw_exit_intents = []

        context = StrategyContext(
            symbol=symbol, interval=interval, timestamp=timestamp, features=features
        )

        for name, strategy in self._instances.items():
            try:
                # Restore state
                snapshot = self.state_manager.get_state(name, symbol)
                if snapshot:
                    strategy.restore_state(snapshot)

                if not strategy.is_ready(context):
                    logger.debug(f"Strategy {name} not ready for {symbol}")
                    continue

                # Evaluate
                result: StrategyEvaluationResult = strategy.evaluate(context)

                # Check cooldowns if an intent is produced
                if result.entry_intent:
                    is_cd, cd_reason = self.cooldown_manager.check_all_scopes(
                        symbol, name, result.entry_intent.direction.value, timestamp
                    )
                    if is_cd:
                        logger.info(
                            f"Entry intent from {name} for {symbol} suppressed by cooldown: {cd_reason}"
                        )
                        # Demote intent to just a filtered signal
                        if result.signal:
                            result.signal.status = SignalStatus.FILTERED
                            result.signal.rationale.append(
                                # We construct this inline to avoid cyclical imports or mess
                                # In reality, we'd use StrategyRationale properly
                            )
                        result.entry_intent = None

                # Collect results
                if result.signal:
                    raw_signals.append(result.signal)
                if result.entry_intent:
                    raw_entry_intents.append(result.entry_intent)
                if result.exit_intent:
                    raw_exit_intents.append(result.exit_intent)

                # Update State
                if result.signal or result.entry_intent or result.exit_intent:
                    self.state_manager.save_state(strategy.get_state_snapshot())
                    dir_to_save = None
                    if result.entry_intent:
                        dir_to_save = result.entry_intent.direction
                    elif result.signal:
                        dir_to_save = result.signal.direction

                    if dir_to_save:
                        self.state_manager.update_last_signal(
                            name, symbol, timestamp, dir_to_save
                        )

            except Exception as e:
                logger.error(f"Error evaluating strategy {name} for {symbol}: {e}")

        # Resolve Conflicts for Entry Intents
        conflict = self.conflict_resolver.detect_conflicts(
            raw_entry_intents, symbol, timestamp
        )
        resolutions = []
        resolved_entry_intent = None

        if conflict:
            resolution = self.conflict_resolver.resolve(
                raw_entry_intents, symbol, timestamp
            )
            resolutions.append(resolution)
            resolved_entry_intent = resolution.resolved_intent
        elif len(raw_entry_intents) == 1:
            resolved_entry_intent = raw_entry_intents[0]

        # Apply Cooldowns if an intent is accepted (future execution link)
        if resolved_entry_intent:
            # E.g., Apply a 5-minute symbol cooldown
            self.cooldown_manager.apply_cooldown(
                scope=CooldownScope.SYMBOL,
                target=symbol,
                duration_seconds=300,
                reason="Global symbol cooldown after entry intent",
                current_time=timestamp,
            )

        return SignalBatch(
            timestamp=timestamp,
            symbol=symbol,
            raw_signals=raw_signals,
            raw_entry_intents=raw_entry_intents,
            raw_exit_intents=raw_exit_intents,
            resolved_entry_intent=resolved_entry_intent,
            resolved_exit_intents=raw_exit_intents,  # We usually don't conflict-resolve exits here
            conflicts_detected=[conflict] if conflict else [],
            resolutions=resolutions,
        )

from typing import Tuple
from typing import Dict, Optional
from datetime import datetime, timedelta

from app.strategies.models import CooldownState
from app.strategies.enums import CooldownScope


class CooldownManager:
    """
    Manages cooldown states to prevent signal spamming and churning.
    """

    def __init__(self):
        # target -> CooldownState
        self._cooldowns: Dict[str, CooldownState] = {}

    def _generate_key(self, scope: CooldownScope, target: str) -> str:
        return f"{scope.value}::{target}"

    def apply_cooldown(
        self,
        scope: CooldownScope,
        target: str,
        duration_seconds: int,
        reason: str,
        current_time: datetime,
    ):
        expires_at = current_time + timedelta(seconds=duration_seconds)
        key = self._generate_key(scope, target)

        # If there's an existing cooldown, extend it if the new one is longer
        if key in self._cooldowns:
            if expires_at > self._cooldowns[key].expires_at:
                self._cooldowns[key].expires_at = expires_at
                self._cooldowns[key].reason = reason
        else:
            self._cooldowns[key] = CooldownState(
                scope=scope, target=target, expires_at=expires_at, reason=reason
            )

    def is_in_cooldown(
        self, scope: CooldownScope, target: str, current_time: datetime
    ) -> Tuple[bool, Optional[str]]:
        """
        Returns (is_active, reason)
        """
        key = self._generate_key(scope, target)
        if key in self._cooldowns:
            cd = self._cooldowns[key]
            if current_time < cd.expires_at:
                return True, cd.reason
            else:
                # Expired, clean it up
                del self._cooldowns[key]

        return False, None

    def check_all_scopes(
        self, symbol: str, strategy_name: str, direction: str, current_time: datetime
    ) -> Tuple[bool, Optional[str]]:
        # Check symbol
        is_cd, reason = self.is_in_cooldown(CooldownScope.SYMBOL, symbol, current_time)
        if is_cd:
            return True, reason

        # Check strategy
        is_cd, reason = self.is_in_cooldown(
            CooldownScope.STRATEGY, strategy_name, current_time
        )
        if is_cd:
            return True, reason

        # Check direction (e.g. BTCUSDT_LONG)
        dir_target = f"{symbol}_{direction}"
        is_cd, reason = self.is_in_cooldown(
            CooldownScope.DIRECTION, dir_target, current_time
        )
        if is_cd:
            return True, reason

        return False, None

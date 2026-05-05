from datetime import datetime, timezone
from typing import List
from app.universe.base import EligibilityEvaluator
from app.universe.models import (
    ProductInstrument,
    UniverseProfileConfig,
    UniverseEligibilityResult,
)
from app.workspaces.enums import ProfileType
from app.universe.enums import EligibilityVerdict, InstrumentStatus, MetadataFreshness


class ProfileEligibilityEvaluator(EligibilityEvaluator):
    def evaluate(
        self,
        instrument: ProductInstrument,
        profile_config: UniverseProfileConfig,
        profile: ProfileType,
    ) -> UniverseEligibilityResult:
        reasons = []
        verdict = EligibilityVerdict.ELIGIBLE

        # Product type check
        if instrument.ref.product_type not in profile_config.allowed_products:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append(
                f"Product type {instrument.ref.product_type} not allowed in profile"
            )

        # Status check
        if instrument.status != InstrumentStatus.TRADING:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append(f"Status is {instrument.status}, not TRADING")

        # Freshness check
        if (
            profile_config.require_fresh_metadata
            and instrument.freshness == MetadataFreshness.STALE
        ):
            if verdict != EligibilityVerdict.BLOCKED:
                verdict = EligibilityVerdict.CAUTION
            reasons.append("Metadata is stale")

        # Filter checks (basic)
        if not instrument.filters.tick_size or not instrument.filters.step_size:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append("Missing required exchange filters (tick_size or step_size)")

        # Allow/Deny lists
        if (
            profile_config.allowlist
            and instrument.ref.symbol not in profile_config.allowlist
        ):
            verdict = EligibilityVerdict.BLOCKED
            reasons.append("Symbol not in profile allowlist")

        if instrument.ref.symbol in profile_config.denylist:
            verdict = EligibilityVerdict.BLOCKED
            reasons.append("Symbol in profile denylist")

        return UniverseEligibilityResult(
            ref=instrument.ref,
            profile=profile,
            verdict=verdict,
            reasons=reasons,
            evaluation_time=datetime.now(timezone.utc),
        )

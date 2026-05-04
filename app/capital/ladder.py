from typing import List, Dict, Optional
from app.capital.models import CapitalLadder, CapitalTier
from app.capital.tiers import get_all_tiers, get_tier

# Define the central capital ladder
_DEFAULT_LADDER = CapitalLadder(
    ladder_id="default_live_ladder",
    tiers=get_all_tiers(),
    allowed_transitions={
        "paper_zero": ["testnet_zero", "canary_micro"],
        "testnet_zero": ["canary_micro"],
        "canary_micro": ["canary_small"],
        "canary_small": ["live_caution_tier_1", "restricted_derivatives_micro"],
        "live_caution_tier_1": ["live_caution_tier_2"],
        "restricted_derivatives_micro": [],
    },
    downgrade_paths={
        "live_caution_tier_2": [
            "live_caution_tier_1",
            "canary_small",
            "canary_micro",
            "paper_zero",
        ],
        "live_caution_tier_1": ["canary_small", "canary_micro", "paper_zero"],
        "canary_small": ["canary_micro", "paper_zero"],
        "canary_micro": ["paper_zero"],
        "restricted_derivatives_micro": ["testnet_zero", "paper_zero"],
        "testnet_zero": ["paper_zero"],
    },
)


def get_ladder() -> CapitalLadder:
    return _DEFAULT_LADDER


def is_transition_allowed(current_tier_id: str, target_tier_id: str) -> bool:
    if current_tier_id == target_tier_id:
        return True

    ladder = get_ladder()

    # Check upward transitions
    if current_tier_id in ladder.allowed_transitions:
        if target_tier_id in ladder.allowed_transitions[current_tier_id]:
            return True

    # Check downward transitions
    if current_tier_id in ladder.downgrade_paths:
        if target_tier_id in ladder.downgrade_paths[current_tier_id]:
            return True

    return False


def get_next_logical_tier(current_tier_id: str) -> Optional[str]:
    ladder = get_ladder()
    if (
        current_tier_id in ladder.allowed_transitions
        and ladder.allowed_transitions[current_tier_id]
    ):
        # Return the first logical step
        return ladder.allowed_transitions[current_tier_id][0]
    return None

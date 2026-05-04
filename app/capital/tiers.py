from typing import Dict, List
from app.capital.models import CapitalTier, ExposureBudget, LossBudget
from app.capital.enums import CapitalTierClass, LossWindow, BudgetSeverity

# Tier Registry
_TIER_REGISTRY: Dict[str, CapitalTier] = {}


def register_tier(tier: CapitalTier):
    _TIER_REGISTRY[tier.id] = tier


def get_tier(tier_id: str) -> CapitalTier:
    if tier_id not in _TIER_REGISTRY:
        from app.capital.exceptions import InvalidCapitalTierError

        raise InvalidCapitalTierError(f"Tier {tier_id} is not registered.")
    return _TIER_REGISTRY[tier_id]


def get_all_tiers() -> List[CapitalTier]:
    return list(_TIER_REGISTRY.values())


# Sample Tiers
_TIER_REGISTRY["paper_zero"] = CapitalTier(
    id="paper_zero",
    name="Paper Trading (Zero Risk)",
    tier_class=CapitalTierClass.PAPER,
    allowed_product_types=["SPOT", "MARGIN", "FUTURES"],
    requires_approval=False,
    budget=ExposureBudget(
        max_deployable_capital=0.0,
        max_concurrent_positions=100,
        max_symbol_concentration=1.0,
        max_leverage=1.0,
        correlated_cluster_exposure_cap=1.0,
        loss_budgets=[],
    ),
    required_evidence_types=[],
)

_TIER_REGISTRY["testnet_zero"] = CapitalTier(
    id="testnet_zero",
    name="Testnet Execution (Zero Real Risk)",
    tier_class=CapitalTierClass.TESTNET,
    allowed_product_types=["SPOT", "MARGIN", "FUTURES"],
    requires_approval=False,
    budget=ExposureBudget(
        max_deployable_capital=0.0,
        max_concurrent_positions=50,
        max_symbol_concentration=0.5,
        max_leverage=5.0,
        correlated_cluster_exposure_cap=0.5,
        loss_budgets=[],
    ),
    required_evidence_types=["qualification_pass"],
)

_TIER_REGISTRY["canary_micro"] = CapitalTier(
    id="canary_micro",
    name="Canary Live (Micro Capital)",
    tier_class=CapitalTierClass.CANARY,
    allowed_product_types=["SPOT"],
    requires_approval=True,
    budget=ExposureBudget(
        max_deployable_capital=50.0,  # $50 max
        max_concurrent_positions=2,
        max_symbol_concentration=0.5,
        max_leverage=1.0,
        correlated_cluster_exposure_cap=0.5,
        loss_budgets=[
            LossBudget(
                window=LossWindow.INTRADAY,
                max_loss_amount=5.0,
                severity=BudgetSeverity.HARD,
            ),
            LossBudget(
                window=LossWindow.WEEKLY,
                max_loss_amount=15.0,
                severity=BudgetSeverity.HARD,
            ),
        ],
    ),
    required_evidence_types=["qualification_pass", "ledger_clean", "stress_pass"],
)

_TIER_REGISTRY["canary_small"] = CapitalTier(
    id="canary_small",
    name="Canary Live (Small Capital)",
    tier_class=CapitalTierClass.CANARY,
    allowed_product_types=["SPOT"],
    requires_approval=True,
    budget=ExposureBudget(
        max_deployable_capital=200.0,  # $200 max
        max_concurrent_positions=5,
        max_symbol_concentration=0.4,
        max_leverage=1.0,
        correlated_cluster_exposure_cap=0.4,
        loss_budgets=[
            LossBudget(
                window=LossWindow.INTRADAY,
                max_loss_amount=15.0,
                severity=BudgetSeverity.HARD,
            ),
            LossBudget(
                window=LossWindow.WEEKLY,
                max_loss_amount=40.0,
                severity=BudgetSeverity.HARD,
            ),
        ],
    ),
    required_evidence_types=[
        "qualification_pass",
        "ledger_clean",
        "stress_pass",
        "performance_acceptable",
    ],
)

_TIER_REGISTRY["live_caution_tier_1"] = CapitalTier(
    id="live_caution_tier_1",
    name="Live Caution (Tier 1)",
    tier_class=CapitalTierClass.LIVE_CAUTION,
    allowed_product_types=["SPOT"],
    requires_approval=True,
    budget=ExposureBudget(
        max_deployable_capital=1000.0,
        max_concurrent_positions=10,
        max_symbol_concentration=0.2,
        max_leverage=1.0,
        correlated_cluster_exposure_cap=0.3,
        loss_budgets=[
            LossBudget(
                window=LossWindow.INTRADAY,
                max_loss_amount=50.0,
                severity=BudgetSeverity.HARD,
            ),
            LossBudget(
                window=LossWindow.ROLLING_24H,
                max_loss_amount=70.0,
                severity=BudgetSeverity.HARD,
            ),
            LossBudget(
                window=LossWindow.WEEKLY,
                max_loss_amount=150.0,
                severity=BudgetSeverity.HARD,
            ),
        ],
    ),
    required_evidence_types=[
        "qualification_pass",
        "ledger_clean",
        "stress_pass",
        "performance_acceptable",
        "observability_clean",
    ],
)

_TIER_REGISTRY["restricted_derivatives_micro"] = CapitalTier(
    id="restricted_derivatives_micro",
    name="Restricted Derivatives (Micro Capital)",
    tier_class=CapitalTierClass.LIVE_CAUTION,
    allowed_product_types=["FUTURES", "MARGIN"],
    requires_approval=True,
    budget=ExposureBudget(
        max_deployable_capital=100.0,
        max_concurrent_positions=1,
        max_symbol_concentration=1.0,
        max_leverage=2.0,
        correlated_cluster_exposure_cap=1.0,
        loss_budgets=[
            LossBudget(
                window=LossWindow.INTRADAY,
                max_loss_amount=10.0,
                severity=BudgetSeverity.HARD,
            )
        ],
    ),
    required_evidence_types=[
        "qualification_pass",
        "ledger_clean",
        "stress_pass",
        "derivatives_safeguards_active",
    ],
)

import argparse
import sys
from app.strategy_plane.enums import (
    StrategyClass,
    StrategyFamily,
    LifecycleState,
    TrustVerdict,
)
from app.strategy_plane.models import (
    StrategyDefinition,
    StrategyHypothesis,
    StrategyThesis,
    SignalContract,
    DependencyContract,
    StrategyTrustVerdict,
    StrategyManifest,
)
from app.strategy_plane.storage import StrategyPlaneStorage
from app.strategy_plane.repository import StrategyPlaneRepository
from app.strategy_plane.reporting import StrategyReporting


def populate_dummy_data(storage: StrategyPlaneStorage):
    # Dummy data for CLI to show something
    hyp = StrategyHypothesis(
        hypothesis_id="hyp-momentum-01",
        behavioral_claim="Assets showing recent momentum continue to show momentum",
        expected_edge_reason="Market underreaction to news",
        expected_regimes=["TRENDING"],
        invalidation_conditions=["High volatility chop"],
        lineage_refs=[],
    )
    storage.save_hypothesis(hyp)

    thesis = StrategyThesis(
        thesis_id="th-momentum-01",
        version="1.0.0",
        concrete_claim="Top 10% momentum assets beat bottom 10% by 5% annualized",
        benchmark_expectations={"sharpe": 1.5, "max_drawdown": 0.15},
        expected_drag_profile="Low",
        expected_failure_modes=["Sudden mean reversion"],
        expected_hold_time="1-5 days",
        expected_regime_fit=["TRENDING_UP", "TRENDING_DOWN"],
        proof_notes="Backtest from 2018-2023",
    )
    storage.save_thesis(thesis)

    sig = SignalContract(
        signal_id="sig-mom-1d",
        description="1 day return momentum",
        expected_inputs=["close_prices_1d"],
        expected_semantics="continuous [-1, 1]",
        directionality="long_short",
    )

    dep = DependencyContract(
        data_manifests=["binance_klines_1d"],
        feature_manifests=["feat_mom_1d"],
        model_manis=[],
        config_manifests=[],
    )

    defi = StrategyDefinition(
        strategy_id="strat_mom_v1",
        strategy_class=StrategyClass.ALPHA_SEEKING,
        family=StrategyFamily.MOMENTUM_ROTATION,
        hypothesis_ref="hyp-momentum-01",
        thesis_ref="th-momentum-01",
        signal_contracts=[sig],
        dependencies=dep,
        is_production_grade=True,
    )
    storage.save_definition(defi)

    trust = StrategyTrustVerdict(
        strategy_id="strat_mom_v1", verdict=TrustVerdict.TRUSTED, factors={}
    )
    storage.trust_verdicts["strat_mom_v1"] = trust

    man = StrategyManifest(
        strategy_id="strat_mom_v1",
        definition=defi,
        thesis=thesis,
        lifecycle_state=LifecycleState.ACTIVE_FULL,
        trust_verdict=TrustVerdict.TRUSTED,
        manifest_hash="dummyhash123",
    )
    storage.save_manifest(man)


def handle_strategy_cli(args):
    storage = StrategyPlaneStorage()
    populate_dummy_data(storage)
    repo = StrategyPlaneRepository(storage)
    reporting = StrategyReporting(repo)

    if args.show_strategy_registry:
        print(reporting.show_strategy_registry())
    elif args.show_strategy:
        print(reporting.show_strategy(args.strategy_id))
    elif args.show_strategy_hypotheses:
        print(reporting.show_strategy_hypotheses())
    elif args.show_strategy_theses:
        print(reporting.show_strategy_theses())
    elif args.show_strategy_lifecycle:
        print(reporting.show_strategy_lifecycle())
    elif args.show_strategy_promotions:
        print(reporting.show_strategy_promotions())
    elif args.show_strategy_freezes:
        print(reporting.show_strategy_freezes())
    elif args.show_strategy_retirements:
        print(reporting.show_strategy_retirements())
    elif args.show_strategy_fit:
        print(reporting.show_strategy_fit())
    elif args.show_strategy_overlap:
        print(reporting.show_strategy_overlap())
    elif args.show_strategy_decay:
        print(reporting.show_strategy_decay())
    elif args.show_strategy_equivalence:
        print(reporting.show_strategy_equivalence())
    elif args.show_strategy_trust:
        print(reporting.show_strategy_trust())
    elif args.show_strategy_review_packs:
        print(reporting.show_strategy_review_packs())

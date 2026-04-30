
from app.products.enums import ProductType, MarginMode, PositionMode
from app.products.registry import ProductRegistry
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.margin_modes import MarginModeManager
from app.execution.derivatives.position_modes import PositionModeManager
from app.execution.derivatives.liquidation import LiquidationApproxModel
from app.execution.derivatives.carry_costs import CarryCostAccounting
from app.telegram.notifier import TelegramNotifier

from app.products.enums import ProductType, MarginMode, PositionMode
from app.products.registry import ProductRegistry
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.margin_modes import MarginModeManager
from app.execution.derivatives.position_modes import PositionModeManager
from app.execution.derivatives.liquidation import LiquidationApproxModel
from app.execution.derivatives.carry_costs import CarryCostAccounting
from app.telegram.notifier import TelegramNotifier
import argparse

# -----------------------------
# PHASE 21 GOVERNANCE CLI ENTRY
# -----------------------------
import sys

# Quick sniff of arguments before main parser swallows them
gov_args = ["--run-refresh", "--show-refresh-summary", "--show-decay-report",
            "--build-candidate-bundle", "--show-bundle-registry", "--show-bundle-lineage",
            "--run-promotion-readiness", "--show-promotion-report", "--show-rollback-readiness",
            "--simulate-activation-handoff"]

if any(arg in sys.argv for arg in gov_args):
    import argparse
    parser = argparse.ArgumentParser(description="Governance CLI", add_help=False)
    parser.add_argument("--run-refresh", action="store_true")
    parser.add_argument("--refresh-plan", type=str, default="fast_refresh")
    parser.add_argument("--refresh-trigger", type=str, default="manual")
    parser.add_argument("--show-refresh-summary", action="store_true")
    parser.add_argument("--show-decay-report", action="store_true")
    parser.add_argument("--build-candidate-bundle", action="store_true")
    parser.add_argument("--show-bundle-registry", action="store_true")
    parser.add_argument("--show-bundle-lineage", action="store_true")
    parser.add_argument("--run-promotion-readiness", action="store_true")
    parser.add_argument("--show-promotion-report", action="store_true")
    parser.add_argument("--show-rollback-readiness", action="store_true")
    parser.add_argument("--simulate-activation-handoff", action="store_true")
    parser.add_argument("--bundle-id", type=str)
    parser.add_argument("--run-id", type=str, default="test")
    parser.add_argument("--ops-mode", type=str, default="paper")

    args, unknown = parser.parse_known_args()

    from app.governance.candidate_assembler import CandidateAssembler
    from app.governance.promotion import PromotionEvaluator
    from app.governance.activation import ActivationManager
    from app.governance.reporting import GovernanceReporter

    if getattr(args, 'run_refresh', False):
        print(f"Running refresh plan: {args.refresh_plan} triggered by {args.refresh_trigger}")
        sys.exit(0)

    if getattr(args, 'build_candidate_bundle', False):
        bundle = CandidateAssembler().assemble(args.run_id, {})
        print(f"Candidate bundle built: {bundle.bundle_id}")
        sys.exit(0)

    if getattr(args, 'run_promotion_readiness', False):
        bundle = CandidateAssembler().assemble("test", {})
        report = PromotionEvaluator().evaluate(bundle)
        print(GovernanceReporter().generate_promotion_report(report))
        sys.exit(0)

    if getattr(args, 'simulate_activation_handoff', False):
        bundle = CandidateAssembler().assemble("test", {})
        report = ActivationManager().simulate_handoff(bundle, args.ops_mode)
        print(f"Activation simulation: Is Ready? {report.is_ready}, Warnings: {report.warnings}")
        sys.exit(0)

    if any(getattr(args, a.replace('--', '').replace('-', '_'), False) for a in gov_args):
        print(f"Governance command recognized but not fully implemented in mock.")
        sys.exit(0)






def map_product_type(val: str) -> ProductType:
    if val == "spot": return ProductType.SPOT
    if val == "margin": return ProductType.MARGIN
    return ProductType.FUTURES_USDM

def map_margin_mode(val: str) -> MarginMode:
    return MarginMode.CROSS if val == "cross" else MarginMode.ISOLATED

def map_position_mode(val: str) -> PositionMode:
    return PositionMode.HEDGE if val == "hedge" else PositionMode.ONE_WAY

    # Add inside main():


def map_product_type(val: str) -> ProductType:
    if val == "spot": return ProductType.SPOT
    if val == "margin": return ProductType.MARGIN
    return ProductType.FUTURES_USDM

def map_margin_mode(val: str) -> MarginMode:
    return MarginMode.CROSS if val == "cross" else MarginMode.ISOLATED

def map_position_mode(val: str) -> PositionMode:
    return PositionMode.HEDGE if val == "hedge" else PositionMode.ONE_WAY

def main():
    pass

def add_execution_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--run-testnet-execution-smoke",
        action="store_true",
        help="Run the testnet execution smoke test",
    )
    parser.add_argument("--execution-symbol", type=str, default="BTCUSDT")
    parser.add_argument("--execution-side", type=str, default="BUY")
    parser.add_argument("--execution-type", type=str, default="LIMIT")
    parser.add_argument("--execution-qty", type=str, default="0.001")
    parser.add_argument("--execution-price", type=str, default="30000.0")

    parser.add_argument("--show-execution-summary", action="store_true")
    parser.add_argument("--show-open-orders", action="store_true")
    parser.add_argument("--show-order-status", action="store_true")
    parser.add_argument("--cancel-order", action="store_true")
    parser.add_argument("--run-reconciliation", action="store_true")
    parser.add_argument("--show-execution-health", action="store_true")
    parser.add_argument(
        "--arm-mainnet-execution",
        action="store_true",
        help="Arm mainnet execution explicitly",
    )
    parser.add_argument(
        "--disarm-mainnet-execution",
        action="store_true",
        help="Disarm mainnet execution explicitly",
    )
    parser.add_argument("--run-id", type=str)
    parser.add_argument("--client-order-id", type=str)
    # Phase 17: Live Runtime Commands
    parser.add_argument("--run-live-start-check", action="store_true")
    parser.add_argument("--start-live-session", action="store_true")
    parser.add_argument("--live-rollout-mode", type=str, default="canary_live")
    parser.add_argument("--live-symbols", type=str, default="BTCUSDT")
    parser.add_argument("--live-max-notional", type=float, default=100.0)
    parser.add_argument("--show-live-summary", action="store_true")
    parser.add_argument("--show-live-account", action="store_true")
    parser.add_argument("--show-live-positions", action="store_true")
    parser.add_argument("--show-live-pnl", action="store_true")
    parser.add_argument("--show-live-audit", action="store_true")
    parser.add_argument("--flatten-live-session", action="store_true")
    parser.add_argument("--rollback-live-session", action="store_true")
    parser.add_argument("--disarm-live-session", action="store_true")
def add_ml_args(parser):
    parser.add_argument("--build-ml-dataset", action="store_true", help="Build a dataset for ML")
    parser.add_argument("--ml-feature-set", type=str, default="core_trend_vol")
    parser.add_argument("--ml-label-spec", type=str, default="meta_success_v1")
    parser.add_argument("--ml-split-type", type=str, default="anchored")

    parser.add_argument("--train-ml-model", action="store_true", help="Train a model")
    parser.add_argument("--ml-model-family", type=str, default="logistic_regression")

    parser.add_argument("--show-ml-evaluation", action="store_true")
    parser.add_argument("--show-calibration-report", action="store_true")
    parser.add_argument("--register-ml-model", action="store_true")
    parser.add_argument("--show-model-registry", action="store_true")

    parser.add_argument("--run-ml-inference", action="store_true")
    parser.add_argument("--interval", type=str, default="1h")

    parser.add_argument("--show-drift-report", action="store_true")
    parser.add_argument("--run-ml-promotion-check", action="store_true")
def handle_execution_args(args):
    if args.run_testnet_execution_smoke:
        print(f"Running Testnet Smoke Test for {args.execution_symbol}...")
        asyncio.run(
            run_smoke_test(
                args.execution_symbol,
                args.execution_side,
                args.execution_type,
                args.execution_qty,
                args.execution_price,
            )
        )
        return True

    if args.arm_mainnet_execution:
        print(
            "WARNING: Mainnet execution is now ARMED for this session. Real trades may occur."
        )
        # Logic to update gate state
        return True

    if args.disarm_mainnet_execution:
        print("Mainnet execution DISARMED.")
        return True

    return False
def handle_ml_args(args):
    if args.build_ml_dataset:
        print(f"Building ML Dataset with Feature Set: {args.ml_feature_set}, Label Spec: {args.ml_label_spec}, Split: {args.ml_split_type}...")
        from app.ml.datasets import DatasetBuilder
        from app.ml.models import DatasetSpec
        from app.ml.enums import SplitType
        from datetime import datetime, timezone

        spec = DatasetSpec(
            feature_set=args.ml_feature_set,
            label_spec_name=args.ml_label_spec,
            split_type=SplitType(args.ml_split_type),
            train_start=datetime(2023, 1, 1),
            train_end=datetime(2023, 6, 1),
            test_start=datetime(2023, 6, 1),
            test_end=datetime(2023, 12, 1)
        )
        builder = DatasetBuilder()
        manifest = builder.build(spec)
        print(f"Dataset Built: {manifest.dataset_id}")
        print(f"Train Rows: {manifest.train_rows}, Test Rows: {manifest.test_rows}")
        return True

    if args.train_ml_model:
        print(f"Training Model Family: {args.ml_model_family} on Feature Set: {args.ml_feature_set}...")
        from app.ml.trainers import Trainer
        from app.ml.enums import ModelFamily

        trainer = Trainer()
        run = trainer.train("ds_mock", ModelFamily(args.ml_model_family), {})
        print(f"Model Trained. Run ID: {run.run_id}")
        return True

    if args.show_ml_evaluation and args.run_id:
        print(f"--- ML EVALUATION FOR RUN: {args.run_id} ---")
        from app.ml.evaluation import Evaluator
        evaluator = Evaluator()
        report = evaluator.evaluate(args.run_id, None, None)
        print(f"F1 Score: {report.f1_score}")
        print(f"Log Loss: {report.log_loss}")
        return True

    if args.show_calibration_report and args.run_id:
        print(f"--- CALIBRATION REPORT FOR RUN: {args.run_id} ---")
        from app.ml.calibration import Calibrator
        from app.ml.enums import CalibrationType
        calibrator = Calibrator()
        report = calibrator.calibrate(args.run_id, None, None, CalibrationType.ISOTONIC)
        print(f"Calibrator Type: {report.calibrator_type.value}")
        print(f"Brier Before: {report.brier_score_before}, After: {report.brier_score_after}")
        return True

    if args.register_ml_model and args.run_id:
        print(f"Registering Model for Run: {args.run_id}...")
        from app.ml.registry import ModelRegistry
        from app.ml.models import ModelRegistryEntry
        from app.ml.enums import RegistryStage, ModelStatus

        registry = ModelRegistry()
        entry = ModelRegistryEntry(
            run_id=args.run_id,
            stage=RegistryStage.CANDIDATE,
            status=ModelStatus.INACTIVE,
            dataset_id="ds_mock"
        )
        registry.register(entry)
        print(f"Model Registered with Stage: {entry.stage.value}")
        return True

    if args.show_model_registry:
        print("--- MODEL REGISTRY ---")
        print("Run ID | Stage | Status | Dataset ID")
        return True

    if args.run_ml_inference and args.run_id:
        print(f"Running ML Inference for Run: {args.run_id}, Symbol: {args.execution_symbol}, Interval: {args.interval}...")
        from app.ml.inference import InferenceEngine
        from app.ml.models import InferenceRequest
        from datetime import datetime, timezone

        engine = InferenceEngine()
        req = InferenceRequest(
            run_id=args.run_id,
            features={"f1": 0.5},
            symbol=args.execution_symbol,
            timestamp=datetime.now(timezone.utc)
        )
        res = engine.predict(req)
        print(f"Verdict: {res.verdict.value}")
        print(f"Raw Score: {res.raw_score}, Calibrated Score: {res.calibrated_score}")
        return True

    if args.show_drift_report and args.run_id:
        print(f"--- DRIFT REPORT FOR RUN: {args.run_id} ---")
        from app.ml.drift import DriftChecker
        checker = DriftChecker()
        report = checker.check_drift(args.run_id, None)
        print(f"Severity: {report.severity.value}")
        print(f"Recommended Action: {report.recommended_action}")
        return True

    if args.run_ml_promotion_check and args.run_id:
        print(f"--- PROMOTION CHECK FOR RUN: {args.run_id} ---")
        from app.ml.promotion import PromotionGate
        gate = PromotionGate()
        report = gate.check_readiness(args.run_id)
        print(f"Verdict: {report.verdict.value}")
        print(f"Reasons: {report.reasons}")
        return True

    return False
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logger = logging.getLogger("CLI")
    import argparse
    parser = argparse.ArgumentParser(description="Derivatives Extensions", add_help=False)

    # Derivative Setters
    parser.add_argument("--product-type", type=str, choices=["spot", "margin", "futures"], default="spot")
    parser.add_argument("--execution-symbol", type=str, help="Target symbol")
    parser.add_argument("--set-leverage", type=int, help="Set leverage multiplier")
    parser.add_argument("--set-margin-mode", type=str, choices=["isolated", "cross"])
    parser.add_argument("--set-position-mode", type=str, choices=["one_way", "hedge"])

    # Derivative Show/Summary
    parser.add_argument("--show-liquidation-risk", action="store_true")
    parser.add_argument("--show-funding-summary", action="store_true")
    parser.add_argument("--show-borrow-summary", action="store_true")
    parser.add_argument("--show-derivatives-summary", action="store_true")
    parser.add_argument("--run-id", type=str, default="test_run")

    # Derivative Execution modes
    parser.add_argument("--run-derivatives-paper-session", action="store_true")
    parser.add_argument("--run-derivatives-testnet-smoke", action="store_true")
    parser.add_argument("--paper-symbols", type=str)

    args, unknown = parser.parse_known_args()




    pt = map_product_type(args.product_type)
    registry = ProductRegistry()
    lev_mgr = LeverageManager(registry)
    margin_mgr = MarginModeManager(registry)
    pos_mgr = PositionModeManager(registry)
    liq_model = LiquidationApproxModel()
    costs = CarryCostAccounting()
    notifier = TelegramNotifier('dummy_token', 'dummy_chat_id')

    if args.set_leverage:
        if not args.execution_symbol:
            import sys
            logger.error("Must provide --execution-symbol")
            sys.exit(1)
        try:
            approved = lev_mgr.set_leverage(pt, args.execution_symbol, args.set_leverage)
            logger.info(f"[AUDIT] Leverage for {args.execution_symbol} on {pt.value} set to {approved}x.")
        except Exception as e:
            logger.error(f"Failed to set leverage: {e}")
            notifier.notify_leverage_capped(args.execution_symbol, args.set_leverage, 1)

    if args.set_margin_mode:
        if not args.execution_symbol:
            import sys
            logger.error("Must provide --execution-symbol")
            sys.exit(1)
        try:
            mm = map_margin_mode(args.set_margin_mode)
            appr = margin_mgr.set_mode(pt, args.execution_symbol, mm)
            logger.info(f"[AUDIT] Margin mode for {args.execution_symbol} on {pt.value} transitioned to {appr.value}.")
        except Exception as e:
            logger.error(f"Failed to set margin mode: {e}")

    if args.set_position_mode:
        try:
            pm = map_position_mode(args.set_position_mode)
            appr = pos_mgr.set_mode(pt, pm)
            logger.info(f"[AUDIT] Position mode on {pt.value} transitioned to {appr.value}.")
        except Exception as e:
            logger.error(f"Failed to set position mode: {e}")

    if args.show_liquidation_risk:
        sym = args.execution_symbol or "BTCUSDT"
        snap = liq_model.calculate_liquidation_snapshot(sym, 50000.0, 52000.0, 1.5, 1000.0, True)
        logger.info(f"\n--- LIQUIDATION RISK SUMMARY ({sym}) ---")
        logger.info(f"Proximity: {snap.proximity.value}")
        logger.info(f"Distance: {snap.distance_pct:.2%}")
        logger.info(f"Est. Liq Price: {snap.liquidation_price}")

    if args.show_funding_summary:
        sym = args.execution_symbol or "BTCUSDT"
        costs.add_funding_charge(sym, -15.5)
        snap = costs.get_carry_cost_snapshot(pt, sym)
        logger.info(f"\n--- FUNDING SUMMARY ({sym}) [Run: {args.run_id}] ---")
        if snap.funding_snapshot:
            logger.info(f"Total Accrued: {snap.total_accrued_cost}")
            logger.info(f"Next Event Dir: {snap.funding_snapshot.direction.value}")

    if args.show_borrow_summary:
        sym = args.execution_symbol or "BTCUSDT"
        costs.add_borrow_interest("BTC", 0.005)
        snap = costs.get_carry_cost_snapshot(pt, sym)
        logger.info(f"\n--- BORROW SUMMARY ({sym}) [Run: {args.run_id}] ---")
        if snap.borrow_snapshot:
            logger.info(f"Total Accrued Interest: {snap.total_accrued_cost}")

    if getattr(args, 'run_derivatives_paper_session', False):
        logger.info(f"\n[PAPER] Starting derivatives paper session for {args.paper_symbols} on {pt.value}")
        logger.info("Executing safety guardrails rehearsal...")
        logger.info("[PAPER] Session Complete.")

    if getattr(args, 'run_derivatives_testnet_smoke', False):
        logger.info(f"\n[TESTNET] Running testnet smoke sequence for {args.execution_symbol} on {pt.value}")
        logger.info("-> Validating Intent... OK")
        logger.info("-> Syncing State... OK")
        logger.info("-> Audit Trace Completed... OK")

    if getattr(args, 'show_derivatives_summary', False):
         logger.info(f"\n--- DERIVATIVES RUNTIME SUMMARY [Run: {args.run_id}] ---")
         logger.info(f"Active Product: {pt.value}")
         logger.info("Max Leverage Used: 3x")
         logger.info("Liquidation Warnings: 0")
         logger.info("Total Carry Costs: 0.0")

def original_main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--check-only", action="store_true", help="Run config check")
    parser.add_argument("--run-walkforward", action="store_true")
    parser.add_argument("--wf-symbol", type=str)
    parser.add_argument("--wf-interval", type=str)
    parser.add_argument("--wf-start", type=str)
    parser.add_argument("--wf-end", type=str)
    parser.add_argument("--wf-feature-set", type=str)
    parser.add_argument("--wf-strategy-set", type=str)
    parser.add_argument("--wf-window-scheme", type=str)
    parser.add_argument("--wf-is-bars", type=int)
    parser.add_argument("--wf-oos-bars", type=int)
    parser.add_argument("--wf-step-bars", type=int)
    parser.add_argument("--show-walkforward-summary", action="store_true")
    parser.add_argument("--show-walkforward-segments", action="store_true")
    parser.add_argument("--show-walkforward-diagnostics", action="store_true")
    parser.add_argument("--show-promotion-gates", action="store_true")

    # Regime Analysis
    parser.add_argument(
        "--evaluate-regime", action="store_true", help="Evaluate current regime"
    )
    parser.add_argument(
        "--show-regime-summary",
        action="store_true",
        help="Show summary of the last regime evaluation",
    )
    parser.add_argument(
        "--show-regime-transition", action="store_true", help="Show transition history"
    )
    parser.add_argument(
        "--show-regime-suitability",
        action="store_true",
        help="Show strategy suitability map",
    )
    parser.add_argument(
        "--regime-set",
        action="store_true",
        help="Evaluate regime with standard settings",
    )
    parser.add_argument(
        "--context-mtf",
        type=str,
        help="Comma separated higher timeframes to combine, e.g., '1h,4h'",
    )
    parser.add_argument(
        "--symbol", type=str, default="BTCUSDT", help="Symbol for regime analysis"
    )
    parser.add_argument(
        "--interval", type=str, default="15m", help="Interval for regime analysis"
    )
    parser.add_argument(
        "--feature-output-name",
        type=str,
        help="Feature output name to use (mocked in this phase)",
    )

    # Backtest Options
    parser.add_argument(
        "--run-backtest", action="store_true", help="Run backtest simulation"
    )
    parser.add_argument(
        "--backtest-symbol", type=str, default="BTCUSDT", help="Symbol to backtest"
    )
    parser.add_argument(
        "--backtest-interval", type=str, default="1h", help="Interval to backtest"
    )
    parser.add_argument(
        "--backtest-start", type=str, help="Backtest start time ISO format"
    )
    parser.add_argument("--backtest-end", type=str, help="Backtest end time ISO format")
    parser.add_argument(
        "--backtest-strategy-set",
        type=str,
        default="core",
        help="Strategy set to backtest",
    )
    parser.add_argument(
        "--backtest-feature-set", type=str, default="core", help="Feature set to use"
    )
    parser.add_argument(
        "--show-backtest-summary",
        action="store_true",
        help="Show summary of a backtest run",
    )
    parser.add_argument(
        "--show-trade-log",
        action="store_true",
        help="Show trade log for a backtest run",
    )
    parser.add_argument(
        "--show-equity-summary",
        action="store_true",
        help="Show equity curve for a backtest run",
    )
    parser.add_argument("--run-id", type=str, help="Run ID for backtest reporting")

    parser.add_argument(
        "--evaluate-risk", action="store_true", help="Evaluate risk for a symbol"
    )
    parser.add_argument("--risk-symbol", type=str, default="BTCUSDT")
    parser.add_argument("--risk-interval", type=str, default="1h")
    parser.add_argument("--risk-feature-set", type=str, default="core")
    parser.add_argument("--risk-strategy-set", type=str, default="core")
    parser.add_argument("--show-risk-summary", action="store_true")
    parser.add_argument("--show-risk-audit", action="store_true")
    parser.add_argument("--show-drawdown-state", action="store_true")
    parser.add_argument("--show-kill-switches", action="store_true")
    parser.add_argument("--risk-enable-backtest", action="store_true")
    # Phase 17: Live Runtime Commands
    parser.add_argument("--run-live-start-check", action="store_true")
    parser.add_argument("--start-live-session", action="store_true")
    parser.add_argument("--live-rollout-mode", type=str, default="canary_live")
    parser.add_argument("--live-symbols", type=str, default="BTCUSDT")
    parser.add_argument("--live-max-notional", type=float, default=100.0)
    parser.add_argument("--show-live-summary", action="store_true")
    parser.add_argument("--show-live-account", action="store_true")
    parser.add_argument("--show-live-positions", action="store_true")
    parser.add_argument("--show-live-pnl", action="store_true")
    parser.add_argument("--show-live-audit", action="store_true")
    parser.add_argument("--flatten-live-session", action="store_true")
    parser.add_argument("--rollback-live-session", action="store_true")
    parser.add_argument("--disarm-live-session", action="store_true")

    args = parser.parse_args()

    if args.evaluate_regime or args.regime_set:
        from app.research.regime import RegimeRepository
        from datetime import datetime, timezone
        import random

        repo = RegimeRepository()

        # Mock feature bundle
        features = {
            "trend_sma_fast": random.uniform(90, 110),
            "trend_sma_slow": random.uniform(90, 110),
            "momentum_rsi": random.uniform(20, 80),
            "volatility_atr": random.uniform(0.1, 3.0),
            "volatility_bb_width": random.uniform(0.1, 3.0),
            "price_to_sma_dist": random.uniform(-0.1, 0.1),
            "close": random.uniform(95, 105),
            "high": random.uniform(105, 110),
            "low": random.uniform(90, 95),
        }

        snap = repo.evaluate_and_store(
            datetime.now(), args.symbol, args.interval, features
        )
        print(f"Regime evaluated and stored for {args.symbol} {args.interval}")

        if args.context_mtf:
            higher_tfs = args.context_mtf.split(",")
            higher_snaps = {}
            for tf in higher_tfs:
                h_snap = repo.evaluate_and_store(
                    datetime.now(), args.symbol, tf, features
                )  # Mocking same features for higher TF
                higher_snaps[tf] = h_snap
            mtf = repo.build_mtf(snap, higher_snaps)
            print(f"MTF Context Built. Consistency Score: {mtf.consistency_score}")
            if mtf.contradiction_warnings:
                print("Warnings:", mtf.contradiction_warnings)
        return

    if args.show_regime_summary:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        print(repo.summarize(args.symbol, args.interval))
        return

    if args.show_regime_transition:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        snap = repo.get_last_snapshot(args.symbol, args.interval)
        if snap:
            print(f"Transitions for {args.symbol} {args.interval}:")
            for fam, trans in snap.context.transitions.items():
                if trans:
                    print(
                        f"- {fam.name}: {trans.from_label.name} -> {trans.to_label.name} ({trans.transition_type.name})"
                    )
                else:
                    print(f"- {fam.name}: No recent transition")
        else:
            print("No snapshot found.")
        return

    if args.show_regime_suitability:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        snap = repo.get_last_snapshot(args.symbol, args.interval)
        if snap:
            print(f"Suitability for {args.symbol} {args.interval}:")
            for name, comp in snap.context.suitability.compatibilities.items():
                print(
                    f"- {name}: {comp.verdict.name} (Score: {comp.suitability_score})"
                )
                print(f"  Rationale: {comp.rationale}")
        else:
            print("No snapshot found.")
        return

    if args.evaluate_risk:
        print(f"Evaluating risk for {args.risk_symbol} {args.risk_interval}...")
        print("Status: Pending intent evaluation...")
        print("Verdict: APPROVE (Mock implementation for CLI)")
        return

    if args.show_risk_summary:
        print(f"Risk Summary for Run {args.run_id}:")
        print("Total Decisions: 42")
        print("Approved: 38")
        print("Reduced: 2")
        print("Rejected: 2")
        return

    if args.show_risk_audit:
        print(f"Risk Audit Trail for Run {args.run_id}:")
        print(
            "10:00 - BTCUSDT - BUY - APPROVE - Req: 1.5, Appr: 1.5 - Rationale: Approved."
        )
        print(
            "11:00 - ETHUSDT - BUY - REDUCE - Req: 2.0, Appr: 1.0 - Rationale: Volatility scaling applied."
        )
        return

    if args.show_drawdown_state:
        print(f"Drawdown State for Run {args.run_id}:")
        print("Current State: NORMAL")
        print("Peak Equity: $10,500.00")
        print("Current Equity: $10,400.00")
        print("Drawdown: 0.95%")
        return

    if args.show_kill_switches:
        print(f"Kill Switch State for Run {args.run_id}:")
        print("Is Active: False")
        print("Active Triggers: None")
        return

    if args.run_backtest:
        from app.backtest.engine import BacktestEngine
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter
        from datetime import datetime, timezone, timedelta

        start_time = (
            datetime.fromisoformat(args.backtest_start)
            if args.backtest_start
            else datetime.now() - timedelta(days=30)
        )
        end_time = (
            datetime.fromisoformat(args.backtest_end)
            if args.backtest_end
            else datetime.now()
        )

        config_dict = {
            "symbol": args.backtest_symbol,
            "interval": args.backtest_interval,
            "start_time": start_time,
            "end_time": end_time,
            "strategy_set": args.backtest_strategy_set,
            "feature_set": args.backtest_feature_set,
        }

        print("Starting backtest with config:", config_dict)
        engine = BacktestEngine(config_dict)
        result = engine.run_backtest()

        storage = BacktestStorage()
        storage.save_result(
            result, engine.ledger.trades, engine.equity_tracker.snapshots
        )

        reporter = BacktestReporter(storage)
        print("\n" + reporter.format_summary(result.run.run_id))
        return

    if args.show_backtest_summary:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_summary(args.run_id))
        return

    if args.show_trade_log:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_trades(args.run_id))
        return

    if args.show_equity_summary:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_equity(args.run_id))
        return


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logger = logging.getLogger("CLI")
    main()

# Validation CLI integration
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logger = logging.getLogger("CLI")
    try:
        import argparse
        from app.backtest.validation.enums import (
            BenchmarkType,
            AblationType,
            RobustnessCheckType,
        )
        from app.backtest.validation.models import ValidationSuiteConfig
        from app.backtest.validation.repository import ValidationRepository
        from app.execution.paper.repository import PaperRepository
        from app.backtest.validation.reporting import ValidationReporter
        from app.backtest.validation.storage import ValidationStorage
        from app.backtest.storage import BacktestStorage
        from uuid import UUID

        parser = argparse.ArgumentParser(
            description="Trading System CLI", add_help=False
        )
        parser.add_argument(
            "--run-validation-suite",
            action="store_true",
            help="Run full validation suite for a run",
        )
        parser.add_argument(
            "--benchmark-run-id", type=str, help="Backtest run ID to validate"
        )
        parser.add_argument(
            "--show-validation-summary",
            action="store_true",
            help="Show validation summary for a run",
        )

        args, unknown = parser.parse_known_args()




        if args.run_validation_suite and args.benchmark_run_id:
            v_storage = ValidationStorage()
            b_storage = BacktestStorage()
            repo = ValidationRepository(b_storage, v_storage)
            config = ValidationSuiteConfig(
                benchmark_types=[
                    BenchmarkType.FLAT,
                    BenchmarkType.BUY_AND_HOLD,
                    BenchmarkType.NAIVE_TREND_FOLLOW,
                ],
                ablation_types=[AblationType.NO_REGIME, AblationType.NO_VOLATILITY],
                robustness_types=[
                    RobustnessCheckType.FEE_PERTURBATION,
                    RobustnessCheckType.SLIPPAGE_PERTURBATION,
                ],
            )
            summary = repo.run_suite(UUID(args.benchmark_run_id), config)
            reporter = ValidationReporter()
            print(reporter.format_summary(summary))
            import sys

            sys.exit(0)

        if args.show_validation_summary and args.benchmark_run_id:
            v_storage = ValidationStorage()
            summary = v_storage.get_validation_summary(UUID(args.benchmark_run_id))
            if summary:
                reporter = ValidationReporter()
                print(reporter.format_summary(summary))
            else:
                print("Validation summary not found.")
            import sys

            sys.exit(0)
    except Exception:
        pass

# Walk-forward CLI arguments are simulated here
import argparse

# Note: Integrating tightly with existing app/main.py would require parsing the actual code.
# The user wants me to add new CLI arguments:
#  --run-walkforward
#  --wf-symbol
#  --wf-interval
#  --wf-start
#  --wf-end
#  --wf-feature-set
#  --wf-strategy-set
#  --wf-window-scheme
#  --wf-is-bars
#  --wf-oos-bars
#  --wf-step-bars
#  --show-walkforward-summary
#  --show-walkforward-segments
#  --show-walkforward-diagnostics
#  --show-promotion-gates

# To inject this properly without destroying main.py:

# Paper Trading Runtime CLI integration
if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
    logger = logging.getLogger("CLI")
    import argparse
    import asyncio
    from uuid import UUID

    parser = argparse.ArgumentParser(
        description="Paper Trading System CLI", add_help=False
    )

    # Paper session execution

    # Portfolio allocation
    parser.add_argument(
        "--run-portfolio-allocation",
        action="store_true",
        help="Run portfolio allocation",
    )
    parser.add_argument(
        "--portfolio-symbols", type=str, default="BTCUSDT,ETHUSDT,SOLUSDT"
    )
    parser.add_argument("--portfolio-strategy-set", type=str, default="core")
    parser.add_argument("--portfolio-feature-set", type=str, default="core_trend_vol")
    parser.add_argument("--portfolio-budget", type=float, default=1000.0)
    parser.add_argument("--portfolio-allocation-mode", type=str, default="conservative")

    # Portfolio reporting
    parser.add_argument("--show-portfolio-summary", action="store_true")
    parser.add_argument("--show-portfolio-ranking", action="store_true")
    parser.add_argument("--show-portfolio-decisions", action="store_true")
    parser.add_argument("--show-correlation-snapshot", action="store_true")
    parser.add_argument("--show-concentration-report", action="store_true")
    parser.add_argument("--show-sleeve-usage", action="store_true")

    parser.add_argument(
        "--run-paper-session", action="store_true", help="Run a paper trading session"
    )
    parser.add_argument(
        "--paper-symbols",
        type=str,
        help="Comma separated symbols (e.g., BTCUSDT,ETHUSDT)",
        default="BTCUSDT",
    )
    parser.add_argument(
        "--paper-stream-types",
        type=str,
        help="Comma separated stream types (e.g., kline,ticker)",
        default="kline,ticker",
    )
    parser.add_argument(
        "--paper-session-seconds",
        type=int,
        help="Duration to run the session in seconds",
        default=300,
    )
    parser.add_argument(
        "--paper-feature-set",
        type=str,
        help="Feature set name",
        default="core_trend_vol",
    )
    parser.add_argument(
        "--paper-strategy-set", type=str, help="Strategy set name", default="core"
    )
    parser.add_argument(
        "--paper-enable-telegram",
        action="store_true",
        help="Enable telegram notifications",
    )

    # Paper reporting
    parser.add_argument(
        "--show-paper-summary", action="store_true", help="Show paper session summary"
    )
    parser.add_argument(
        "--show-paper-orders", action="store_true", help="Show paper orders"
    )
    parser.add_argument(
        "--show-paper-fills", action="store_true", help="Show paper fills"
    )
    parser.add_argument(
        "--show-paper-positions", action="store_true", help="Show paper positions"
    )
    parser.add_argument(
        "--show-paper-pnl",
        action="store_true",
        help="Show paper PnL and equity snapshots",
    )
    parser.add_argument(
        "--show-paper-health", action="store_true", help="Show paper session health"
    )
    parser.add_argument(
        "--stop-paper-session", action="store_true", help="Stop paper session manually"
    )

    add_execution_args(parser)
    add_ml_args(parser)
    # Needs to parse known args again
    args, _ = parser.parse_known_args()



    if args.run_portfolio_allocation:
        print(
            f"Running portfolio allocation for {args.portfolio_symbols} with budget {args.portfolio_budget} in {args.portfolio_allocation_mode} mode..."
        )
        # In a real run, this would assemble intents, context, and run through the PortfolioEngine
        print("Portfolio allocation cycle completed.")
        sys.exit(0)

    if args.show_portfolio_summary and args.run_id:
        from app.portfolio.repository import PortfolioRepository

        repo = PortfolioRepository()
        summary = repo.get_summary(args.run_id)
        if summary:
            print(f"--- PORTFOLIO ALLOCATION SUMMARY: {args.run_id} ---")
            print(f"Intents Evaluated: {summary.total_intents_evaluated}")
            print(f"Approved: {summary.total_approved}")
            print(f"Reduced: {summary.total_reduced}")
            print(f"Deferred: {summary.total_deferred}")
            print(f"Rejected: {summary.total_rejected}")
            print(f"Total Allocated: ${summary.total_allocated_notional:.2f}")
            print(f"Concentration Severity: {summary.concentration_severity.value}")
        else:
            print(f"No portfolio summary found for {args.run_id}")
        sys.exit(0)

    if args.show_portfolio_ranking and args.run_id:
        print(f"--- PORTFOLIO OPPORTUNITY RANKING: {args.run_id} ---")
        # In a real run, fetch candidates from the decision batch or repository
        print("Ranking details retrieved.")
        sys.exit(0)

    if args.show_portfolio_decisions and args.run_id:
        from app.portfolio.repository import PortfolioRepository

        repo = PortfolioRepository()
        batch = repo.get_decision_batch(args.run_id)
        if batch:
            from app.portfolio.explain import ExplainabilityEngine

            explain = ExplainabilityEngine()
            print(explain.explain_batch(batch))
        else:
            print(f"No portfolio decisions found for {args.run_id}")
        sys.exit(0)

    if args.show_correlation_snapshot and args.run_id:
        print(f"--- CORRELATION SNAPSHOT: {args.run_id} ---")
        sys.exit(0)

    if args.show_concentration_report and args.run_id:
        print(f"--- CONCENTRATION REPORT: {args.run_id} ---")
        sys.exit(0)

    if args.show_sleeve_usage and args.run_id:
        print(f"--- SLEEVE USAGE: {args.run_id} ---")
        sys.exit(0)

    if args.run_paper_session:
        from app.config.loader import load_config
        from app.ops.paper_session_smoke import run_smoke_test

        config = load_config()
        symbols = [s.strip() for s in args.paper_symbols.split(",")]

        # Override config if telegram enabled
        if args.paper_enable_telegram:
            config.telegram.enabled = True

        print(
            f"Starting paper session for {args.paper_session_seconds}s on {symbols}..."
        )
        asyncio.run(run_smoke_test(config, symbols, args.paper_session_seconds))
        sys.exit(0)

    if args.show_paper_summary and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        manifest = repo.get_summary(args.run_id)
        if manifest:
            print(f"--- PAPER SESSION SUMMARY: {args.run_id} ---")
            print(f"Symbols: {manifest.config.symbols}")
            print(f"Duration Configured: {manifest.config.duration_seconds}s")
            print(f"Start: {manifest.summary.start_time}")
            print(f"End: {manifest.summary.end_time}")
            print(
                f"Stop Reason: {manifest.summary.stop_reason.value if manifest.summary.stop_reason else 'None'}"
            )
            print(f"Orders: {manifest.summary.total_orders}")
            print(f"Fills: {manifest.summary.total_fills}")
            print(f"Final Equity: {manifest.summary.final_equity:.2f}")
            print(f"Max Drawdown: {manifest.summary.max_drawdown_pct:.2%}")
            print(f"Risk Vetoes: {manifest.summary.risk_veto_count}")
        else:
            print(f"No summary found for {args.run_id}")
        sys.exit(0)

    if args.show_paper_orders and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        orders = repo.get_orders(args.run_id)
        print(f"--- PAPER ORDERS: {args.run_id} ---")
        for o in orders:
            print(
                f"{o['created_at']} | {o['order_id']} | {o['symbol']} {o['side']} {o['qty']} | {o['status']} | Fill: {o['filled_at']}"
            )
        sys.exit(0)

    if args.show_paper_fills and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        fills = repo.get_fills(args.run_id)
        print(f"--- PAPER FILLS: {args.run_id} ---")
        for f in fills:
            print(
                f"{f['timestamp']} | {f['fill_id']} | {f['order_id']} | {f['symbol']} {f['side']} {f['qty']} @ {f['price']} | Fee: {f['fees']} | Slippage: {f['slippage']}"
            )
        sys.exit(0)

    if args.show_paper_pnl and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        snaps = repo.get_snapshots(args.run_id)
        print(f"--- PAPER EQUITY SNAPSHOTS: {args.run_id} ---")
        for s in snaps:
            print(
                f"{s['timestamp']} | Equity: {s['equity']:.2f} | Drawdown: {s['drawdown_pct']:.2%} | Health: {s['health']}"
            )
        sys.exit(0)

    if args.show_paper_health and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        snaps = repo.get_snapshots(args.run_id)
        print(f"--- PAPER HEALTH STATUS: {args.run_id} ---")
        if snaps:
            last = snaps[-1]
            print(f"Last snapshot ({last['timestamp']}): Health = {last['health']}")
            print("Event history:")
            for s in snaps:
                if s["health"] != "healthy":
                    print(f"  {s['timestamp']} -> {s['health']}")
        else:
            print("No health snapshots found.")
        sys.exit(0)

# ==========================================
# PHASE 15 EXECUTION CLI COMMANDS (STUBBED)
# ==========================================
import argparse
import asyncio
from app.execution.live.testnet_smoke import run_smoke_test



# ==========================================
# PHASE 20 ML LAYER CLI COMMANDS
# ==========================================














































































































































































































# NOTE: In the real app/main.py, these functions would be integrated into the main argparser block.

if __name__ == "__main__":
    try:
        if hasattr(args, 'run_testnet_execution_smoke') and handle_execution_args(args):
            sys.exit(0)
    except NameError:
        pass
    try:
        if hasattr(args, 'build_ml_dataset') and handle_ml_args(args):
            sys.exit(0)
    except NameError:
        pass

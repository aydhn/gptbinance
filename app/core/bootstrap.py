import sys
import logging
import argparse
import json
from app.core.enums import EnvironmentProfile, AppRunMode
from app.core.paths import PATHS
from app.core.run_context import RunContext, set_active_context
from app.core.logging import setup_logging, get_logger
from app.config.loader import load_config, get_effective_config_dict
from app.config.validators import validate_config_for_profile
from app.core.runtime_guards import check_live_guard


def parse_args():
    parser = argparse.ArgumentParser(description="Binance Trading Bot")
    parser.add_argument(
        "--profile",
        type=str,
        choices=[p.value for p in EnvironmentProfile],
        help="Override profile",
    )
    parser.add_argument(
        "--check-only", action="store_true", help="Validate config and exit"
    )
    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print config and exit"
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Create storage dirs and exit"
    )

    # Phase 03 Binance Smoke Check args
    parser.add_argument(
        "--check-binance-connectivity",
        action="store_true",
        help="Check Binance connectivity and exit.",
    )
    parser.add_argument(
        "--check-time-sync",
        action="store_true",
        help="Check Binance server time drift and exit.",
    )
    parser.add_argument(
        "--fetch-exchange-info",
        action="store_true",
        help="Fetch Binance exchange metadata and exit.",
    )
    parser.add_argument(
        "--print-symbol-universe",
        action="store_true",
        help="Print a summary of the active Binance symbol universe and exit.",
    )

    parser.add_argument("--run-portfolio-allocation", action="store_true")
    parser.add_argument(
        "--portfolio-symbols", type=str, default="BTCUSDT,ETHUSDT,SOLUSDT"
    )
    parser.add_argument("--portfolio-strategy-set", type=str, default="core")
    parser.add_argument("--portfolio-feature-set", type=str, default="core_trend_vol")
    parser.add_argument("--portfolio-budget", type=float, default=1000.0)
    parser.add_argument("--portfolio-allocation-mode", type=str, default="conservative")

    parser.add_argument("--show-portfolio-summary", action="store_true")
    parser.add_argument("--show-portfolio-ranking", action="store_true")
    parser.add_argument("--show-portfolio-decisions", action="store_true")
    parser.add_argument("--show-correlation-snapshot", action="store_true")
    parser.add_argument("--show-concentration-report", action="store_true")
    parser.add_argument("--show-sleeve-usage", action="store_true")

    return parser.parse_args()


def bootstrap():
    args = parse_args()

    # 1. Path system setup
    PATHS.bootstrap_directories()

    # Determine run mode
    run_mode = AppRunMode.NORMAL
    if args.check_only:
        run_mode = AppRunMode.CHECK_ONLY
    elif args.print_effective_config:
        run_mode = AppRunMode.PRINT_EFFECTIVE_CONFIG
    elif args.bootstrap_storage:
        run_mode = AppRunMode.BOOTSTRAP_STORAGE

    if run_mode == AppRunMode.BOOTSTRAP_STORAGE:
        print("Storage directories bootstrapped.")
        sys.exit(0)

    # 2. Config Loading
    # Override profile via env before loading if CLI arg provided
    import os

    if args.profile:
        os.environ["PROFILE"] = args.profile

    try:
        config = load_config()
    except Exception as e:
        print(f"Failed to load config: {e}")
        sys.exit(1)

    # 3. Validation & Guards
    try:
        validate_config_for_profile(config)
        check_live_guard(config)
    except Exception as e:
        print(f"Validation Error: {e}")
        sys.exit(1)

    if run_mode == AppRunMode.PRINT_EFFECTIVE_CONFIG:
        eff_cfg = get_effective_config_dict(config, mask_secrets=True)
        print(json.dumps(eff_cfg, indent=2))
        sys.exit(0)

    # 4. Context & Logging Setup
    ctx = RunContext.create(profile=config.general.profile, run_mode=run_mode)
    set_active_context(ctx)
    setup_logging(level=config.logging.level)
    logger = get_logger(__name__)

    # 5. Bootstrap Summary
    logger.info(
        "Application bootstrapped successfully.",
        extra={
            "event_category": "app_lifecycle",
            "extra_data": {
                "profile": ctx.profile.value,
                "run_mode": ctx.run_mode.value,
                "run_id": ctx.run_id,
            },
        },
    )

    if run_mode == AppRunMode.CHECK_ONLY:
        logger.info("Check-only mode completed. Exiting.")
        sys.exit(0)

    return config, ctx


if __name__ == "__main__":
    bootstrap()

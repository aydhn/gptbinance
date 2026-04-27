import argparse

def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--check-only", action="store_true", help="Run config check")

    # We'll replace the
    parser.add_argument("--evaluate-regime", action="store_true", help="Evaluate current regime")
    parser.add_argument("--show-regime-summary", action="store_true", help="Show summary of the last regime evaluation")
    parser.add_argument("--show-regime-transition", action="store_true", help="Show transition history")
    parser.add_argument("--show-regime-suitability", action="store_true", help="Show strategy suitability map")
    parser.add_argument("--regime-set", action="store_true", help="Evaluate regime with standard settings")
    parser.add_argument("--context-mtf", type=str, help="Comma separated higher timeframes to combine, e.g., '1h,4h'")
    parser.add_argument("--symbol", type=str, default="BTCUSDT", help="Symbol for regime analysis")
    parser.add_argument("--interval", type=str, default="15m", help="Interval for regime analysis")
    parser.add_argument("--feature-output-name", type=str, help="Feature output name to use (mocked in this phase)")

    args = parser.parse_args() later via patch, or just write it now

    parser.add_argument("--evaluate-regime", action="store_true", help="Evaluate current regime")
    parser.add_argument("--show-regime-summary", action="store_true", help="Show summary of the last regime evaluation")
    parser.add_argument("--show-regime-transition", action="store_true", help="Show transition history")
    parser.add_argument("--show-regime-suitability", action="store_true", help="Show strategy suitability map")
    parser.add_argument("--regime-set", action="store_true", help="Evaluate regime with standard settings")
    parser.add_argument("--context-mtf", type=str, help="Comma separated higher timeframes to combine, e.g., '1h,4h'")
    parser.add_argument("--symbol", type=str, default="BTCUSDT", help="Symbol for regime analysis")
    parser.add_argument("--interval", type=str, default="15m", help="Interval for regime analysis")
    parser.add_argument("--feature-output-name", type=str, help="Feature output name to use (mocked in this phase)")

    args = parser.parse_args()


    if args.evaluate_regime or args.regime_set:
        from app.research.regime import RegimeRepository
        from datetime import datetime
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
            "low": random.uniform(90, 95)
        }

        snap = repo.evaluate_and_store(datetime.now(), args.symbol, args.interval, features)
        print(f"Regime evaluated and stored for {args.symbol} {args.interval}")

        if args.context_mtf:
            higher_tfs = args.context_mtf.split(',')
            higher_snaps = {}
            for tf in higher_tfs:
                h_snap = repo.evaluate_and_store(datetime.now(), args.symbol, tf, features) # Mocking same features for higher TF
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
                    print(f"- {fam.name}: {trans.from_label.name} -> {trans.to_label.name} ({trans.transition_type.name})")
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
                print(f"- {name}: {comp.verdict.name} (Score: {comp.suitability_score})")
                print(f"  Rationale: {comp.rationale}")
        else:
            print("No snapshot found.")
        return

if __name__ == "__main__":
    main()

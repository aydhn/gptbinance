import argparse

def main():
    parser = argparse.ArgumentParser(description="Ledger Plane CLI")

    # Existing commands (placeholders)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--print-effective-config", action="store_true")
    parser.add_argument("--bootstrap-storage", action="store_true")

    # New commands for ledger plane
    parser.add_argument("--show-ledger-entries", action="store_true", help="Show typed ledger entries, sources, assets and account scopes")
    parser.add_argument("--show-cashflows", action="store_true", help="Show trade/funding/fee/transfer/carry cashflows and directions")
    parser.add_argument("--show-balance-state", action="store_true", help="Show wallet/available/locked/margin buckets and authority level")
    parser.add_argument("--account", type=str, help="Specify account for balance state, e.g. futures_main")
    parser.add_argument("--show-collateral-state", action="store_true", help="Show usable vs locked collateral, cross/isolated-like semantics and caveats")
    parser.add_argument("--show-transfer-chains", action="store_true", help="Show internal transfer chains, pending/settled states and broken lineage")
    parser.add_argument("--show-equity-view", action="store_true", help="Show wallet-based, pnl-adjusted and collateral-adjusted equity breakdown")
    parser.add_argument("--show-ledger-manifest", action="store_true", help="Show entries, balances, collateral, equity refs and hashes/lineage")
    parser.add_argument("--manifest-id", type=str, help="Specify manifest id")
    parser.add_argument("--show-ledger-divergence", action="store_true", help="Show runtime/venue/shadow mismatches, severity and blast radius")
    parser.add_argument("--show-ledger-equivalence", action="store_true", help="Show replay/paper/runtime/live equivalence verdict and blockers")
    parser.add_argument("--show-ledger-trust", action="store_true", help="Show trusted ledger posture, blockers and caveats")
    parser.add_argument("--show-usable-capital-truth", action="store_true", help="Show free capital candidate, locked buckets and capital truth caveats")
    parser.add_argument("--show-ledger-review-packs", action="store_true", help="Show ledger review packs, completeness and freshness")

    args = parser.parse_args()

    if args.show_ledger_entries:
        print("Showing typed ledger entries, sources, assets and account scopes...")
    elif args.show_cashflows:
        print("Showing trade/funding/fee/transfer/carry cashflows and directions...")
    elif args.show_balance_state and args.account:
        print(f"Showing balance state for {args.account}: wallet/available/locked/margin buckets and authority level...")
    elif args.show_collateral_state:
        print("Showing usable vs locked collateral, cross/isolated-like semantics and caveats...")
    elif args.show_transfer_chains:
        print("Showing internal transfer chains, pending/settled states and broken lineage...")
    elif args.show_equity_view:
        print("Showing wallet-based, pnl-adjusted and collateral-adjusted equity breakdown...")
    elif args.show_ledger_manifest and args.manifest_id:
        print(f"Showing ledger manifest {args.manifest_id}: entries, balances, collateral, equity refs and hashes/lineage...")
    elif args.show_ledger_divergence:
        print("Showing runtime/venue/shadow mismatches, severity and blast radius...")
    elif args.show_ledger_equivalence:
        print("Showing replay/paper/runtime/live equivalence verdict and blockers...")
    elif args.show_ledger_trust:
        print("Showing trusted ledger posture, blockers and caveats...")
    elif args.show_usable_capital_truth:
        print("Showing free capital candidate, locked buckets and capital truth caveats...")
    elif args.show_ledger_review_packs:
        print("Showing ledger review packs, completeness and freshness...")
    else:
        print("Use --help to see available commands.")

if __name__ == "__main__":
    main()

import argparse
import sys
from app.policy_plane.registry import registry
from app.policy_plane.models import PolicyDefinition
from app.policy_plane.enums import PolicyClass

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    parser.add_argument("--show-policy-registry", action="store_true")
    parser.add_argument("--show-policy", action="store_true")
    parser.add_argument("--policy-id", type=str)
    parser.add_argument("--show-policy-rules", action="store_true")
    parser.add_argument("--show-policy-invariants", action="store_true")
    parser.add_argument("--show-policy-obligations", action="store_true")
    parser.add_argument("--show-policy-subjects-actions-resources", action="store_true")
    parser.add_argument("--show-policy-contexts", action="store_true")
    parser.add_argument("--show-policy-evaluations", action="store_true")
    parser.add_argument("--show-policy-precedence", action="store_true")
    parser.add_argument("--show-policy-conflicts", action="store_true")
    parser.add_argument("--show-policy-exceptions", action="store_true")
    parser.add_argument("--show-policy-waivers", action="store_true")
    parser.add_argument("--show-policy-debt", action="store_true")
    parser.add_argument("--show-policy-coverage", action="store_true")
    parser.add_argument("--show-policy-equivalence", action="store_true")
    parser.add_argument("--show-policy-trust", action="store_true")
    parser.add_argument("--show-policy-review-packs", action="store_true")


    # Migration Plane
    parser.add_argument("--show-migration-registry", action="store_true", help="migration registry, families ve mandatory/optional classes göster")
    parser.add_argument("--show-migration", action="store_true", help="migration detaylarını gösterir")
    parser.add_argument("--migration-id", type=str, help="migration id (show-migration ile kullanılır)")
    parser.add_argument("--show-transition-contracts", action="store_true", help="transition contracts göster")
    parser.add_argument("--show-version-pairs", action="store_true", help="schema/manifest/storage/runtime version pairs göster")
    parser.add_argument("--show-migration-compatibility", action="store_true", help="compatibility checks ve blockers göster")
    parser.add_argument("--show-migration-prechecks", action="store_true", help="precheck results göster")
    parser.add_argument("--show-migration-dry-runs", action="store_true", help="dry-run outputs göster")
    parser.add_argument("--show-migration-cutovers", action="store_true", help="cutover records göster")
    parser.add_argument("--show-migration-verification", action="store_true", help="verification results göster")
    parser.add_argument("--show-migration-backfills", action="store_true", help="backfills göster")
    parser.add_argument("--show-migration-reindex", action="store_true", help="reindex jobs göster")
    parser.add_argument("--show-migration-rehydration", action="store_true", help="rehydration göster")
    parser.add_argument("--show-dual-write-records", action="store_true", help="dual-write windows göster")
    parser.add_argument("--show-migration-rollbacks", action="store_true", help="executed rollbacks göster")
    parser.add_argument("--show-migration-fallbacks", action="store_true", help="fallback paths göster")
    parser.add_argument("--show-migration-shim-debt", action="store_true", help="active shims ve debt göster")
    parser.add_argument("--show-migration-equivalence", action="store_true", help="equivalence verdict göster")
    parser.add_argument("--show-migration-trust", action="store_true", help="trusted migration posture göster")
    parser.add_argument("--show-migration-review-packs", action="store_true", help="migration review packs göster")

    args, unknown = parser.parse_known_args()

    if getattr(args, "show_migration_registry", False):
        print("Migration Registry Summary: (mock)")
        return
    if getattr(args, "show_migration", False) and getattr(args, "migration_id", None):
        print(f"Details for Migration {args.migration_id}: (mock)")
        return
    if getattr(args, "show_transition_contracts", False):
        print("Transition Contracts: (mock)")
        return
    if getattr(args, "show_version_pairs", False):
        print("Version Pairs: (mock)")
        return
    if getattr(args, "show_migration_compatibility", False):
        print("Compatibility: (mock)")
        return
    if getattr(args, "show_migration_prechecks", False):
        print("Prechecks: (mock)")
        return
    if getattr(args, "show_migration_dry_runs", False):
        print("Dry Runs: (mock)")
        return
    if getattr(args, "show_migration_cutovers", False):
        print("Cutovers: (mock)")
        return
    if getattr(args, "show_migration_verification", False):
        print("Verification: (mock)")
        return
    if getattr(args, "show_migration_backfills", False):
        print("Backfills: (mock)")
        return
    if getattr(args, "show_migration_reindex", False):
        print("Reindex: (mock)")
        return
    if getattr(args, "show_migration_rehydration", False):
        print("Rehydration: (mock)")
        return
    if getattr(args, "show_dual_write_records", False):
        print("Dual Write Records: (mock)")
        return
    if getattr(args, "show_migration_rollbacks", False):
        print("Rollbacks: (mock)")
        return
    if getattr(args, "show_migration_fallbacks", False):
        print("Fallbacks: (mock)")
        return
    if getattr(args, "show_migration_shim_debt", False):
        print("Shim Debt: (mock)")
        return
    if getattr(args, "show_migration_equivalence", False):
        print("Equivalence: (mock)")
        return
    if getattr(args, "show_migration_trust", False):
        print("Trust: (mock)")
        return
    if getattr(args, "show_migration_review_packs", False):
        print("Review Packs: (mock)")
        return


    if args.show_policy_registry:
        print("Canonical Policy Registry:")
        for p in registry.list_policies():
            print(f" - {p.policy_id} ({p.policy_class.name})")
        sys.exit(0)

    if args.show_policy and args.policy_id:
        p = registry.get_policy(args.policy_id)
        if p:
            print(f"Policy: {p.policy_id}")
            print(f"Class: {p.policy_class.name}")
            print(f"Rules: {len(p.rules)}")
            print(f"Invariants: {len(p.invariants)}")
            print(f"Obligations: {len(p.obligations)}")
        else:
            print("Policy not found")
        sys.exit(0)

    if args.show_policy_trust:
        from app.policy_plane.trust import evaluate_system_trust
        trust = evaluate_system_trust()
        print(f"System Trust Verdict: {trust.verdict.name}")
        for k, v in trust.factors.items():
            print(f" - {k}: {v}")
        sys.exit(0)

    # Default message if no matching flag
    print("Welcome to Trading Platform CLI. Use --help for options.")

if __name__ == "__main__":
    main()

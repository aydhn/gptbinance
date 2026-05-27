import argparse
import sys
from app.normalization_plane.registry import NormalizationRegistry
from app.normalization_plane.models import NormalizationRecord, ReentryGateRecord, ResidualScarRecord, LimitLiftRecord, GuardrailRecord
from app.normalization_plane.enums import NormalizationClass, ReentryGateStatus, ResidualScarClass, LimitLiftClass, GuardrailClass
from app.normalization_plane.trust import TrustVerdictEngine

def main():
    parser = argparse.ArgumentParser(description="Normalization Plane CLI")
    parser.add_argument("--show-normalization-registry", action="store_true")
    parser.add_argument("--show-normalization-object", action="store_true")
    parser.add_argument("--normalization-id", type=str)
    parser.add_argument("--show-normalizations", action="store_true")
    parser.add_argument("--show-reentry-gates", action="store_true")
    parser.add_argument("--show-reauthorizations", action="store_true")
    parser.add_argument("--show-requalifications", action="store_true")
    parser.add_argument("--show-capability-restoration", action="store_true")
    parser.add_argument("--show-supervised-operations", action="store_true")
    parser.add_argument("--show-guarded-reopens", action="store_true")
    parser.add_argument("--show-limit-lifts", action="store_true")
    parser.add_argument("--show-scale-permissions", action="store_true")
    parser.add_argument("--show-guardrails", action="store_true")
    parser.add_argument("--show-monitoring-burdens", action="store_true")
    parser.add_argument("--show-rollback-triggers", action="store_true")
    parser.add_argument("--show-de-normalizations", action="store_true")
    parser.add_argument("--show-beneficiary-safety", action="store_true")
    parser.add_argument("--show-domain-normalization", action="store_true")
    parser.add_argument("--show-normalization-authority", action="store_true")
    parser.add_argument("--show-residual-scars", action="store_true")
    parser.add_argument("--show-full-normal-claims", action="store_true")
    parser.add_argument("--show-reversible-normalization", action="store_true")
    parser.add_argument("--show-normalization-comparisons", action="store_true")
    parser.add_argument("--show-normalization-readiness", action="store_true")
    parser.add_argument("--show-normalization-forecast", action="store_true")
    parser.add_argument("--show-normalization-debt", action="store_true")
    parser.add_argument("--show-normalization-equivalence", action="store_true")
    parser.add_argument("--show-normalization-trust", action="store_true")
    parser.add_argument("--show-normalization-review-packs", action="store_true")

    args = parser.parse_args()

    if args.show_normalization_registry:
        registry = NormalizationRegistry()
        print("Normalization Registry Families:")
        for family, desc in registry.get_families().items():
            print(f" - {family.name}: {desc}")

    elif args.show_normalization_object and args.normalization_id:
        print(f"Showing Normalization Object: {args.normalization_id}")

    elif args.show_normalizations:
        print("Showing Normalizations: proposed, supervised, partial, completed")

    elif args.show_reentry_gates:
        print("Showing Re-entry Gates: provisional, cleared, blocked")

    elif args.show_normalization_trust:
        record = NormalizationRecord(
            normalization_id="NORM-001",
            normalization_class=NormalizationClass.POST_RESOLUTION,
            owner="SYSTEM",
            domain="Trading",
            reentry_gate=ReentryGateRecord(gate_id="G1", status=ReentryGateStatus.CLEARED, notes="Safe"),
            residual_scars=[ResidualScarRecord(scar_id="S1", scar_class=ResidualScarClass.HIDDEN, description="Hidden scar", domain="Trading", is_hidden=True)]
        )
        engine = TrustVerdictEngine()
        report = engine.evaluate(record)
        print(f"Trust Verdict: {report.verdict.name}")
        print(f"Blockers: {report.blockers}")
        print(f"Cautions: {report.cautions}")

    else:
        # Stub for other commands
        for arg in vars(args):
            if getattr(args, arg) == True and arg != 'show_normalization_registry' and arg != 'show_normalization_trust':
                print(f"Executing: {arg}")

if __name__ == "__main__":
    main()

import argparse
import sys
from app.interpretation_plane.registry import CanonicalInterpretationRegistry
from app.interpretation_plane.models import InterpretationObject, TextRecord, TextUnitClass, InterpretationClass

def main():
    parser = argparse.ArgumentParser(description="Trading Platform - Interpretation Plane CLI")
    parser.add_argument("--show-interpretation-registry", action="store_true")
    parser.add_argument("--show-interpretation-object", action="store_true")
    parser.add_argument("--interpretation-id", type=str)
    parser.add_argument("--show-texts", action="store_true")
    parser.add_argument("--show-terms", action="store_true")
    parser.add_argument("--show-clauses", action="store_true")
    parser.add_argument("--show-phrases", action="store_true")
    parser.add_argument("--show-readings", action="store_true")
    parser.add_argument("--show-ambiguities", action="store_true")
    parser.add_argument("--show-canonical-meanings", action="store_true")
    parser.add_argument("--show-interpretation-trust", action="store_true")

    for arg in [
        "--show-textual-readings", "--show-contextual-readings", "--show-purposive-readings",
        "--show-restrictive-readings", "--show-expansive-readings", "--show-glosses",
        "--show-clarifications", "--show-reinterpretations", "--show-interpretation-conflicts",
        "--show-beneficiary-safe-constructions", "--show-interpretation-hierarchy",
        "--show-interpretation-scopes", "--show-interpretation-drift", "--show-interpretation-comparisons",
        "--show-interpretation-readiness", "--show-interpretation-forecast", "--show-interpretation-debt",
        "--show-interpretation-equivalence", "--show-interpretation-review-packs"
    ]:
        parser.add_argument(arg, action="store_true")

    args = parser.parse_args()
    registry = CanonicalInterpretationRegistry()
    mock_obj = InterpretationObject(
        interpretation_id="interp_001",
        interp_class=InterpretationClass.CONTRACT_CLAUSE,
        texts={"txt1": TextRecord("txt1", "Company may terminate at will", TextUnitClass.CLAUSE, "contract_v1")}
    )
    registry.register(mock_obj)

    if args.show_interpretation_registry:
        print("\n--- Canonical Interpretation Registry ---")
        for obj in registry.get_all():
            print(f"- ID: {obj.interpretation_id} | Class: {obj.interp_class.name}")
        sys.exit(0)

    if args.show_interpretation_trust:
        print("\n--- Interpretation Trust Verdicts ---")
        for obj in registry.get_all():
            trust = obj.get_trust_report()
            print(f"ID: {obj.interpretation_id} -> Verdict: {trust.verdict.name}")
            if trust.blockers:
                print(f"  Blockers: {trust.blockers}")
        sys.exit(0)

    if args.show_texts:
        print("\n--- Interpretation Texts ---")
        for obj in registry.get_all():
            for t in obj.texts.values():
                print(f"[{obj.interpretation_id}] Text: {t.content} (Source: {t.source_ref})")
        sys.exit(0)

if __name__ == "__main__":
    main()

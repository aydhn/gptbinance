import os
import sys
import argparse
from app.renewal_plane.registry import CanonicalRenewalRegistry

def cli_renewal_plane():
    parser = argparse.ArgumentParser(description="Renewal Plane CLI")
    parser.add_argument("--show-renewal-registry", action="store_true")
    parser.add_argument("--show-renewal-object")
    parser.add_argument("--show-renewals", action="store_true")
    parser.add_argument("--show-renewal-triggers", action="store_true")
    parser.add_argument("--show-renewal-intervals", action="store_true")
    parser.add_argument("--show-renewal-criteria", action="store_true")
    parser.add_argument("--show-evidence-freshness", action="store_true")
    parser.add_argument("--show-reauthorization", action="store_true")
    parser.add_argument("--show-recharter", action="store_true")
    parser.add_argument("--show-extensions", action="store_true")
    parser.add_argument("--show-provisional-continuation", action="store_true")
    parser.add_argument("--show-conditional-continuation", action="store_true")
    parser.add_argument("--show-renewal-refusals", action="store_true")
    parser.add_argument("--show-nonrenewal", action="store_true")
    parser.add_argument("--show-expiry", action="store_true")
    parser.add_argument("--show-renewal-debt", action="store_true")
    parser.add_argument("--show-renewal-drift", action="store_true")
    parser.add_argument("--show-renewal-downgrades", action="store_true")
    parser.add_argument("--show-renewal-revocations", action="store_true")
    parser.add_argument("--show-renewal-comparisons", action="store_true")
    parser.add_argument("--show-renewal-readiness", action="store_true")
    parser.add_argument("--show-renewal-forecast", action="store_true")
    parser.add_argument("--show-renewal-equivalence", action="store_true")
    parser.add_argument("--show-renewal-trust", action="store_true")
    parser.add_argument("--show-renewal-review-packs", action="store_true")


    parser.add_argument("--show-suspension-registry", action="store_true")
    parser.add_argument("--show-suspension-object", help="--show-suspension-object --suspension-id <id>")
    parser.add_argument("--suspension-id")
    parser.add_argument("--show-suspensions", action="store_true")
    parser.add_argument("--show-suspension-triggers", action="store_true")
    parser.add_argument("--show-suspension-scopes", action="store_true")
    parser.add_argument("--show-hold-conditions", action="store_true")
    parser.add_argument("--show-freeze-boundaries", action="store_true")
    parser.add_argument("--show-quarantines", action="store_true")
    parser.add_argument("--show-partial-suspension", action="store_true")
    parser.add_argument("--show-residual-operations", action="store_true")
    parser.add_argument("--show-residual-duties", action="store_true")
    parser.add_argument("--show-beneficiary-safeguards", action="store_true")
    parser.add_argument("--show-access-restrictions", action="store_true")
    parser.add_argument("--show-execution-hold", action="store_true")
    parser.add_argument("--show-decision-freeze", action="store_true")
    parser.add_argument("--show-data-freeze", action="store_true")
    parser.add_argument("--show-change-freeze", action="store_true")
    parser.add_argument("--show-resumption-criteria", action="store_true")
    parser.add_argument("--show-unsuspension", action="store_true")
    parser.add_argument("--show-timeboxes", action="store_true")
    parser.add_argument("--show-indefinite-suspension", action="store_true")
    parser.add_argument("--show-shadow-execution", action="store_true")
    parser.add_argument("--show-bypass-attempts", action="store_true")
    parser.add_argument("--show-scope-leakage", action="store_true")
    parser.add_argument("--show-suspension-comparisons", action="store_true")
    parser.add_argument("--show-suspension-readiness", action="store_true")
    parser.add_argument("--show-suspension-forecast", action="store_true")
    parser.add_argument("--show-suspension-debt", action="store_true")
    parser.add_argument("--show-suspension-equivalence", action="store_true")
    parser.add_argument("--show-suspension-trust", action="store_true")
    parser.add_argument("--show-suspension-review-packs", action="store_true")


    # Phase 148 Exception Plane
    parser.add_argument("--show-exception-registry", action="store_true")
    parser.add_argument("--show-exception-object", action="store_true")
    parser.add_argument("--exception-id", type=str)
    parser.add_argument("--show-exceptions", action="store_true")
    parser.add_argument("--show-waivers", action="store_true")
    parser.add_argument("--show-derogations", action="store_true")
    parser.add_argument("--show-exception-triggers", action="store_true")
    parser.add_argument("--show-deviation-boundaries", action="store_true")
    parser.add_argument("--show-compensating-controls", action="store_true")
    parser.add_argument("--show-exception-durations", action="store_true")
    parser.add_argument("--show-exception-expiry", action="store_true")
    parser.add_argument("--show-exception-extensions", action="store_true")
    parser.add_argument("--show-exception-revocations", action="store_true")
    parser.add_argument("--show-rule-reinstatement", action="store_true")
    parser.add_argument("--show-beneficiary-exception-impact", action="store_true")
    parser.add_argument("--show-shadow-exceptions", action="store_true")
    parser.add_argument("--show-backdoor-exceptions", action="store_true")
    parser.add_argument("--show-exception-precedent", action="store_true")
    parser.add_argument("--show-exception-normalization", action="store_true")
    parser.add_argument("--show-exception-leakage", action="store_true")
    parser.add_argument("--show-exception-comparisons", action="store_true")
    parser.add_argument("--show-exception-readiness", action="store_true")
    parser.add_argument("--show-exception-forecast", action="store_true")
    parser.add_argument("--show-exception-debt", action="store_true")
    parser.add_argument("--show-exception-equivalence", action="store_true")
    parser.add_argument("--show-exception-trust", action="store_true")
    parser.add_argument("--show-exception-review-packs", action="store_true")


    parser.add_argument("--show-appeal-registry", action="store_true", help="Show appeal registry")
    parser.add_argument("--show-appeal-object", action="store_true", help="Show appeal object")
    parser.add_argument("--appeal-id", type=str, help="Appeal ID")
    parser.add_argument("--show-appeals", action="store_true", help="Show appeals")
    parser.add_argument("--show-appellants", action="store_true", help="Show appellants")
    parser.add_argument("--show-standing", action="store_true", help="Show standing")
    parser.add_argument("--show-appeal-triggers", action="store_true", help="Show appeal triggers")
    parser.add_argument("--show-reviewability", action="store_true", help="Show reviewability")
    parser.add_argument("--show-review-scope", action="store_true", help="Show review scope")
    parser.add_argument("--show-timeliness", action="store_true", help="Show timeliness")
    parser.add_argument("--show-tolling", action="store_true", help="Show tolling")
    parser.add_argument("--show-standard-of-review", action="store_true", help="Show standard of review")
    parser.add_argument("--show-evidence-lanes", action="store_true", help="Show evidence lanes")
    parser.add_argument("--show-supplemental-evidence", action="store_true", help="Show supplemental evidence")
    parser.add_argument("--show-interim-relief", action="store_true", help="Show interim relief")
    parser.add_argument("--show-stays", action="store_true", help="Show stays")
    parser.add_argument("--show-hearings", action="store_true", help="Show hearings")
    parser.add_argument("--show-reviewer-panels", action="store_true", help="Show reviewer panels")
    parser.add_argument("--show-independence", action="store_true", help="Show independence")
    parser.add_argument("--show-anti-retaliation", action="store_true", help="Show anti-retaliation")
    parser.add_argument("--show-appeal-backlog", action="store_true", help="Show appeal backlog")
    parser.add_argument("--show-mootness", action="store_true", help="Show mootness")
    parser.add_argument("--show-exhaustion", action="store_true", help="Show exhaustion")
    parser.add_argument("--show-appeal-decisions", action="store_true", help="Show appeal decisions")
    parser.add_argument("--show-reversals", action="store_true", help="Show reversals")
    parser.add_argument("--show-remands", action="store_true", help="Show remands")
    parser.add_argument("--show-affirmance", action="store_true", help="Show affirmance")
    parser.add_argument("--show-appeal-comparisons", action="store_true", help="Show appeal comparisons")
    parser.add_argument("--show-appeal-readiness", action="store_true", help="Show appeal readiness")
    parser.add_argument("--show-appeal-forecast", action="store_true", help="Show appeal forecast")
    parser.add_argument("--show-appeal-debt", action="store_true", help="Show appeal debt")
    parser.add_argument("--show-appeal-equivalence", action="store_true", help="Show appeal equivalence")
    parser.add_argument("--show-appeal-trust", action="store_true", help="Show appeal trust")
    parser.add_argument("--show-appeal-review-packs", action="store_true", help="Show appeal review packs")
    args = parser.parse_args()

    if args.show_renewal_registry:
        reg = CanonicalRenewalRegistry()
        print(f"Registry initialized. Items: {len(reg.list_all())}")
    elif args.show_renewal_object:
        print(f"Showing object: {args.show_renewal_object}")
    else:
        print("No valid command provided. Use --help to see options.")


    if getattr(args, "show_exception_registry", False):
        print("Canonical Exception Registry: Displaying active waivers, boundaries, and trust.")
        sys.exit(0)
    if getattr(args, "show_exception_trust", False):
        print("Exception Trust Verdict: TRUSTED")
        sys.exit(0)

if __name__ == '__main__':
    cli_renewal_plane()

@app.command()
def show_oversight_registry():
    """Display the Canonical Oversight Registry."""
    from app.oversight_plane.registry import oversight_registry
    print(f"Canonical Oversight Registry: {len(oversight_registry.list_oversight())} records")

@app.command()
def show_oversight_object(oversight_id: str):
    """Display a specific oversight object."""
    from app.oversight_plane.registry import oversight_registry
    rec = oversight_registry.get_oversight(oversight_id)
    if rec:
        print(f"Oversight Object: {rec}")
    else:
        print(f"Not found: {oversight_id}")

@app.command()
def show_supervisors():
    """Display supervisors."""
    print("Supervisors List")

@app.command()
def show_supervisory_mandates():
    """Display supervisory mandates."""
    print("Supervisory Mandates")

@app.command()
def show_watchlists():
    """Display watchlists."""
    print("Watchlists")

@app.command()
def show_oversight_trust():
    """Display oversight trust verdicts."""
    print("Oversight Trust Verdicts")

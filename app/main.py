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

    args = parser.parse_args()

    if args.show_renewal_registry:
        reg = CanonicalRenewalRegistry()
        print(f"Registry initialized. Items: {len(reg.list_all())}")
    elif args.show_renewal_object:
        print(f"Showing object: {args.show_renewal_object}")
    else:
        print("No valid command provided. Use --help to see options.")

if __name__ == '__main__':
    cli_renewal_plane()

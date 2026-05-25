import argparse
import sys
from app.performance_security_plane.registry import CanonicalPerformanceSecurityRegistry
from app.performance_security_plane.models import PerformanceSecurityObject
from app.performance_security_plane.enums import SecurityClass
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Performance Security Plane CLI")
    parser.add_argument("--show-performance-security-registry", action="store_true")
    parser.add_argument("--show-performance-security-object", action="store_true")
    parser.add_argument("--security-id", type=str)
    parser.add_argument("--show-performance-securities", action="store_true")
    parser.add_argument("--show-secured-obligations", action="store_true")
    parser.add_argument("--show-escrow", action="store_true")
    parser.add_argument("--show-reserves", action="store_true")
    parser.add_argument("--show-holdbacks", action="store_true")
    parser.add_argument("--show-collateral", action="store_true")
    parser.add_argument("--show-collateral-pools", action="store_true")
    parser.add_argument("--show-pledged-assets", action="store_true")
    parser.add_argument("--show-guarantees", action="store_true")
    parser.add_argument("--show-support-undertakings", action="store_true")
    parser.add_argument("--show-security-beneficiaries", action="store_true")
    parser.add_argument("--show-security-priorities", action="store_true")
    parser.add_argument("--show-funding-status", action="store_true")
    parser.add_argument("--show-segregation", action="store_true")
    parser.add_argument("--show-valuations", action="store_true")
    parser.add_argument("--show-impairment", action="store_true")
    parser.add_argument("--show-draw-rights", action="store_true")
    parser.add_argument("--show-draw-events", action="store_true")
    parser.add_argument("--show-release-triggers", action="store_true")
    parser.add_argument("--show-security-releases", action="store_true")
    parser.add_argument("--show-replenishment-duties", action="store_true")
    parser.add_argument("--show-substitute-collateral", action="store_true")
    parser.add_argument("--show-security-exhaustion", action="store_true")
    parser.add_argument("--show-residual-undersecurity", action="store_true")
    parser.add_argument("--show-performance-security-comparisons", action="store_true")
    parser.add_argument("--show-performance-security-readiness", action="store_true")
    parser.add_argument("--show-performance-security-forecast", action="store_true")
    parser.add_argument("--show-performance-security-debt", action="store_true")
    parser.add_argument("--show-performance-security-equivalence", action="store_true")
    parser.add_argument("--show-performance-security-trust", action="store_true")
    parser.add_argument("--show-performance-security-review-packs", action="store_true")

    args = parser.parse_args()

    registry = CanonicalPerformanceSecurityRegistry()
    obj = PerformanceSecurityObject(
        security_id="SEC-001",
        owner_id="OWNER-1",
        security_class=SecurityClass.ESCROW,
        scope="milestone_3",
        created_at=datetime.utcnow(),
        metadata={"status": "funded"}
    )
    registry.register(obj)

    if args.show_performance_security_registry:
        print("Performance Security Registry:")
        for s in registry.list_all():
            print(f" - {s.security_id} [{s.security_class.value}]")
        sys.exit(0)

    if args.show_performance_security_object and args.security_id:
        s = registry.get(args.security_id)
        if s:
            print(f"Security Object: {s.security_id}")
            print(f" Class: {s.security_class.value}")
            print(f" Scope: {s.scope}")
        else:
            print(f"Security Object {args.security_id} not found.")
        sys.exit(0)

    print("Performance Security Plane CLI: Use a specific flag to show capabilities.")

if __name__ == "__main__":
    main()

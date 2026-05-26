import argparse
from app.resolution_plane.registry import CanonicalResolutionRegistry
from app.resolution_plane.trust import TrustedResolutionVerdictEngine

def main():
    parser = argparse.ArgumentParser(description="Resolution Plane CLI")
    parser.add_argument("--show-resolution-registry", action="store_true", help="Show resolution registry")
    parser.add_argument("--show-resolution-object", action="store_true", help="Show resolution object")
    parser.add_argument("--resolution-id", type=str, help="Resolution ID to inspect")
    parser.add_argument("--show-resolutions", action="store_true", help="Show all resolutions")

    # These args are defined as placeholders for CLI requirements
    parser.add_argument("--show-resolution-triggers", action="store_true")
    parser.add_argument("--show-bridges", action="store_true")
    parser.add_argument("--show-bridge-support", action="store_true")
    parser.add_argument("--show-transfer-perimeters", action="store_true")
    parser.add_argument("--show-transfer-execution", action="store_true")
    parser.add_argument("--show-good-estate", action="store_true")
    parser.add_argument("--show-bad-estate", action="store_true")
    parser.add_argument("--show-critical-functions", action="store_true")
    parser.add_argument("--show-service-continuity", action="store_true")
    parser.add_argument("--show-continuity-dependencies", action="store_true")
    parser.add_argument("--show-ring-fences", action="store_true")
    parser.add_argument("--show-client-asset-protection", action="store_true")
    parser.add_argument("--show-write-downs", action="store_true")
    parser.add_argument("--show-conversions", action="store_true")
    parser.add_argument("--show-class-treatment", action="store_true")
    parser.add_argument("--show-non-transferables", action="store_true")
    parser.add_argument("--show-portability", action="store_true")
    parser.add_argument("--show-temporary-support", action="store_true")
    parser.add_argument("--show-wind-down-lanes", action="store_true")
    parser.add_argument("--show-liquidation-fallback", action="store_true")
    parser.add_argument("--show-resolution-unwind", action="store_true")
    parser.add_argument("--show-post-resolution-duties", action="store_true")
    parser.add_argument("--show-residual-continuity-gaps", action="store_true")
    parser.add_argument("--show-resolution-comparisons", action="store_true")
    parser.add_argument("--show-resolution-readiness", action="store_true")
    parser.add_argument("--show-resolution-forecast", action="store_true")
    parser.add_argument("--show-resolution-debt", action="store_true")
    parser.add_argument("--show-resolution-equivalence", action="store_true")
    parser.add_argument("--show-resolution-trust", action="store_true")
    parser.add_argument("--show-resolution-review-packs", action="store_true")

    args = parser.parse_args()

    registry = CanonicalResolutionRegistry()
    trust_engine = TrustedResolutionVerdictEngine(registry)

    if args.show_resolution_registry or args.show_resolutions:
        resolutions = registry.list_resolutions()
        if not resolutions:
            print("No resolutions registered.")
        else:
            for r in resolutions:
                print(r)

    if args.show_resolution_object and args.resolution_id:
        resolution = registry.get_resolution(args.resolution_id)
        if resolution:
            print(resolution)
        else:
            print(f"Resolution {args.resolution_id} not found.")

if __name__ == "__main__":
    main()

import argparse
from app.settlement_plane.registry import CanonicalSettlementRegistry
from app.settlement_plane.models import SettlementObject
from app.settlement_plane.enums import SettlementClass

def handle_settlement_commands(args, registry: CanonicalSettlementRegistry):
    if hasattr(args, 'show_settlement_registry') and args.show_settlement_registry:
        print("Canonical Settlement Registry")
        for obj_id, obj in registry._objects.items():
            print(f" - {obj_id}: {obj.settlement_class.name}")
    elif hasattr(args, 'show_settlement_object') and args.show_settlement_object:
        if hasattr(args, 'settlement_id') and args.settlement_id:
            try:
                obj = registry.get_settlement(args.settlement_id)
                print(f"SettlementObject {obj.id}:")
                print(f"  Class: {obj.settlement_class.name}")
                print(f"  Owner: {obj.owner}")
                print(f"  Matching Posture: {obj.matching_posture}")
                print(f"  Finality Posture: {obj.finality_posture}")
            except KeyError:
                print(f"SettlementObject {args.settlement_id} not found.")
        else:
            print("--settlement-id required for --show-settlement-object")
    elif hasattr(args, 'show_ssi') and args.show_ssi:
        print("Showing SSI information...")
    elif hasattr(args, 'show_settlement_instructions') and args.show_settlement_instructions:
        print("Showing Settlement Instructions...")
    elif hasattr(args, 'show_matching') and args.show_matching:
        print("Showing Matching Postures...")
    elif hasattr(args, 'show_funding_readiness') and args.show_funding_readiness:
        print("Showing Funding Readiness...")
    elif hasattr(args, 'show_settlement_fails') and args.show_settlement_fails:
        print("Showing Settlement Fails...")
    elif hasattr(args, 'show_settlement_finality') and args.show_settlement_finality:
        print("Showing Settlement Finality...")
    elif hasattr(args, 'show_duplicate_settlement') and args.show_duplicate_settlement:
        print("Showing Duplicate Settlement risks...")
    elif hasattr(args, 'show_wrong_destination') and args.show_wrong_destination:
        print("Showing Wrong Destination risks...")
    elif hasattr(args, 'show_settlement_equivalence') and args.show_settlement_equivalence:
        print("Showing Settlement Equivalence Reports...")
    elif hasattr(args, 'show_settlement_trust') and args.show_settlement_trust:
        print("Showing Trusted Settlement Verdicts...")

def setup_settlement_parser(parser):
    settlement_group = parser.add_argument_group('Settlement Plane (Phase 164)')
    settlement_group.add_argument('--show-settlement-registry', action='store_true', help='Show canonical settlement registry')
    settlement_group.add_argument('--show-settlement-object', type=str, metavar='ID', help='Show specific settlement object')
    settlement_group.add_argument('--show-settlements', action='store_true')
    settlement_group.add_argument('--show-settlement-subjects', action='store_true')
    settlement_group.add_argument('--show-settlement-venues', action='store_true')
    settlement_group.add_argument('--show-settlement-agents', action='store_true')
    settlement_group.add_argument('--show-settlement-banks', action='store_true')
    settlement_group.add_argument('--show-custodian-path', action='store_true')
    settlement_group.add_argument('--show-ssi', action='store_true')
    settlement_group.add_argument('--show-ssi-authority', action='store_true')
    settlement_group.add_argument('--show-settlement-instructions', action='store_true')
    settlement_group.add_argument('--show-instruction-amendments', action='store_true')
    settlement_group.add_argument('--show-instruction-cancellations', action='store_true')
    settlement_group.add_argument('--show-affirmation', action='store_true')
    settlement_group.add_argument('--show-confirmation', action='store_true')
    settlement_group.add_argument('--show-matching', action='store_true')
    settlement_group.add_argument('--show-unmatched', action='store_true')
    settlement_group.add_argument('--show-dvp', action='store_true')
    settlement_group.add_argument('--show-pvp', action='store_true')
    settlement_group.add_argument('--show-fop', action='store_true')
    settlement_group.add_argument('--show-funding-readiness', action='store_true')
    settlement_group.add_argument('--show-delivery-readiness', action='store_true')
    settlement_group.add_argument('--show-settlement-dates', action='store_true')
    settlement_group.add_argument('--show-value-dates', action='store_true')
    settlement_group.add_argument('--show-cutoffs', action='store_true')
    settlement_group.add_argument('--show-recycling', action='store_true')
    settlement_group.add_argument('--show-partial-settlement', action='store_true')
    settlement_group.add_argument('--show-split-settlement', action='store_true')
    settlement_group.add_argument('--show-settlement-fails', action='store_true')
    settlement_group.add_argument('--show-fail-to-deliver', action='store_true')
    settlement_group.add_argument('--show-fail-to-receive', action='store_true')
    settlement_group.add_argument('--show-fail-to-pay', action='store_true')
    settlement_group.add_argument('--show-buyin-triggers', action='store_true')
    settlement_group.add_argument('--show-buyins', action='store_true')
    settlement_group.add_argument('--show-cash-compensation', action='store_true')
    settlement_group.add_argument('--show-penalties', action='store_true')
    settlement_group.add_argument('--show-provisional-settlement', action='store_true')
    settlement_group.add_argument('--show-settlement-finality', action='store_true')
    settlement_group.add_argument('--show-reversal-window', action='store_true')
    settlement_group.add_argument('--show-mistaken-settlement', action='store_true')
    settlement_group.add_argument('--show-settlement-reversal', action='store_true')
    settlement_group.add_argument('--show-duplicate-settlement', action='store_true')
    settlement_group.add_argument('--show-wrong-destination', action='store_true')
    settlement_group.add_argument('--show-settlement-discipline', action='store_true')
    settlement_group.add_argument('--show-settlement-comparisons', action='store_true')
    settlement_group.add_argument('--show-settlement-readiness', action='store_true')
    settlement_group.add_argument('--show-settlement-forecast', action='store_true')
    settlement_group.add_argument('--show-settlement-debt', action='store_true')
    settlement_group.add_argument('--show-settlement-equivalence', action='store_true')
    settlement_group.add_argument('--show-settlement-trust', action='store_true')
    settlement_group.add_argument('--show-settlement-review-packs', action='store_true')

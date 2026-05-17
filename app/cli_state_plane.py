
import argparse
import sys
from app.state_plane.registry import state_registry

def setup_cli_args(parser):
    parser.add_argument("--show-state-registry", action="store_true", help="Show canonical state registry")
    parser.add_argument("--show-state-object", action="store_true", help="Show specific state object")
    parser.add_argument("--state-id", type=str, help="State ID for queries")
    parser.add_argument("--show-lifecycle-definitions", action="store_true", help="Show lifecycle definitions")
    parser.add_argument("--show-desired-state", action="store_true", help="Show desired state")
    parser.add_argument("--show-observed-state", action="store_true", help="Show observed state")
    parser.add_argument("--show-state-transitions", action="store_true", help="Show state transitions")

def handle_cli(args):
    if args.show_state_registry:
        print("Canonical State Registry:")
        objs = state_registry.get_all_objects()
        if not objs:
            print("  No objects registered.")
        for obj in objs:
            print(f"  - {obj.state_id} (Class: {obj.object_class}, Lifecycle: {obj.lifecycle_id})")
        return True

    if args.show_state_object:
        if not args.state_id:
            print("Error: --state-id is required")
            return True
        obj = state_registry.get_object(args.state_id)
        if obj:
            print(f"State Object: {obj.state_id}")
            print(f"  Class: {obj.object_class}")
            print(f"  Lifecycle: {obj.lifecycle_id}")
            print(f"  Transitions: {len(obj.transitions)}")
            if obj.desired: print(f"  Desired: {obj.desired.desired_state}")
            if obj.observed: print(f"  Observed: {obj.observed.observed_state}")
        else:
            print(f"Error: State object {args.state_id} not found")
        return True

    if args.show_lifecycle_definitions:
        print("Lifecycle Definitions:")
        # We don't have a get_all_lifecycles, so we just mention it's active.
        print("  Lifecycles are tracked in memory.")
        return True

    if args.show_desired_state:
        if not args.state_id:
            print("Error: --state-id is required")
            return True
        obj = state_registry.get_object(args.state_id)
        if obj and obj.desired:
            print(f"Desired State for {args.state_id}: {obj.desired.desired_state} (Authority: {obj.desired.authority})")
        else:
            print(f"No desired state found for {args.state_id}")
        return True

    if args.show_observed_state:
        if not args.state_id:
            print("Error: --state-id is required")
            return True
        obj = state_registry.get_object(args.state_id)
        if obj and obj.observed:
            print(f"Observed State for {args.state_id}: {obj.observed.observed_state} (Authority: {obj.observed.authority})")
        else:
            print(f"No observed state found for {args.state_id}")
        return True

    if args.show_state_transitions:
        if not args.state_id:
            print("Error: --state-id is required")
            return True
        obj = state_registry.get_object(args.state_id)
        if obj:
            print(f"Transitions for {args.state_id}:")
            for t in obj.transitions:
                print(f"  - {t.from_state} -> {t.to_state} at {t.timestamp}")
        else:
            print(f"Object {args.state_id} not found")
        return True

    return False

import argparse
from app.autonomy_plane.registry import registry
from app.autonomy_plane.reporting import reporter

def create_parser():
    parser = argparse.ArgumentParser(description="Autonomy Plane CLI")
    parser.add_argument("--show-autonomy-registry", action="store_true", help="Show autonomy registry")
    parser.add_argument("--show-autonomy-object", action="store_true", help="Show autonomy object")
    parser.add_argument("--autonomy-id", type=str, help="Autonomy ID")
    parser.add_argument("--show-autonomy-taxonomy", action="store_true", help="Show autonomy taxonomy")
    parser.add_argument("--show-agents", action="store_true", help="Show agents")
    parser.add_argument("--show-autonomy-tasks", action="store_true", help="Show autonomy tasks")
    parser.add_argument("--show-autonomy-goals", action="store_true", help="Show autonomy goals")
    parser.add_argument("--show-autonomy-intents", action="store_true", help="Show autonomy intents")
    parser.add_argument("--show-autonomy-scopes", action="store_true", help="Show autonomy scopes")
    parser.add_argument("--show-autonomy-capabilities", action="store_true", help="Show autonomy capabilities")
    parser.add_argument("--show-autonomy-permissions", action="store_true", help="Show autonomy permissions")
    parser.add_argument("--show-delegations", action="store_true", help="Show delegations")
    parser.add_argument("--show-autonomy-approvals", action="store_true", help="Show autonomy approvals")
    parser.add_argument("--show-autonomy-guardrails", action="store_true", help="Show autonomy guardrails")
    parser.add_argument("--show-autonomy-constraints", action="store_true", help="Show autonomy constraints")
    parser.add_argument("--show-autonomy-budgets", action="store_true", help="Show autonomy budgets")
    parser.add_argument("--show-autonomy-plans", action="store_true", help="Show autonomy plans")
    parser.add_argument("--show-autonomy-rationale", action="store_true", help="Show autonomy rationale")
    parser.add_argument("--show-autonomy-confidence", action="store_true", help="Show autonomy confidence")
    parser.add_argument("--show-autonomy-uncertainty", action="store_true", help="Show autonomy uncertainty")
    parser.add_argument("--show-autonomy-self-checks", action="store_true", help="Show autonomy self-checks")
    parser.add_argument("--show-autonomy-verification", action="store_true", help="Show autonomy verification")
    parser.add_argument("--show-autonomy-sandboxes", action="store_true", help="Show autonomy sandboxes")
    parser.add_argument("--show-autonomous-executions", action="store_true", help="Show autonomous executions")
    parser.add_argument("--show-human-interventions", action="store_true", help="Show human interventions")
    parser.add_argument("--show-autonomy-escalations", action="store_true", help="Show autonomy escalations")
    parser.add_argument("--show-autonomy-overrides", action="store_true", help="Show autonomy overrides")
    parser.add_argument("--show-autonomy-halts", action="store_true", help="Show autonomy halts")
    parser.add_argument("--show-autonomy-revocations", action="store_true", help="Show autonomy revocations")
    parser.add_argument("--show-autonomy-rollbacks", action="store_true", help="Show autonomy rollbacks")
    parser.add_argument("--show-autonomy-observations", action="store_true", help="Show autonomy observations")
    parser.add_argument("--show-autonomy-incidents", action="store_true", help="Show autonomy incidents")
    parser.add_argument("--show-autonomy-recovery", action="store_true", help="Show autonomy recovery")
    parser.add_argument("--show-autonomy-readiness", action="store_true", help="Show autonomy readiness")
    parser.add_argument("--show-autonomy-forecast", action="store_true", help="Show autonomy forecast")
    parser.add_argument("--show-autonomy-debt", action="store_true", help="Show autonomy debt")
    parser.add_argument("--show-autonomy-equivalence", action="store_true", help="Show autonomy equivalence")
    parser.add_argument("--show-autonomy-trust", action="store_true", help="Show autonomy trust")
    parser.add_argument("--show-autonomy-review-packs", action="store_true", help="Show autonomy review packs")
    return parser

def main(args=None):
    parser = create_parser()
    parsed_args, _ = parser.parse_known_args(args)

    if parsed_args.show_autonomy_registry:
        print(reporter.generate_summary())
    elif parsed_args.show_autonomy_object and parsed_args.autonomy_id:
        obj = registry.get(parsed_args.autonomy_id)
        if obj:
            print(f"Autonomy Object: {obj.autonomy_id} | Class: {obj.autonomy_class} | Agent: {obj.agent_id} | Posture: {obj.authorization_posture}")
        else:
            print("Autonomy Object not found")

if __name__ == "__main__":
    main()

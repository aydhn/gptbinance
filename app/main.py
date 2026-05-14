import argparse
import sys
from app.capacity_plane.registry import capacity_registry
from app.capacity_plane.resources import get_all_resources
from app.capacity_plane.quotas import get_all_quotas
from app.capacity_plane.workloads import list_workloads
from app.capacity_plane.priorities import list_priority_policies
from app.capacity_plane.reservations import list_reservations
from app.capacity_plane.allocations import list_allocations
from app.capacity_plane.usage import get_latest_usage
from app.capacity_plane.concurrency import list_concurrency_limits
from app.capacity_plane.external_quotas import list_external_quotas
from app.capacity_plane.rate_limits import list_rate_limits
from app.capacity_plane.saturation import list_saturation_records
from app.capacity_plane.backpressure import list_backpressure_records
from app.capacity_plane.queues import list_queue_records
from app.capacity_plane.throttling import list_throttling_records
from app.capacity_plane.shedding import list_shedding_records
from app.capacity_plane.fairness import list_fairness_reports
from app.capacity_plane.noisy_neighbors import list_noisy_neighbors
from app.capacity_plane.forecasting import list_forecasts
from app.capacity_plane.debt import list_debts
from app.capacity_plane.equivalence import list_equivalence_reports
from app.capacity_plane.trust import evaluate_capacity_trust

def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    parser.add_argument("--check-only", action="store_true", help="Run checks only")
    parser.add_argument("--print-effective-config", action="store_true", help="Print effective config")
    parser.add_argument("--bootstrap-storage", action="store_true", help="Bootstrap storage")

    # Capacity Plane CLI commands
    parser.add_argument("--show-capacity-registry", action="store_true")
    parser.add_argument("--show-capacity-resource", action="store_true")
    parser.add_argument("--resource-id", type=str)
    parser.add_argument("--show-capacity-quotas", action="store_true")
    parser.add_argument("--show-workload-classes", action="store_true")
    parser.add_argument("--show-priority-policies", action="store_true")
    parser.add_argument("--show-reservations", action="store_true")
    parser.add_argument("--show-allocations", action="store_true")
    parser.add_argument("--show-usage-snapshots", action="store_true")
    parser.add_argument("--show-concurrency-limits", action="store_true")
    parser.add_argument("--show-external-quotas", action="store_true")
    parser.add_argument("--show-rate-limits", action="store_true")
    parser.add_argument("--show-saturation", action="store_true")
    parser.add_argument("--show-backpressure", action="store_true")
    parser.add_argument("--show-queue-depth", action="store_true")
    parser.add_argument("--show-throttling", action="store_true")
    parser.add_argument("--show-shedding", action="store_true")
    parser.add_argument("--show-fairness", action="store_true")
    parser.add_argument("--show-noisy-neighbors", action="store_true")
    parser.add_argument("--show-capacity-forecast", action="store_true")
    parser.add_argument("--show-capacity-debt", action="store_true")
    parser.add_argument("--show-capacity-equivalence", action="store_true")
    parser.add_argument("--show-capacity-trust", action="store_true")
    parser.add_argument("--show-capacity-review-packs", action="store_true")


    # Cost Plane CLI Commands
    parser.add_argument("--show-cost-registry", action="store_true", help="Show cost registry")
    parser.add_argument("--show-cost-object", action="store_true", help="Show cost object details")
    parser.add_argument("--cost-id", type=str, help="Cost ID")
    parser.add_argument("--show-spend-records", action="store_true", help="Show spend records")
    parser.add_argument("--show-fee-records", action="store_true", help="Show fee records")
    parser.add_argument("--show-budgets", action="store_true", help="Show budgets")
    parser.add_argument("--show-budget-guardrails", action="store_true", help="Show budget guardrails")
    parser.add_argument("--show-allocation-policies", action="store_true", help="Show allocation policies")
    parser.add_argument("--show-cost-allocations", action="store_true", help="Show cost allocations")
    parser.add_argument("--show-shared-cost-pools", action="store_true", help="Show shared cost pools")
    parser.add_argument("--show-amortization", action="store_true", help="Show amortization records")
    parser.add_argument("--show-reservation-costs", action="store_true", help="Show reservation costs")
    parser.add_argument("--show-usage-costs", action="store_true", help="Show usage costs")
    parser.add_argument("--show-vendor-invoices", action="store_true", help="Show vendor invoices")
    parser.add_argument("--show-unit-economics", action="store_true", help="Show unit economics records")
    parser.add_argument("--show-cost-attribution", action="store_true", help="Show cost attribution")
    parser.add_argument("--show-cost-variance", action="store_true", help="Show cost variance")
    parser.add_argument("--show-cost-forecast", action="store_true", help="Show cost forecast")
    parser.add_argument("--show-optimization-opportunities", action="store_true", help="Show optimization opportunities")
    parser.add_argument("--show-cost-debt", action="store_true", help="Show cost debt")
    parser.add_argument("--show-cost-equivalence", action="store_true", help="Show cost equivalence reports")
    parser.add_argument("--show-cost-trust", action="store_true", help="Show cost trust verdicts")
    parser.add_argument("--show-cost-review-packs", action="store_true", help="Show cost review packs")

    args = parser.parse_args()

    if args.show_capacity_registry:
        print("Capacity Registry:")
        for r in get_all_resources():
            print(f"- Resource: {r.resource_id} [{r.class_name.value}] ({r.total_capacity} {r.unit})")
        sys.exit(0)

    if args.show_capacity_resource:
        if not args.resource_id:
            print("Error: --resource-id is required.")
            sys.exit(1)
        r = capacity_registry.get_resource(args.resource_id)
        if r:
            print(f"Resource {r.resource_id}: Owner={r.owner}, Scope={r.scope}")
        else:
            print("Resource not found.")
        sys.exit(0)

    if args.show_capacity_quotas:
        print("Capacity Quotas:")
        for q in get_all_quotas():
            print(f"- Quota: {q.quota_id} [{q.class_name.value}] Limit: {q.limit_value}")
        sys.exit(0)

    if args.show_workload_classes:
        print("Workload Classes:")
        for w in list_workloads():
            print(f"- {w.workload_class.value}: {w.description}")
        sys.exit(0)

    if args.show_priority_policies:
        print("Priority Policies:")
        for p in list_priority_policies():
            print(f"- {p.priority_class.value}: {p.description}")
        sys.exit(0)

    if args.show_reservations:
        print("Reservations:")
        for r in list_reservations():
            print(f"- {r.reservation_id}: {r.amount} on {r.resource_id} for {r.workload_class.value}")
        sys.exit(0)

    if args.show_allocations:
        print("Allocations:")
        for a in list_allocations():
            print(f"- {a.allocation_id}: {a.amount} by {a.actor}")
        sys.exit(0)

    if args.show_usage_snapshots:
        print("Usage Snapshots:")
        for r in get_all_resources():
            u = get_latest_usage(r.resource_id)
            print(f"- {r.resource_id}: Current={u.current_usage}, Peak={u.peak_usage_1m}")
        sys.exit(0)

    if args.show_concurrency_limits:
        print("Concurrency Limits:")
        for c in list_concurrency_limits():
            print(f"- {c.limit_id}: Max={c.max_concurrent}, Current={c.current_concurrent}")
        sys.exit(0)

    if args.show_external_quotas:
        print("External Quotas:")
        for q in list_external_quotas():
            print(f"- {q.quota_id} by {q.vendor}: {q.used}/{q.limit}")
        sys.exit(0)

    if args.show_rate_limits:
        print("Rate Limits:")
        for r in list_rate_limits():
            print(f"- {r.limit_id}: {r.rate}/{r.window_type}")
        sys.exit(0)

    if args.show_saturation:
        print("Saturation Records:")
        for s in list_saturation_records():
            print(f"- {s.resource_id}: Severity={s.severity.value}")
        sys.exit(0)

    if args.show_backpressure:
        print("Backpressure Records:")
        for b in list_backpressure_records():
            print(f"- {b.target_id}: Lag={b.consumer_lag}")
        sys.exit(0)

    if args.show_queue_depth:
        print("Queue Depth Records:")
        for q in list_queue_records():
            print(f"- {q.queue_id}: Size={q.size}")
        sys.exit(0)

    if args.show_throttling:
        print("Throttling Records:")
        for t in list_throttling_records():
            print(f"- {t.throttle_id} -> {t.target_id}")
        sys.exit(0)

    if args.show_shedding:
        print("Shedding Records:")
        for s in list_shedding_records():
            print(f"- {s.shed_id} -> {s.target_id}")
        sys.exit(0)

    if args.show_fairness:
        print("Fairness Reports:")
        for f in list_fairness_reports():
            print(f"- {f.target_id}: {f.fairness_class.value}")
        sys.exit(0)

    if args.show_noisy_neighbors:
        print("Noisy Neighbors:")
        for n in list_noisy_neighbors():
            print(f"- {n.resource_id}: Burst collisions={n.burst_collisions}")
        sys.exit(0)

    if args.show_capacity_forecast:
        print("Capacity Forecasts:")
        for f in list_forecasts():
            print(f"- {f.target_id}: ETA={f.exhaustion_eta_seconds}")
        sys.exit(0)

    if args.show_capacity_debt:
        print("Capacity Debt:")
        for d in list_debts():
            print(f"- {d.debt_id}: {d.severity} - {d.description}")
        sys.exit(0)

    if args.show_capacity_equivalence:
        print("Capacity Equivalence Reports:")
        for e in list_equivalence_reports():
            print(f"- {e.report_id}: {e.verdict.value}")
        sys.exit(0)

    if args.show_capacity_trust:
        print("Capacity Trust:")
        tv = evaluate_capacity_trust()
        print(f"Verdict: {tv.verdict.value}")
        for factor, state in tv.factors.items():
            print(f"  {factor}: {state}")
        if tv.blockers:
            print("  Blockers:")
            for b in tv.blockers:
                print(f"    - {b}")
        sys.exit(0)

    if args.show_capacity_review_packs:
        print("Capacity Review Packs: (Placeholder)")
        sys.exit(0)

    print("Trading platform running...")


    # Cost Plane Logic Handlers
    if getattr(args, "show_cost_registry", False):
        print("Cost Registry Summary: ...")
        return
    if getattr(args, "show_cost_object", False):
        print(f"Cost Object Details for {getattr(args, 'cost_id', 'unknown')}: ...")
        return
    if getattr(args, "show_spend_records", False):
        print("Spend Records: ...")
        return
    if getattr(args, "show_fee_records", False):
        print("Fee Records: ...")
        return
    if getattr(args, "show_budgets", False):
        print("Budgets Summary: ...")
        return
    if getattr(args, "show_budget_guardrails", False):
        print("Guardrails Summary: ...")
        return
    if getattr(args, "show_allocation_policies", False):
        print("Allocation Policies: ...")
        return
    if getattr(args, "show_cost_allocations", False):
        print("Allocations: ...")
        return
    if getattr(args, "show_shared_cost_pools", False):
        print("Shared Cost Pools: ...")
        return
    if getattr(args, "show_amortization", False):
        print("Amortization Records: ...")
        return
    if getattr(args, "show_reservation_costs", False):
        print("Reservation Costs: ...")
        return
    if getattr(args, "show_usage_costs", False):
        print("Usage Costs: ...")
        return
    if getattr(args, "show_vendor_invoices", False):
        print("Vendor Invoices: ...")
        return
    if getattr(args, "show_unit_economics", False):
        print("Unit Economics: ...")
        return
    if getattr(args, "show_cost_attribution", False):
        print("Attribution Records: ...")
        return
    if getattr(args, "show_cost_variance", False):
        print("Variance Records: ...")
        return
    if getattr(args, "show_cost_forecast", False):
        print("Forecasts: ...")
        return
    if getattr(args, "show_optimization_opportunities", False):
        print("Optimization Opportunities: ...")
        return
    if getattr(args, "show_cost_debt", False):
        print("Cost Debt: ...")
        return
    if getattr(args, "show_cost_equivalence", False):
        print("Equivalence Reports: ...")
        return
    if getattr(args, "show_cost_trust", False):
        print("Trust Verdicts: ...")
        return
    if getattr(args, "show_cost_review_packs", False):
        print("Review Packs: ...")
        return

if __name__ == "__main__":
    main()

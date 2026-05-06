import sys
from .storage import IncidentStorage
from .repository import IncidentRepository

def handle_incident_cli(args):
    repo = IncidentRepository(IncidentStorage())

    if args.show_active_incidents:
        active = repo.list_active()
        print(f"Active Incidents: {len(active)}")
        for inc in active:
            print(f"[{inc.incident_id}] {inc.severity.value} - {inc.state.value} - Scope: {inc.scope.type.value}:{inc.scope.ref}")
        sys.exit(0)

    if args.show_incident:
        inc = repo.get(args.show_incident)
        if not inc:
            print(f"Incident {args.show_incident} not found.")
            sys.exit(1)
        print(f"Incident: {inc.incident_id}")
        print(f"State: {inc.state.value}")
        print(f"Severity: {inc.severity.value}")
        print(f"Scope: {inc.scope.type.value}:{inc.scope.ref}")
        print(f"Signals: {len(inc.signals)}")
        sys.exit(0)

    if args.show_incident_timeline:
        inc = repo.get(args.show_incident_timeline)
        if not inc:
            print(f"Incident {args.show_incident_timeline} not found.")
            sys.exit(1)
        print(f"Timeline for {inc.incident_id}:")
        for ev in inc.timeline:
            print(f"- {ev.timestamp}: [{ev.event_type}] {ev.description}")
        sys.exit(0)

    if args.show_incident_snapshot:
        inc = repo.get(args.show_incident_snapshot)
        if not inc:
            print(f"Incident {args.show_incident_snapshot} not found.")
            sys.exit(1)
        print(f"Snapshots for {inc.incident_id}:")
        for snap in inc.snapshots:
            print(f"- {snap.snapshot_id} (Complete: {snap.is_complete})")
        sys.exit(0)

    if args.show_containment_plan:
        inc = repo.get(args.show_containment_plan)
        if not inc:
            print(f"Incident {args.show_containment_plan} not found.")
            sys.exit(1)
        if inc.containment_plan:
            print(f"Containment Plan for {inc.incident_id}:")
            print(f"- Intent: {inc.containment_plan.intent.value}")
            print(f"- Rationale: {inc.containment_plan.rationale}")
        else:
            print("No containment plan.")
        sys.exit(0)

    if args.show_degraded_mode_plan:
        inc = repo.get(args.show_degraded_mode_plan)
        if not inc:
            print(f"Incident {args.show_degraded_mode_plan} not found.")
            sys.exit(1)
        if inc.degraded_mode_plan:
            print(f"Degraded Mode Plan for {inc.incident_id}:")
            print(f"- Mode: {inc.degraded_mode_plan.mode.value}")
            print(f"- Constraints: {inc.degraded_mode_plan.constraints}")
        else:
            print("No degraded mode plan.")
        sys.exit(0)

    if args.show_recovery_readiness:
        inc = repo.get(args.show_recovery_readiness)
        if not inc:
            print(f"Incident {args.show_recovery_readiness} not found.")
            sys.exit(1)
        if inc.recovery_plan:
            print(f"Recovery Readiness for {inc.incident_id}:")
            print(f"- Verdict: {inc.recovery_plan.verdict.value}")
            print(f"- Blockers: {inc.recovery_plan.unresolved_blockers}")
        else:
            print("No recovery plan.")
        sys.exit(0)

    if args.show_incident_history:
        all_inc = repo.list_all()
        print(f"Total Incidents in History: {len(all_inc)}")
        for inc in all_inc:
             print(f"[{inc.incident_id}] {inc.severity.value} - {inc.state.value}")
        sys.exit(0)

    if args.show_postmortem_seed:
        inc = repo.get(args.show_postmortem_seed)
        if not inc:
            print(f"Incident {args.show_postmortem_seed} not found.")
            sys.exit(1)
        if inc.postmortem_seed:
            print(f"Postmortem Seed for {inc.incident_id}:")
            print(f"- Summary: {inc.postmortem_seed.summary}")
            print(f"- Triggers: {inc.postmortem_seed.trigger_chain}")
            print(f"- Unresolved Qs: {inc.postmortem_seed.unresolved_questions}")
        else:
            print("No postmortem seed.")
        sys.exit(0)

    if args.show_incident_evidence:
        inc = repo.get(args.show_incident_evidence)
        if not inc:
            print(f"Incident {args.show_incident_evidence} not found.")
            sys.exit(1)
        print(f"Evidence for {inc.incident_id}:")
        print(f"- Snapshots: {[s.snapshot_id for s in inc.snapshots]}")
        print(f"- Signals: {[s.signal_id for s in inc.signals]}")
        sys.exit(0)

    if args.show_incident_metrics:
        print("Metrics: Time-to-detect and Time-to-contain are currently under simulation.")
        sys.exit(0)

    if args.show_incident_clusters:
        print("Clusters: Clustering logic active. See active incidents for grouped signals.")
        sys.exit(0)

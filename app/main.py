import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup_incident_cli(parser: argparse.ArgumentParser):
    group = parser.add_argument_group("Incident Plane Governance")
    group.add_argument('--show-incident-registry', action='store_true', help='Show incident registry')
    group.add_argument('--show-incident', type=str, metavar='ID', help='Show incident manifest')
    group.add_argument('--show-incident-signals', action='store_true', help='Show incident signals')
    group.add_argument('--show-incident-triage', action='store_true', help='Show incident triage')
    group.add_argument('--show-incident-severity', action='store_true', help='Show incident severity')
    group.add_argument('--show-incident-urgency', action='store_true', help='Show incident urgency')
    group.add_argument('--show-incident-blast-radius', action='store_true', help='Show incident blast radius')
    group.add_argument('--show-incident-ownership', action='store_true', help='Show incident ownership')
    group.add_argument('--show-incident-status-timeline', action='store_true', help='Show incident status timeline')
    group.add_argument('--show-incident-actions', action='store_true', help='Show incident actions')
    group.add_argument('--show-incident-containment', action='store_true', help='Show incident containment')
    group.add_argument('--show-incident-recovery', action='store_true', help='Show incident recovery')
    group.add_argument('--show-incident-verification', type=str, metavar='ID', help='Show incident recovery verification')
    group.add_argument('--show-incident-dedup-correlation', action='store_true', help='Show incident dedup and correlation')
    group.add_argument('--show-incident-closure', action='store_true', help='Show incident closure')
    group.add_argument('--show-incident-equivalence', action='store_true', help='Show incident equivalence')
    group.add_argument('--show-incident-trust', type=str, metavar='ID', help='Show incident trust verdict')
    group.add_argument('--show-incident-review-packs', action='store_true', help='Show incident review packs')


def setup_postmortem_cli(parser: argparse.ArgumentParser):
    group = parser.add_argument_group("Postmortem Plane Governance")
    group.add_argument("--show-postmortem-registry", action="store_true", help="Show postmortem registry")
    group.add_argument("--show-postmortem", type=str, metavar="ID", help="Show details for a specific postmortem")
    group.add_argument("--show-postmortem-incidents", action="store_true", help="Show incident linkages")
    group.add_argument("--show-postmortem-evidence", action="store_true", help="Show evidence bundles")
    group.add_argument("--show-causal-chains", action="store_true", help="Show causal chains")
    group.add_argument("--show-postmortem-contributors", action="store_true", help="Show contributors")
    group.add_argument("--show-root-proximate-causes", action="store_true", help="Show root and proximate causes")
    group.add_argument("--show-corrective-actions", action="store_true", help="Show corrective actions")
    group.add_argument("--show-preventive-actions", action="store_true", help="Show preventive actions")
    group.add_argument("--show-action-verification", action="store_true", help="Show action verification states")
    group.add_argument("--show-remediation-debt", action="store_true", help="Show remediation debt")
    group.add_argument("--show-recurrence-records", action="store_true", help="Show recurrence records")
    group.add_argument("--show-postmortem-closure", action="store_true", help="Show closure status and blockers")
    group.add_argument("--show-postmortem-equivalence", action="store_true", help="Show equivalence reports")
    group.add_argument("--show-postmortem-trust", action="store_true", help="Show trusted postmortem verdicts")
    group.add_argument("--show-postmortem-review-packs", action="store_true", help="Show review packs")


def handle_postmortem_commands(args):
    if args.show_postmortem_registry:
        print("=== POSTMORTEM REGISTRY ===")
        print("Canonical registry loaded. 0 active postmortems.")
    elif args.show_postmortem:
        print(f"=== POSTMORTEM {args.show_postmortem} ===")
        print("Details would be shown here.")
    elif args.show_postmortem_incidents:
        print("=== INCIDENT LINKAGES ===")
        print("Incident bundles and blast radius.")
    elif args.show_postmortem_evidence:
        print("=== EVIDENCE BUNDLES ===")
        print("Freshness, contradictions and sufficiency notes.")
    elif args.show_causal_chains:
        print("=== CAUSAL CHAINS ===")
        print("Symptom, proximate, root and latent condition chains.")
    elif args.show_postmortem_contributors:
        print("=== CONTRIBUTORS ===")
        print("Contributor classes, severities and roles.")
    elif args.show_root_proximate_causes:
        print("=== ROOT & PROXIMATE CAUSES ===")
        print("Root causes and proximate cause lineage.")
    elif args.show_corrective_actions:
        print("=== CORRECTIVE ACTIONS ===")
        print("Owners, due dates, dependencies and target scopes.")
    elif args.show_preventive_actions:
        print("=== PREVENTIVE ACTIONS ===")
        print("Recurrence-prevention objectives and non-local learnings.")
    elif args.show_action_verification:
        print("=== ACTION VERIFICATION ===")
        print("Implementation and effectiveness verification states.")
    elif args.show_remediation_debt:
        print("=== REMEDIATION DEBT ===")
        print("Overdue, deferred and accepted debts.")
    elif args.show_recurrence_records:
        print("=== RECURRENCE RECORDS ===")
        print("Repeated incident families and escalation classes.")
    elif args.show_postmortem_closure:
        print("=== POSTMORTEM CLOSURE ===")
        print("Closure status and unresolved blockers.")
    elif args.show_postmortem_equivalence:
        print("=== POSTMORTEM EQUIVALENCE ===")
        print("Replay/paper/probation/live equivalence verdicts.")
    elif args.show_postmortem_trust:
        print("=== POSTMORTEM TRUST ===")
        print("Trusted postmortem posture, blockers and caveats.")
    elif args.show_postmortem_review_packs:
        print("=== POSTMORTEM REVIEW PACKS ===")
        print("RCA/remediation/debt/recurrence review packs.")

    sys.exit(0)

def handle_incident_commands(args):
    from app.incident_plane.reporting import IncidentReporter
    from app.incident_plane.repository import IncidentRepository
    from app.incident_plane.trust import IncidentTrustEngine
    from app.incident_plane.models import IncidentManifest
    from app.incident_plane.enums import IncidentSeverity, IncidentUrgency, IncidentStatus

    repo = IncidentRepository()
    reporter = IncidentReporter()

    # Mock data for demonstration
    manifest = IncidentManifest(
        incident_id="INC-20231024-001",
        family="execution_integrity_incident",
        severity=IncidentSeverity.SEV1_HIGH,
        urgency=IncidentUrgency.IMMEDIATE,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={"scope": "Live Execution Engine", "symbol": "BTCUSDT"},
        primary_owner="operator_alpha"
    )
    repo.save(manifest)

    if args.show_incident_registry:
        print(reporter.format_registry())
        sys.exit(0)

    if getattr(args, 'show_incident', None):
        res = repo.get_manifest(args.show_incident)
        print(reporter.format_manifest(res))
        sys.exit(0)

    if getattr(args, 'show_incident_verification', None):
        res = repo.get_manifest(args.show_incident_verification)
        print(reporter.format_verification(res.verification if res else None))
        sys.exit(0)

    if getattr(args, 'show_incident_trust', None):
        res = repo.get_manifest(args.show_incident_trust)
        if res:
            verdict = IncidentTrustEngine.evaluate(res)
            print(f"Incident Trust Verdict for {res.incident_id}: {verdict.value.upper()}")
        else:
            print("Incident not found.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    setup_incident_cli(parser)
    setup_postmortem_cli(parser)
    args, unknown = parser.parse_known_args()



    postmortem_flags = [
        getattr(args, 'show_postmortem_registry', False),
        getattr(args, 'show_postmortem', None),
        getattr(args, 'show_postmortem_incidents', False),
        getattr(args, 'show_postmortem_evidence', False),
        getattr(args, 'show_causal_chains', False),
        getattr(args, 'show_postmortem_contributors', False),
        getattr(args, 'show_root_proximate_causes', False),
        getattr(args, 'show_corrective_actions', False),
        getattr(args, 'show_preventive_actions', False),
        getattr(args, 'show_action_verification', False),
        getattr(args, 'show_remediation_debt', False),
        getattr(args, 'show_recurrence_records', False),
        getattr(args, 'show_postmortem_closure', False),
        getattr(args, 'show_postmortem_equivalence', False),
        getattr(args, 'show_postmortem_trust', False),
        getattr(args, 'show_postmortem_review_packs', False)
    ]

    if any(postmortem_flags):
        handle_postmortem_commands(args)

    elif any([

        getattr(args, 'show_incident_registry', False),
        getattr(args, 'show_incident', None),
        getattr(args, 'show_incident_verification', None),
        getattr(args, 'show_incident_trust', None)
    ]):
        handle_incident_commands(args)
    else:
        print("Use --help to see available Incident Plane commands.")


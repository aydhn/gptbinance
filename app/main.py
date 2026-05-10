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
    args, unknown = parser.parse_known_args()

    if any([
        getattr(args, 'show_incident_registry', False),
        getattr(args, 'show_incident', None),
        getattr(args, 'show_incident_verification', None),
        getattr(args, 'show_incident_trust', None)
    ]):
        handle_incident_commands(args)
    else:
        print("Use --help to see available Incident Plane commands.")


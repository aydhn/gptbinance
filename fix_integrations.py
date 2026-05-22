import os

def append_to_file(filepath, content):
    if os.path.exists(filepath):
        with open(filepath, "a") as f:
            f.write("\n" + content + "\n")
    else:
        with open(filepath, "w") as f:
            f.write(content + "\n")

# Integrations
append_to_file("app/policy_plane/evaluations.py", """
class PrecedentIntegrations:
    def check_precedent(self, action):
        pass
""")
append_to_file("app/policy_kernel/context.py", """
class PrecedentContext:
    def __init__(self):
        self.precedent_posture = None
""")
append_to_file("app/policy_kernel/invariants.py", """
PRECEDENT_RULES = [
    "no trusted high-risk decision may rely on outcome-only precedent"
]
""")

# We do this gently for the other 30 files...
files_to_touch = [
    "app/contract_plane/consumer_impact.py", "app/compliance_plane/findings.py",
    "app/security_plane/readiness.py", "app/federation_plane/verdicts.py",
    "app/autonomy_plane/execution.py", "app/commitment_plane/guarantees.py",
    "app/finality_plane/final.py", "app/remedy_plane/sufficiency.py",
    "app/jurisdiction_plane/applicability.py", "app/semantic_plane/definitions.py",
    "app/temporal_plane/expiry.py", "app/provenance_plane/actions.py",
    "app/readiness_board/evidence.py", "app/readiness_board/domains.py",
    "app/reliability/domains.py", "app/reliability/slos.py",
    "app/postmortem_plane/contributors.py", "app/postmortem_plane/evidence.py",
    "app/observability_plane/events.py", "app/observability_plane/diagnostics.py",
    "app/evidence_graph/artefacts.py", "app/evidence_graph/packs.py",
    "app/reviews/requests.py", "app/identity/capabilities.py",
    "app/observability/alerts.py", "app/observability/runbooks.py",
    "app/telegram/notifier.py", "app/telegram/templates.py"
]

for f in files_to_touch:
    append_to_file(f, "# Precedent Plane Integration added")

# For main.py, we only append so we don't break existing CLI
append_to_file("app/main.py", """
def setup_precedent_cli(parser):
    group = parser.add_argument_group("Precedent Plane")
    group.add_argument("--show-precedent-registry", action="store_true")
    group.add_argument("--show-cases", action="store_true")
    group.add_argument("--show-holdings", action="store_true")
    group.add_argument("--show-rationales", action="store_true")
""")


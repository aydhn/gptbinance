import os

files_to_fix = [
    "app/evidence_graph/artefacts.py",
    "app/identity/capabilities.py",
    "app/observability/alerts.py",
    "app/observability/runbooks.py",
    "app/observability_plane/events.py",
    "app/readiness_board/domains.py",
    "app/reliability/domains.py",
    "app/reviews/requests.py",
]

for file in files_to_fix:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()

        if "from enum import Enum" not in content and "Enum" in content:
            content = "from enum import Enum\n" + content
            with open(file, 'w') as f:
                f.write(content)

print("Integrations fixed.")

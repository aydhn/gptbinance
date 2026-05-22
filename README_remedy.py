import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file("app/remedy_plane/README.md", """
# Remedy Plane

The Remedy Plane provides a canonical typed registry and cure/mitigation/containment/restitution/compensation governance layer.
It ensures that taking technical action to fix an issue does not get conflated with the actual restoration or compensation of the harm suffered.

Fix != Remedy.

We strictly distinguish:
- Harms, Breach Harms, Impacts
- Triggers
- Cures, Mitigations, Containments, Rollbacks, Restorations, Restitutions, Compensations
- Sufficiency, Proportionality, Timeliness, Exhaustion
- Residual Harms, Recourse
- Trust and Quality Verdicts (No rollback theater, no compensation laundering, no hidden residual harms).
""")

with open('app/observability/runbooks.py', 'r') as f:
    content = f.read()

if "add_crossbook_runbook_refs" not in content:
    content = content.replace("_RUNBOOK_REGISTRY", """    # Added in Phase 40
def add_crossbook_runbook_refs(self):
    pass

_RUNBOOK_REGISTRY""", 1)

with open('app/observability/runbooks.py', 'w') as f:
    f.write(content)

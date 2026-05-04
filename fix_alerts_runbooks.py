with open("app/observability/alerts.py", "r") as f:
    content = f.read()
if "class AlertRule" not in content:
    content = content.replace("class CapitalAlertRule(AlertRule):", "class CapitalAlertRule:\n    def __init__(self):\n        pass\n\n    def evaluate(self, metrics: dict) -> bool:")
with open("app/observability/alerts.py", "w") as f:
    f.write(content)

with open("app/observability/runbooks.py", "r") as f:
    content = f.read()
if "RunbookRef" not in content[:300]:
    content = "from pydantic import BaseModel\nclass RunbookRef(BaseModel):\n    runbook_id: str\n    title: str\n    url: str\n\n" + content
with open("app/observability/runbooks.py", "w") as f:
    f.write(content)

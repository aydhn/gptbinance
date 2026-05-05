with open("app/observability/alerts.py", "r") as f:
    content = f.read()

if "add_crossbook_alerts" not in content:
    content = content.replace(
        "class CapitalAlertRule",
        """    # Added in Phase 40
def add_crossbook_alerts(self):
    pass

class CapitalAlertRule""",
    )

with open("app/observability/alerts.py", "w") as f:
    f.write(content)

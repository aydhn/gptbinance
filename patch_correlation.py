import re

with open('app/observability/correlation.py', 'r') as f:
    content = f.read()

# Fix sorting key: Severity enum values might be string, so define a numeric weight mapping.
patch = """            if len(alerts) > 1:
                # Correlate alerts on the same component
                # Define a weight for severity:
                severity_weight = {
                    "info": 0,
                    "warning": 1,
                    "error": 2,
                    "critical": 3
                }
                primary = max(alerts, key=lambda a: (severity_weight.get(a.severity.value, 0), a.occurrence_count))
                related = [a.alert_id for a in alerts if a.alert_id != primary.alert_id]"""

content = re.sub(
    r"            if len\(alerts\) > 1:\n                # Correlate alerts on the same component\n                primary = max\(alerts, key=lambda a: \(a.severity.value, a.occurrence_count\)\)\n                related = \[a.alert_id for a in alerts if a.alert_id != primary.alert_id\]",
    patch,
    content
)

with open('app/observability/correlation.py', 'w') as f:
    f.write(content)

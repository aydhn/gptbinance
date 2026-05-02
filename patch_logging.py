import re

with open('app/core/logging.py', 'r') as f:
    content = f.read()

patch = """
from app.observability.telemetry import ingester
from app.observability.enums import ComponentType, AlertSeverity

def emit_telemetry(event_type: str, component: ComponentType, details: dict = None, severity: AlertSeverity = AlertSeverity.INFO):
    ctx = get_active_context()
    run_id = ctx.run_id if ctx else None
    ingester.capture_event(event_type, component, details, severity, run_id)

class StructuredJSONFormatter(logging.Formatter):
"""

content = content.replace("class StructuredJSONFormatter(logging.Formatter):", patch)

with open('app/core/logging.py', 'w') as f:
    f.write(content)

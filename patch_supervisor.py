import re

with open('app/ops/supervisor.py', 'r') as f:
    content = f.read()

patch_imports = """from app.ops.repository import OpsRepository
from app.observability.telemetry import ingester
from app.observability.enums import ComponentType, AlertSeverity"""

content = content.replace("from app.ops.repository import OpsRepository", patch_imports)

patch_audit = """    def _audit(self, run_id: str, action: str) -> None:
        record = OpsAuditRecord(run_id=run_id, action=action, details="")
        self.repository.append_audit_record(record)
        ingester.capture_event(
            event_type=f"supervisor_{action}",
            component=ComponentType.SUPERVISOR,
            details={"run_id": run_id, "action": action},
            severity=AlertSeverity.INFO,
            run_id=run_id
        )"""

content = content.replace("""    def _audit(self, run_id: str, action: str) -> None:
        record = OpsAuditRecord(run_id=run_id, action=action, details="")
        self.repository.append_audit_record(record)""", patch_audit)

with open('app/ops/supervisor.py', 'w') as f:
    f.write(content)

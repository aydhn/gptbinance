import re

with open('app/execution/live/health.py', 'r') as f:
    content = f.read()

patch_imports = """from datetime import datetime
from typing import Dict, Any
from app.observability.metrics import registry as metric_registry
from app.observability.enums import ComponentType"""

content = content.replace("from datetime import datetime\nfrom typing import Dict, Any", patch_imports)

patch_reject = """    def record_reject(self):
        self.reject_count += 1
        metric_registry.record("live_execution_rejects", 1.0, tags={"type": "reject"})"""

content = content.replace("    def record_reject(self):\n        self.reject_count += 1", patch_reject)

patch_drift = """    def record_drift(self):
        self.drift_count += 1
        metric_registry.record("live_execution_drift", 1.0, tags={"type": "drift"})"""

content = content.replace("    def record_drift(self):\n        self.drift_count += 1", patch_drift)

with open('app/execution/live/health.py', 'w') as f:
    f.write(content)

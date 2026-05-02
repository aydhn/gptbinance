import re

with open('app/execution/live/health.py', 'r') as f:
    content = f.read()

patch = """    def record_reject(self):
        self.reject_count += 1
        try:
            metric_registry.record("live_execution_rejects", 1.0, tags={"type": "reject"})
        except Exception:
            pass"""

content = content.replace("""    def record_reject(self):
        self.reject_count += 1
        metric_registry.record("live_execution_rejects", 1.0, tags={"type": "reject"})""", patch)

patch2 = """    def record_drift(self):
        self.drift_count += 1
        try:
            metric_registry.record("live_execution_drift", 1.0, tags={"type": "drift"})
        except Exception:
            pass"""

content = content.replace("""    def record_drift(self):
        self.drift_count += 1
        metric_registry.record("live_execution_drift", 1.0, tags={"type": "drift"})""", patch2)


with open('app/execution/live/health.py', 'w') as f:
    f.write(content)

with open('app/execution/paper/health.py', 'r') as f:
    content = f.read()

patch3 = """    def record_error(self, err: str):
        self.error_count += 1
        self.last_error = err
        try:
            metric_registry.record("paper_execution_error", 1.0, tags={"error": err[:20]})
        except Exception:
            pass"""

content = content.replace("""    def record_error(self, err: str):
        self.error_count += 1
        self.last_error = err
        metric_registry.record("paper_execution_error", 1.0, tags={"error": err[:20]})""", patch3)

with open('app/execution/paper/health.py', 'w') as f:
    f.write(content)

import re

with open('app/execution/paper/health.py', 'r') as f:
    content = f.read()

patch_imports = """from .models import SessionHealth, SessionHealthSnapshot
from app.observability.metrics import registry as metric_registry
from app.observability.enums import ComponentType"""

content = content.replace("from .models import SessionHealth, SessionHealthSnapshot", patch_imports)

patch_error = """    def record_error(self, err: str):
        self.error_count += 1
        self.last_error = err
        metric_registry.record("paper_execution_error", 1.0, tags={"error": err[:20]})"""

content = content.replace("""    def record_error(self, err: str):
        self.error_count += 1
        self.last_error = err""", patch_error)

with open('app/execution/paper/health.py', 'w') as f:
    f.write(content)

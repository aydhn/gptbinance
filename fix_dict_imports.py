import os

files_to_fix = [
    "app/activation/history.py",
    "app/market_truth/truthfulness.py",
    "app/migrations/debt.py",
    "app/order_lifecycle/reconciliation.py",
    "app/postmortems/tracking.py",
    "app/remediation/debt.py",
    "app/shadow_state/convergence.py",
    "app/shadow_state/storage.py",
    "app/policy_kernel/drift.py",
    "app/decision_quality/reporting.py",
    "app/capital/posture.py",
    "app/crossbook/overlay.py",
]

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r") as f:
        content = f.read()

    if "from typing import" not in content and "Dict" in content:
        content = "from typing import Dict, Any\n" + content
    elif "from typing import" in content and "Dict" not in content:
        content = content.replace("from typing import", "from typing import Dict, Any,")

    with open(filepath, "w") as f:
        f.write(content)

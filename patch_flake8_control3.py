import os

replacements = {
    "app/control_plane/apply.py": {
        "from datetime import datetime, timezone\n": ""
    },
    "app/control_plane/approvals.py": {
        "from app.control_plane.models import ActionRequest, ApprovalDecision, ActionApprovalChain": "from app.control_plane.models import ApprovalDecision, ActionApprovalChain"
    },
    "app/control_plane/models.py": {
        "    PreviewClass,\n    ApprovalClass,\n    ExceptionClass,": "    PreviewClass,\n    ExceptionClass,"
    }
}

for filepath, reps in replacements.items():
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()

        for old, new in reps.items():
            content = content.replace(old, new)

        with open(filepath, "w") as f:
            f.write(content)

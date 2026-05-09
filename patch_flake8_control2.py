import re
import os

files_to_clean = {
    "app/control_plane/apply.py": [
        "from datetime import datetime, timezone\n",
        "from typing import Dict, List\n"
    ],
    "app/control_plane/approvals.py": [
        "from typing import List, Dict, Optional\n",
        "from app.control_plane.models import ActionRequest, ApprovalDecision, ActionApprovalChain\n",
        "from app.control_plane.exceptions import ApprovalViolationError\n",
        "from app.control_plane.enums import ApprovalClass\n"
    ],
    "app/control_plane/models.py": [
        "ApprovalClass,"
    ],
    "app/control_plane/revoke.py": [
        "import uuid\n"
    ],
    "app/control_plane/rollback.py": [
        "from app.control_plane.exceptions import RollbackViolationError\n"
    ],
    "app/control_plane/unfreezes.py": [
        "import uuid\n",
        "from typing import Dict, List\n"
    ]
}

replacements = {
    "app/control_plane/apply.py": {
        "from typing import Dict, List": "from typing import Dict"
    },
    "app/control_plane/approvals.py": {
        "from typing import List, Dict, Optional": "from typing import List, Dict",
        "from app.control_plane.models import ActionRequest, ApprovalDecision, ActionApprovalChain": "from app.control_plane.models import ApprovalDecision, ActionApprovalChain",
        "from app.control_plane.exceptions import ApprovalViolationError\n": "",
        "from app.control_plane.enums import ApprovalClass\n": ""
    },
    "app/control_plane/models.py": {
        "ApprovalClass, ": ""
    },
    "app/control_plane/revoke.py": {
        "import uuid\n": ""
    },
    "app/control_plane/rollback.py": {
        "from app.control_plane.exceptions import RollbackViolationError\n": ""
    },
    "app/control_plane/unfreezes.py": {
        "import uuid\n": "",
        "from typing import Dict, List\n": "from typing import Dict\n"
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

import os

filepath = "app/policy_kernel/drift.py"
if os.path.exists(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    if "from typing import" not in content and "Dict" in content:
        content = "from typing import Dict, Any\n" + content
    elif "from typing import" in content and "Dict" not in content:
        content = content.replace("from typing import", "from typing import Dict, Any,")
    with open(filepath, "w") as f:
        f.write(content)

import os
import glob

all_python_files = glob.glob("app/**/*.py", recursive=True) + glob.glob(
    "tests/**/*.py", recursive=True
)

for filepath in all_python_files:
    with open(filepath, "r") as f:
        content = f.read()

    needs_fix = False

    if "from typing import" not in content and "Dict" in content:
        content = "from typing import Dict, Any, List, Optional\n" + content
        needs_fix = True

    if needs_fix:
        with open(filepath, "w") as f:
            f.write(content)

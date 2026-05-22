import os

files_to_fix = ["app/jurisdiction_plane/models.py"]

for file in files_to_fix:
    with open(file, "r") as f:
        content = f.read()

    content = content.replace("from typing import List, Dict, Optional, Any", "from typing import Dict, Any")

    with open(file, "w") as f:
        f.write(content)

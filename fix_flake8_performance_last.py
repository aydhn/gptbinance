with open("app/performance_plane/baselines.py", "r") as f:
    lines = f.readlines()
with open("app/performance_plane/baselines.py", "w") as f:
    for line in lines:
        if "from app.performance_plane.enums import BaselineClass" in line:
            line = "from app.performance_plane.enums import BaselineClass\n"
        f.write(line)

with open("app/performance_plane/windows.py", "r") as f:
    lines = f.readlines()
with open("app/performance_plane/windows.py", "w") as f:
    for line in lines:
        if "from typing import Dict, Any, Optional" in line:
            line = "from typing import Dict, Any, Optional\n"
        f.write(line)

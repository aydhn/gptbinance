import os

def fix_file(path, replacements):
    with open(path, 'r') as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(path, 'w') as f:
        f.write(content)

fix_file("app/performance_plane/base.py", [
    ("from typing import Dict, Any, List", "from typing import Optional")
])

fix_file("app/performance_plane/baselines.py", [
    ("from typing import Dict, Any, List, Optional", "from typing import Dict, Any, Optional"),
    ("from app.performance_plane.enums import BaselineClass, BenchmarkClass", "from app.performance_plane.enums import BaselineClass")
])

fix_file("app/performance_plane/equivalence.py", [
    ("from typing import Dict, Any, List, Optional", "from typing import Dict, Any, Optional")
])

fix_file("app/performance_plane/risk_adjusted.py", [
    ("from typing import Dict, Any, List, Optional", "from typing import Dict, Any, Optional")
])

fix_file("app/performance_plane/windows.py", [
    ("from datetime import datetime, timedelta, timezone", "from datetime import datetime, timedelta"),
    ("from typing import Dict, Any, List, Optional", "from typing import Dict, Any, Optional")
])

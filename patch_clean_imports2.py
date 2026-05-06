import re

with open("app/evidence_graph/models.py", "r") as f:
    content = f.read()

# Add them back once at the top
content = "from typing import List, Dict, Optional, Any\n" + content

with open("app/evidence_graph/models.py", "w") as f:
    f.write(content)

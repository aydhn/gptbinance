with open("app/evidence_graph/models.py", "r") as f:
    content = f.read()

# remove unused imports
content = content.replace(
    "from typing import List, Dict, Optional, Any\n",
    "from typing import List, Dict, Optional, Any\n",
)
content = content.replace(
    "from app.evidence_graph.enums import (\n",
    "from app.evidence_graph.enums import (\n",
)

with open("app/evidence_graph/models.py", "w") as f:
    f.write(content)

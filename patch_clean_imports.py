import re

with open("app/evidence_graph/models.py", "r") as f:
    content = f.read()

# remove redefinitions
content = content.replace("from typing import List, Dict, Optional, Any\n", "")
content = content.replace("from datetime import datetime\n", "", 1)
content = content.replace("EvidenceGraphVerdict,\n", "")
content = content.replace("    EvidenceGraphVerdict,\n", "")
content = content.replace("EvidenceGraphVerdict", "")

with open("app/evidence_graph/models.py", "w") as f:
    f.write(content)

with open("app/evidence_graph/artefacts.py", "r") as f:
    content = f.read()

content = content.replace("from typing import Dict, Any, List, Optional", "from typing import Dict, List, Optional")
content = content.replace("from app.evidence_graph.enums import ArtefactType, ScopeClass", "from app.evidence_graph.enums import ArtefactType")

with open("app/evidence_graph/artefacts.py", "w") as f:
    f.write(content)

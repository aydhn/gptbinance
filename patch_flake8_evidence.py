import re
import os
import glob

files = glob.glob("app/evidence_graph/*.py")

for file in files:
    with open(file, "r") as f:
        content = f.read()

    # Generic cleanups
    content = content.replace(" \n", "\n")
    content = re.sub(r'\n\n\n+', '\n\n', content)

    # Specific unused imports
    if "base.py" in file:
        content = content.replace("from typing import List, Optional, Dict, Any\n", "from typing import Dict, Any\n")
        content = content.replace("    EvidenceCaseFile,\n    EvidencePack\n", "    EvidenceCaseFile\n")

    if "cases.py" in file:
        content = content.replace("from typing import List, Dict, Any\n", "")

    if "packs.py" in file:
        content = content.replace("from typing import List\n", "")
        content = content.replace("from app.evidence_graph.models import EvidencePack, ArtefactRecord, RelationEdge\n", "from app.evidence_graph.models import EvidencePack\n")

    if "queries.py" in file:
        content = content.replace("from typing import List\n", "")
        content = content.replace("from app.evidence_graph.models import QueryRequest, QueryResult, ArtefactRecord, RelationEdge\n", "from app.evidence_graph.models import QueryRequest, QueryResult\n")

    if "reporting.py" in file:
        content = content.replace("from typing import List, Dict\n", "from typing import List\n")
        content = content.replace("from app.evidence_graph.models import ArtefactRecord, RelationEdge, EvidenceCaseFile, EvidencePack, GraphGapFinding, RedactionRecord\n", "from app.evidence_graph.models import ArtefactRecord, RelationEdge, EvidenceCaseFile, GraphGapFinding, RedactionRecord\n")

    if "relations.py" in file:
        content = content.replace("from typing import Dict, List, Optional\n", "from typing import Dict, List\n")
        content = content.replace("from app.evidence_graph.exceptions import InvalidRelationEdgeError\n", "")

    if "history.py" in file:
        content = content.replace("from app.evidence_graph.models import ArtefactRecord, RelationEdge\n", "")

    if "ingest.py" in file:
        content = content.replace("from typing import Dict, Any, List, Optional\n", "from typing import Dict, Any, List\n")
        content = content.replace("from app.evidence_graph.models import ArtefactRecord, ArtefactScope, ArtefactDescriptor\n", "from app.evidence_graph.models import ArtefactRecord, ArtefactDescriptor\n")

    if "repository.py" in file:
        content = content.replace("from app.evidence_graph.scopes import ScopeEnforcer\n", "")

    if "storage.py" in file:
        content = content.replace("from typing import Dict, List, Any\nfrom datetime import datetime\n", "")

    if "models.py" in file:
        content = content.replace("from app.evidence_graph.enums import EvidenceGraphVerdict\n", "")
        # The redefinition error was due to the monkey patch replacing imports.
        # We did:
        # from dataclasses import dataclass, field
        # from typing import List, Dict, Optional, Any
        # from datetime import datetime
        # Let's clean up duplicate imports.
        # It's easier to just let black handle it if we install isort, but we can do it manually.

    with open(file, "w") as f:
        f.write(content)

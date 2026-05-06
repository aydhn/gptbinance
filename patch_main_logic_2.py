with open("app/main.py", "r") as f:
    content = f.read()

imports = """
from app.evidence_graph.models import EvidenceGraphConfig, ArtefactScope
from app.evidence_graph.enums import CaseFileClass, ScopeClass, QueryClass
from app.evidence_graph.repository import EvidenceGraphRepository
from app.evidence_graph.reporting import GraphReporter
"""

if "EvidenceGraphRepository" not in content[:1000]:
    content = content.replace("from typing import", imports + "\nfrom typing import")

with open("app/main.py", "w") as f:
    f.write(content)

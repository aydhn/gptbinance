with open("app/evidence_graph/models.py", "r") as f:
    content = f.read()
content = content.replace(
    "from pydantic import BaseModel, Field",
    "from dataclasses import dataclass, field\nfrom typing import List, Dict, Optional, Any\nfrom datetime import datetime",
)

content = content.replace(
    "class EvidenceGraphConfig(BaseModel):", "@dataclass\nclass EvidenceGraphConfig:"
)
content = content.replace(
    "class ArtefactScope(BaseModel):", "@dataclass\nclass ArtefactScope:"
)
content = content.replace(
    "class ArtefactDescriptor(BaseModel):", "@dataclass\nclass ArtefactDescriptor:"
)
content = content.replace(
    "class ArtefactRef(BaseModel):", "@dataclass\nclass ArtefactRef:"
)
content = content.replace(
    "class ArtefactLineage(BaseModel):", "@dataclass\nclass ArtefactLineage:"
)
content = content.replace(
    "class ArtefactRecord(BaseModel):", "@dataclass\nclass ArtefactRecord:"
)
content = content.replace(
    "class RelationEdge(BaseModel):", "@dataclass\nclass RelationEdge:"
)
content = content.replace(
    "class RelationPath(BaseModel):", "@dataclass\nclass RelationPath:"
)
content = content.replace(
    "class EvidenceCaseSection(BaseModel):", "@dataclass\nclass EvidenceCaseSection:"
)
content = content.replace(
    "class RedactionRecord(BaseModel):", "@dataclass\nclass RedactionRecord:"
)
content = content.replace(
    "class EvidenceCaseFile(BaseModel):", "@dataclass\nclass EvidenceCaseFile:"
)
content = content.replace(
    "class EvidencePack(BaseModel):", "@dataclass\nclass EvidencePack:"
)
content = content.replace(
    "class QueryRequest(BaseModel):", "@dataclass\nclass QueryRequest:"
)
content = content.replace(
    "class QueryResult(BaseModel):", "@dataclass\nclass QueryResult:"
)
content = content.replace(
    "class LineageTraversal(BaseModel):", "@dataclass\nclass LineageTraversal:"
)
content = content.replace(
    "class DependencyTraversal(BaseModel):", "@dataclass\nclass DependencyTraversal:"
)
content = content.replace(
    "class GraphGapFinding(BaseModel):", "@dataclass\nclass GraphGapFinding:"
)
content = content.replace(
    "class EvidenceGraphAuditRecord(BaseModel):",
    "@dataclass\nclass EvidenceGraphAuditRecord:",
)
content = content.replace(
    "class EvidenceGraphArtifactManifest(BaseModel):",
    "@dataclass\nclass EvidenceGraphArtifactManifest:",
)

content = content.replace("Field(default_factory=list)", "field(default_factory=list)")
content = content.replace("Field(default_factory=dict)", "field(default_factory=dict)")

with open("app/evidence_graph/models.py", "w") as f:
    f.write(content)

with open("app/evidence_graph/artefacts.py", "r") as f:
    content = f.read()
content = content.replace("descriptor.dict()", "descriptor.__dict__")
with open("app/evidence_graph/artefacts.py", "w") as f:
    f.write(content)

with open("app/evidence_graph/storage.py", "r") as f:
    content = f.read()
content = content.replace(
    "artefact.json()", "json.dumps(artefact.__dict__, default=str)"
)
content = content.replace(
    "relation.json()", "json.dumps(relation.__dict__, default=str)"
)
with open("app/evidence_graph/storage.py", "w") as f:
    f.write(content)

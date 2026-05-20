from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ProvenanceObjectRefs(BaseModel):
    provenance_id: str
    ref_type: str

class BaseProvenanceObject(BaseModel):
    provenance_id: str
    class_type: str
    owner: str
    scope: str
    source_authority: str
    custody_posture: str
    lineage_refs: List[ProvenanceObjectRefs] = []

from pydantic import BaseModel
from typing import Dict, Any

class OperatingModelBaseReport(BaseModel):
    report_id: str
    timestamp: str
    metadata: Dict[str, Any]

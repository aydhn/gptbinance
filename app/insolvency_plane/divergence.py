# divergence.py
from typing import Dict, List, Optional
from pydantic import BaseModel
from app.insolvency_plane.models import InsolvencyObjectRef

class InsolvencyDivergenceReport(BaseModel):
    report_id: str
    insolvency_ref: InsolvencyObjectRef
    divergence_type: str # estate, claim, plan, priority, residual_deficit
    description: str
    severity: str
    blast_radius: str

class InsolvencyDivergenceManager:
    def __init__(self):
        self.reports: Dict[str, InsolvencyDivergenceReport] = {}

    def register_report(self, report: InsolvencyDivergenceReport):
        self.reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[InsolvencyDivergenceReport]:
        return self.reports.get(report_id)

    def list_reports(self) -> List[InsolvencyDivergenceReport]:
        return list(self.reports.values())

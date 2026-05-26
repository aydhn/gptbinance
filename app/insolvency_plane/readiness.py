# readiness.py
from typing import Dict, List, Optional
from pydantic import BaseModel
from app.insolvency_plane.models import InsolvencyObjectRef

class InsolvencyReadinessReport(BaseModel):
    report_id: str
    insolvency_ref: InsolvencyObjectRef
    estate_clarity: str
    claim_rigor: str
    priority_discipline: str
    plan_integrity: str
    residual_deficit_visibility: str
    readiness_class: str
    proof_notes: List[str]

class InsolvencyReadinessManager:
    def __init__(self):
        self.reports: Dict[str, InsolvencyReadinessReport] = {}

    def register_report(self, report: InsolvencyReadinessReport):
        self.reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[InsolvencyReadinessReport]:
        return self.reports.get(report_id)

    def list_reports(self) -> List[InsolvencyReadinessReport]:
        return list(self.reports.values())

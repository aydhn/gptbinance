# quality.py
from typing import Dict, List, Optional
from pydantic import BaseModel
from app.insolvency_plane.models import InsolvencyObjectRef

class InsolvencyQualityReport(BaseModel):
    report_id: str
    insolvency_ref: InsolvencyObjectRef
    estate_leakage_warning: bool
    false_secured_warning: bool
    hidden_deficit_warning: bool
    plan_theater_warning: bool
    stay_bypass_warning: bool
    priority_inversion_warning: bool
    quality_verdict: str

class InsolvencyQualityManager:
    def __init__(self):
        self.reports: Dict[str, InsolvencyQualityReport] = {}

    def register_report(self, report: InsolvencyQualityReport):
        self.reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[InsolvencyQualityReport]:
        return self.reports.get(report_id)

    def list_reports(self) -> List[InsolvencyQualityReport]:
        return list(self.reports.values())

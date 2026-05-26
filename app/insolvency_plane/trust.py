# trust.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyTrustVerdict, InsolvencyObjectRef
from pydantic import BaseModel

class TrustReport(BaseModel):
    report_id: str
    insolvency_ref: InsolvencyObjectRef
    verdict: InsolvencyTrustVerdict

class InsolvencyTrustManager:
    def __init__(self):
        self.reports: Dict[str, TrustReport] = {}

    def register_report(self, report: TrustReport):
        self.reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[TrustReport]:
        return self.reports.get(report_id)

    def list_reports(self) -> List[TrustReport]:
        return list(self.reports.values())

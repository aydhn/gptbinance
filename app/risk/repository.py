from typing import List
from app.risk.storage import RiskStorage
from app.risk.models import RiskApprovalBundle, RiskAuditRecord
from app.risk.explain import RiskExplainer


class RiskRepository:
    def __init__(self, storage: RiskStorage):
        self.storage = storage
        self.explainer = RiskExplainer()

    def store_decision(self, run_id: str, bundle: RiskApprovalBundle):
        intent = (
            bundle.decision.approved_intent or bundle.decision.sizing
        )  # rough approx if rejected
        symbol = intent.symbol if intent else "UNKNOWN"
        side = intent.side.name if intent else "UNKNOWN"
        req_sz = (
            bundle.decision.sizing.requested_size if bundle.decision.sizing else 0.0
        )
        app_sz = bundle.decision.sizing.approved_size if bundle.decision.sizing else 0.0

        record = RiskAuditRecord(
            timestamp=bundle.timestamp,
            run_id=run_id,
            symbol=symbol,
            intent_source="StrategyEngine",
            side=side,
            verdict=bundle.decision.verdict.name,
            requested_size=req_sz,
            approved_size=app_sz,
            rationale=self.explainer.explain(bundle.decision),
            rejection_reasons=[
                {
                    "source": r.source,
                    "severity": r.severity.name,
                    "rationale": r.rationale,
                }
                for r in bundle.decision.rejection_reasons
            ],
        )
        self.storage.save_audit(record)

    def get_audit_trail(self, run_id: str) -> List[RiskAuditRecord]:
        return self.storage.get_by_run(run_id)

    # Phase 22 Analytics hook
    def get_analytics_refs(self, run_id: str) -> dict:
        return {"audit_trail": self.get_audit_trail(run_id)}

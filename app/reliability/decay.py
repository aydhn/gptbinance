import uuid
from typing import List, Dict, Any
from app.reliability.enums import ReliabilityDomain, ReadinessDecayClass
from app.reliability.models import ReadinessDecayRecord


class ReadinessDecayEngine:
    @staticmethod
    def evaluate_stale_evidence(
        domain: ReliabilityDomain, evidence_age_hours: float, max_allowed_age: float
    ) -> List[ReadinessDecayRecord]:
        records = []
        if evidence_age_hours > max_allowed_age:
            severity = min(
                1.0, (evidence_age_hours - max_allowed_age) / max_allowed_age
            )
            records.append(
                ReadinessDecayRecord(
                    record_id=f"decay_{uuid.uuid4().hex[:8]}",
                    domain=domain,
                    decay_class=ReadinessDecayClass.STALE_EVIDENCE,
                    severity_score=severity,
                    evidence_ref="evidence_age_check",
                    description=f"Evidence is {evidence_age_hours:.1f}h old (max allowed: {max_allowed_age:.1f}h).",
                )
            )
        return records

    @staticmethod
    def evaluate_unresolved_debt(
        domain: ReliabilityDomain, critical_debt_count: int, oldest_debt_days: float
    ) -> List[ReadinessDecayRecord]:
        records = []
        if critical_debt_count > 0:
            severity = min(1.0, (critical_debt_count * 0.1) + (oldest_debt_days * 0.05))
            records.append(
                ReadinessDecayRecord(
                    record_id=f"decay_{uuid.uuid4().hex[:8]}",
                    domain=domain,
                    decay_class=ReadinessDecayClass.UNRESOLVED_DEBT,
                    severity_score=severity,
                    evidence_ref="debt_tracker",
                    description=f"Unresolved critical debt count: {critical_debt_count}. Oldest: {oldest_debt_days:.1f} days.",
                )
            )
        return records

    @staticmethod
    def evaluate_recurring_incidents(
        domain: ReliabilityDomain, incident_cluster_count: int
    ) -> List[ReadinessDecayRecord]:
        records = []
        if incident_cluster_count > 0:
            severity = min(1.0, incident_cluster_count * 0.2)
            records.append(
                ReadinessDecayRecord(
                    record_id=f"decay_{uuid.uuid4().hex[:8]}",
                    domain=domain,
                    decay_class=ReadinessDecayClass.RECURRING_INCIDENT,
                    severity_score=severity,
                    evidence_ref="incident_history",
                    description=f"Detected {incident_cluster_count} recurring incident clusters.",
                )
            )
        return records

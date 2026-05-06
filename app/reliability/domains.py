from typing import Dict, List
from app.reliability.enums import ReliabilityDomain
from app.reliability.models import ReliabilityDomainModel
from app.reliability.exceptions import ReliabilityTowerError


class ReliabilityDomainRegistry:
    def __init__(self):
        self._domains: Dict[str, ReliabilityDomainModel] = {}
        self._initialize_predefined_domains()

    def _initialize_predefined_domains(self):
        predefined = [
            ReliabilityDomainModel(
                name=ReliabilityDomain.MARKET_TRUTH,
                owner="Market Data Team",
                rationale="Ensures market data freshness and sequence integrity.",
                evidence_requirements=["freshness_metrics", "sequence_gaps"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.SHADOW_TRUTHFULNESS,
                owner="Ledger Team",
                rationale="Ensures shadow state closely tracks the venue state without unacceptable drift.",
                evidence_requirements=["drift_age", "unresolved_drift_count"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.LIFECYCLE_HEALTH,
                owner="Execution Team",
                rationale="Ensures order lifecycle avoids orphans and timeout-unknown states.",
                evidence_requirements=["orphan_density", "timeout_unknown_count"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.INCIDENT_OPERATIONS,
                owner="Incident Response Team",
                rationale="Ensures incidents are resolved quickly and do not frequently recur.",
                evidence_requirements=["mttd", "mttr", "recurring_incident_rate"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.REMEDIATION_CLOSURE,
                owner="Security & Compliance Team",
                rationale="Ensures CAPA items are closed promptly and remediation debt is managed.",
                evidence_requirements=[
                    "overdue_critical_capa_ratio",
                    "remediation_debt_age",
                ],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.MIGRATION_STABILITY,
                owner="Platform Engineering",
                rationale="Ensures migrations are verified and do not introduce instability.",
                evidence_requirements=[
                    "failed_verification_burden",
                    "pending_critical_migrations",
                ],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.POLICY_INTEGRITY,
                owner="Governance Team",
                rationale="Ensures policy evaluations do not drift from actual enforcement.",
                evidence_requirements=[
                    "drift_cleanliness",
                    "hard_block_bypass_attempts",
                ],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.ACTIVATION_PROBATION,
                owner="Release Management",
                rationale="Ensures new features pass probation without excessive failures.",
                evidence_requirements=["probation_fail_density", "repeated_halts"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.CAPITAL_OPERABILITY,
                owner="Treasury",
                rationale="Ensures capital is safely deployed without excessive freezes or reduced posture.",
                evidence_requirements=["freeze_density", "capital_instability"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.CROSS_BOOK_STABILITY,
                owner="Risk Management",
                rationale="Ensures cross-book exposure does not lead to repeated conflicts.",
                evidence_requirements=["repeated_critical_conflict_density"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.DECISION_QUALITY_HEALTH,
                owner="Data Science Team",
                rationale="Ensures decision funnels do not suffer from severe degradation.",
                evidence_requirements=["severe_funnel_degradation_cluster_rate"],
            ),
            ReliabilityDomainModel(
                name=ReliabilityDomain.RELEASE_READINESS_HEALTH,
                owner="Readiness Board",
                rationale="Ensures board decisions are based on fresh and clean evidence.",
                evidence_requirements=[
                    "board_evidence_freshness",
                    "recurring_board_holds",
                ],
            ),
        ]
        for d in predefined:
            self.register(d)

    def register(self, domain: ReliabilityDomainModel):
        if domain.name.value in self._domains:
            raise ReliabilityTowerError(
                f"Domain {domain.name.value} already registered."
            )
        self._domains[domain.name.value] = domain

    def get(self, name: str) -> ReliabilityDomainModel:
        if name not in self._domains:
            raise ReliabilityTowerError(f"Domain {name} not found.")
        return self._domains[name]

    def list_all(self) -> List[ReliabilityDomainModel]:
        return list(self._domains.values())


domain_registry = ReliabilityDomainRegistry()

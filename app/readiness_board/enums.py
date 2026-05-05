from enum import Enum


class CandidateClass(Enum):
    EXPERIMENT_PROMOTION = "experiment_promotion"
    PAPER_SHADOW = "paper_shadow"
    CANDIDATE_QUALIFICATION = "candidate_qualification"
    CANARY_LIVE_CAUTION = "canary_live_caution"
    MIGRATION_AFFECTED = "migration_affected"
    REMEDIATION_RECOVERY = "remediation_recovery"


class EvidenceClass(Enum):
    QUALIFICATION_STATUS = "qualification_status"
    POLICY_DECISION_PROOFS = "policy_decision_proofs"
    MARKET_TRUTH_EVIDENCE = "market_truth_evidence"
    SHADOW_TRUTHFULNESS = "shadow_truthfulness"
    REMEDIATION_DEBT_SUMMARY = "remediation_debt_summary"
    MIGRATION_DEBT_STATUS = "migration_debt_status"
    STRESS_EVIDENCE = "stress_evidence"
    CAPITAL_POSTURE = "capital_posture"
    CROSS_BOOK_POSTURE = "cross_book_posture"
    ORDER_LIFECYCLE_HEALTH = "order_lifecycle_health"
    DECISION_QUALITY_SUMMARIES = "decision_quality_summaries"
    EXPERIMENT_EVIDENCE_BUNDLES = "experiment_evidence_bundles"
    KNOWLEDGE_RUNBOOK_COVERAGE = "knowledge_runbook_coverage"


class AdmissibilityVerdict(Enum):
    ADMISSIBLE = "admissible"
    CAUTION = "caution"
    INADMISSIBLE = "inadmissible"


class ReadinessDomain(Enum):
    POLICY = "policy"
    QUALIFICATION = "qualification"
    MARKET_TRUTH = "market_truth"
    SHADOW_TRUTHFULNESS = "shadow_truthfulness"
    LIFECYCLE_HEALTH = "lifecycle_health"
    LEDGER_RECONCILIATION = "ledger_reconciliation"
    CROSS_BOOK = "cross_book"
    CAPITAL = "capital"
    EVENT_RISK = "event_risk"
    STRESS_RISK = "stress_risk"
    MIGRATION = "migration"
    REMEDIATION = "remediation"
    DECISION_QUALITY = "decision_quality"
    KNOWLEDGE_COVERAGE = "knowledge_coverage"


class DomainVerdict(Enum):
    PASS = "pass"
    CAUTION = "caution"
    BLOCK = "block"
    UNKNOWN = "unknown"


class BoardVerdict(Enum):
    GO = "go"
    NO_GO = "no_go"
    CONDITIONAL_GO = "conditional_go"
    HOLD = "hold"
    NEEDS_REVIEW = "needs_review"


class DecisionSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class ContradictionClass(Enum):
    EXPERIMENT_VS_POLICY = "experiment_vs_policy"
    QUALIFICATION_VS_SHADOW = "qualification_vs_shadow"
    CAPITAL_VS_REMEDIATION = "capital_vs_remediation"
    MARKET_TRUTH_VS_LIFECYCLE = "market_truth_vs_lifecycle"
    CONFLICTING_TIMESTAMPS = "conflicting_timestamps"
    OTHER = "other"


class ConditionalScope(Enum):
    LIMITED_SYMBOL_SET = "limited_symbol_set"
    PROFILE_ONLY = "profile_only"
    PAPER_SHADOW_ONLY = "paper_shadow_only"
    CANDIDATE_QUALIFICATION_ONLY = "candidate_qualification_only"
    NO_NEW_EXPOSURE = "no_new_exposure"
    TIME_BOUND = "time_bound"


class PromotionStage(Enum):
    CANDIDATE_REGISTRY = "candidate_registry"
    PAPER_SHADOW = "paper_shadow"
    CANDIDATE_QUALIFICATION = "candidate_qualification"
    CANARY_LIVE_CAUTION = "canary_live_caution"
    LIVE = "live"


class MemoClass(Enum):
    STANDARD = "standard"
    CONDITIONAL = "conditional"
    BLOCKED = "blocked"

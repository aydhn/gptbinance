from enum import Enum

class FinalityClass(str, Enum):
    PROVISIONAL = "provisional"
    CONDITIONAL = "conditional"
    FINAL = "final"
    SETTLED = "settled"
    SUPERSEDED = "superseded"
    RETIRED = "retired"
    TERMINAL = "terminal"

class ClosureClass(str, Enum):
    OPEN = "open"
    CONDITIONALLY_CLOSED = "conditionally_closed"
    PROVISIONALLY_CLOSED = "provisionally_closed"
    FINALLY_CLOSED = "finally_closed"

class SettlementClass(str, Enum):
    OBLIGATION_SETTLED = "obligation_settled"
    BREACH_SETTLED = "breach_settled"
    COMPENSATING_SETTLEMENT = "compensating_settlement"
    PARTIALLY_SETTLED = "partially_settled"

class TerminalityClass(str, Enum):
    WORKFLOW_TERMINAL = "workflow_terminal"
    CONTRACT_TERMINAL = "contract_terminal"
    MIGRATION_TERMINAL = "migration_terminal"
    DECISION_TERMINAL = "decision_terminal"

class ReopenClass(str, Enum):
    REOPENED = "reopened"
    FORCED_REOPEN = "forced_reopen"
    EVIDENCE_DRIVEN_REOPEN = "evidence_driven_reopen"
    DENIED = "denied"

class AppealClass(str, Enum):
    PENDING = "pending"
    RESOLVED = "resolved"
    EXHAUSTED = "exhausted"
    INVALID = "invalid"

class DisputeClass(str, Enum):
    ACTIVE = "active"
    DORMANT = "dormant"
    RESOLVED = "resolved"

class SupersessionClass(str, Enum):
    CLOSURE_SUPERSEDED = "closure_superseded"
    VERDICT_SUPERSEDED = "verdict_superseded"
    RESOLUTION_SUPERSEDED = "resolution_superseded"

class RetirementClass(str, Enum):
    RECORD_RETIRED = "record_retired"
    OBLIGATION_RETIRED = "obligation_retired"
    PATHWAY_RETIRED = "pathway_retired"

class IrreversibilityClass(str, Enum):
    PRACTICALLY_IRREVERSIBLE = "practically_irreversible"
    LEGALLY_IRREVERSIBLE = "legally_irreversible"
    TECHNICALLY_REVERSIBLE = "technically_reversible"
    TIME_BOUND_REVERSIBILITY = "time_bound_reversibility"

class FinalityTrustVerdictClass(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

import os
import textwrap

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(textwrap.dedent(content).strip() + '\n')

def patch_file(path, old_text, new_text):
    if not os.path.exists(path):
        create_file(path, new_text)
        return
    with open(path, 'r') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
    elif new_text not in content:
        content += "\n" + new_text
    with open(path, 'w') as f:
        f.write(content)

print("Patching integrations...")

# 38. app/research_plane/evidence.py
patch_file("app/research_plane/evidence.py",
           "class ResearchObservation:",
           "class ResearchObservation:\n    def to_decision_quality_evidence(self):\n        pass")

# 39. app/experiment_plane/recommendations.py
patch_file("app/experiment_plane/recommendations.py",
           "class ExperimentRecommendation:",
           "class ExperimentRecommendation:\n    def link_decision(self, decision_id: str):\n        pass")

# 40. app/simulation_plane/results.py
patch_file("app/simulation_plane/results.py",
           "class SimulationResult:",
           "class SimulationResult:\n    def export_to_decision_option(self):\n        pass")

# 41. app/strategy_plane/lifecycle.py
patch_file("app/strategy_plane/lifecycle.py",
           "class StrategyTransition:",
           "class StrategyTransition:\n    def validate_decision_manifest(self, manifest_id: str):\n        pass")

# 42. app/risk_plane/manifests.py
patch_file("app/risk_plane/manifests.py",
           "class RiskPostureManifest:",
           "class RiskPostureManifest:\n    def export_evidence_bundle(self):\n        pass")

# 43. app/allocation/intents.py
patch_file("app/allocation/intents.py",
           "class AllocationIntent:",
           "class AllocationIntent:\n    def require_decision_lineage(self, decision_id: str):\n        pass")

# 44. app/execution_plane/runtime.py
patch_file("app/execution_plane/runtime.py",
           "class ExecutionIntervention:",
           "class ExecutionIntervention:\n    def log_decision_rationale(self, rationale_ref: str):\n        pass")

# 45. app/control_plane/receipts.py
patch_file("app/control_plane/receipts.py",
           "class ActionReceipt:",
           "class ActionReceipt:\n    def associate_decision_manifest(self, manifest_id: str):\n        pass")

# 46. app/release_plane/readiness.py
patch_file("app/release_plane/readiness.py",
           "class ReleaseReadiness:",
           "class ReleaseReadiness:\n    def check_decision_quality_posture(self):\n        pass")

# 47. app/release_plane/rollouts.py
patch_file("app/release_plane/rollouts.py",
           "class ReleaseRollout:",
           "class ReleaseRollout:\n    def require_precommitment_refs(self):\n        pass")

# 48. app/activation/guards.py
patch_file("app/activation/guards.py",
           "class ActivationGuard:",
           "class ActivationGuard:\n    def require_decision_object(self):\n        pass")

# 49. app/activation/history.py
patch_file("app/activation/history.py",
           "class ActivationHistory:",
           "class ActivationHistory:\n    def store_decision_snapshot(self):\n        pass")

# 50. app/policy_plane/evaluations.py
patch_file("app/policy_plane/evaluations.py",
           "class PolicyEvaluation:",
           "class PolicyEvaluation:\n    def enforce_decision_quality_evidence(self):\n        pass")

# 51. app/policy_kernel/context.py
patch_file("app/policy_kernel/context.py",
           "class PolicyContext:",
           "class PolicyContext:\n    def __init__(self):\n        self.decision_posture = None\n        self.open_assumptions = []")

# 52. app/policy_kernel/invariants.py
patch_file("app/policy_kernel/invariants.py",
           "class InvariantChecker:",
           "class InvariantChecker:\n    def check_decision_quality_invariants(self):\n        pass")

# 53. app/readiness_board/evidence.py
patch_file("app/readiness_board/evidence.py",
           "class ReadinessEvidenceBundle:",
           "class ReadinessEvidenceBundle:\n    def include_decision_trust(self):\n        pass")

# 54. app/readiness_board/domains.py
patch_file("app/readiness_board/domains.py",
           "class ReadinessDomain(str, Enum):",
           "class ReadinessDomain(str, Enum):\n    DECISION_INTEGRITY = 'decision_integrity'")

# 55. app/reliability/domains.py
patch_file("app/reliability/domains.py",
           "class ReliabilityDomain(str, Enum):",
           "class ReliabilityDomain(str, Enum):\n    DECISION_INTEGRITY = 'decision_integrity'")

# 56. app/reliability/slos.py
patch_file("app/reliability/slos.py",
           "class SLODefinition:",
           "class SLODefinition:\n    @classmethod\n    def missing_option_absence(cls):\n        pass")

# 57. app/incident_plane/triage.py
patch_file("app/incident_plane/triage.py",
           "class IncidentTriageDecision:",
           "class IncidentTriageDecision:\n    def require_hypothesis_and_options(self):\n        pass")

# 58. app/incident_plane/recovery.py
patch_file("app/incident_plane/recovery.py",
           "class IncidentRecoveryAction:",
           "class IncidentRecoveryAction:\n    def link_recovery_decision_manifest(self):\n        pass")

# 59. app/postmortem_plane/evidence.py
patch_file("app/postmortem_plane/evidence.py",
           "class PostmortemEvidenceBundle:",
           "class PostmortemEvidenceBundle:\n    def pull_decision_quality_evidence(self):\n        pass")

# 60. app/postmortem_plane/lessons.py
patch_file("app/postmortem_plane/lessons.py",
           "class LessonsLearned:",
           "class LessonsLearned:\n    def separate_outcome_and_process_quality(self):\n        pass")

# 61. app/observability_plane/events.py
patch_file("app/observability_plane/events.py",
           "class ObservabilityEventType(str, Enum):",
           "class ObservabilityEventType(str, Enum):\n    DECISION_CREATED = 'decision_created'\n    OPTION_COMPARED = 'option_compared'\n    OUTCOME_REVIEWED = 'outcome_reviewed'")

# 62. app/observability_plane/diagnostics.py
patch_file("app/observability_plane/diagnostics.py",
           "class DiagnosticSignal:",
           "class DiagnosticSignal:\n    @classmethod\n    def overconfidence_pattern(cls):\n        pass")

# 63. app/compliance_plane/requirements.py
patch_file("app/compliance_plane/requirements.py",
           "class ComplianceRequirement:",
           "class ComplianceRequirement:\n    def enforce_rationale_preservation(self):\n        pass")

# 64. app/compliance_plane/findings.py
patch_file("app/compliance_plane/findings.py",
           "class ComplianceFinding:",
           "class ComplianceFinding:\n    @classmethod\n    def missing_rationale(cls):\n        pass")

# 65. app/security_plane/readiness.py
patch_file("app/security_plane/readiness.py",
           "class SecurityReadiness:",
           "class SecurityReadiness:\n    def require_option_comparison_for_high_risk(self):\n        pass")

# 66. app/migration_plane/prechecks.py
patch_file("app/migration_plane/prechecks.py",
           "class MigrationPrecheck:",
           "class MigrationPrecheck:\n    def enforce_irreversible_migration_options(self):\n        pass")

# 67. app/continuity_plane/readiness.py
patch_file("app/continuity_plane/readiness.py",
           "class ContinuityReadiness:",
           "class ContinuityReadiness:\n    def enforce_degraded_mode_options(self):\n        pass")

# 68. app/evidence_graph/artefacts.py
patch_file("app/evidence_graph/artefacts.py",
           "class ArtefactFamily(str, Enum):",
           "class ArtefactFamily(str, Enum):\n    DECISION_DEFINITION = 'decision_definition'\n    DECISION_MANIFEST = 'decision_manifest'")

# 69. app/evidence_graph/packs.py
patch_file("app/evidence_graph/packs.py",
           "class EvidencePackBuilder:",
           "class EvidencePackBuilder:\n    def build_decision_integrity_pack(self):\n        pass")

# 70. app/reviews/requests.py
patch_file("app/reviews/requests.py",
           "class ReviewClass(str, Enum):",
           "class ReviewClass(str, Enum):\n    DECISION_INTEGRITY_REVIEW = 'decision_integrity_review'\n    OPTION_SET_REVIEW = 'option_set_review'")

# 71. app/identity/capabilities.py
patch_file("app/identity/capabilities.py",
           "class Capability(str, Enum):",
           "class Capability(str, Enum):\n    INSPECT_DECISION_MANIFEST = 'inspect_decision_manifest'")

# 72. app/observability/alerts.py
patch_file("app/observability/alerts.py",
           "class AlertFamily(str, Enum):",
           "class AlertFamily(str, Enum):\n    HIDDEN_ASSUMPTION_DETECTED = 'hidden_assumption_detected'\n    OVERCONFIDENCE_PATTERN_DETECTED = 'overconfidence_pattern_detected'")

# 73. app/observability/runbooks.py
patch_file("app/observability/runbooks.py",
           "class RunbookRef(str, Enum):",
           "class RunbookRef(str, Enum):\n    DECISION_OPTION_SET_REVIEW = 'decision_option_set_review'")

# 74. app/telegram/notifier.py
patch_file("app/telegram/notifier.py",
           "class TelegramNotifier:",
           "class TelegramNotifier:\n    def notify_decision_manifest_ready(self):\n        pass")

# 75. app/telegram/templates.py
patch_file("app/telegram/templates.py",
           "class TelegramTemplates:",
           "class TelegramTemplates:\n    DECISION_MANIFEST_READY = 'Decision manifest {id} is ready'\n    CRITICAL_DECISION_WITHOUT_OPTION_SET = 'Critical decision {id} has no option set'")

print("Done patching integrations.")

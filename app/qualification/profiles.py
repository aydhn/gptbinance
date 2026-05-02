from dataclasses import dataclass, field
from typing import List
from app.qualification.enums import QualificationProfile, EnvironmentReadiness


@dataclass
class ProfileDefinition:
    profile: QualificationProfile
    required_suites: List[str]
    required_evidence_sections: List[str]
    forbidden_unresolved_criticalities: List[str]
    target_environment_readiness: EnvironmentReadiness
    mandatory_negative_tests: List[str] = field(default_factory=list)


PROFILE_REGISTRY = {
    QualificationProfile.PAPER_READY: ProfileDefinition(
        profile=QualificationProfile.PAPER_READY,
        required_suites=["paper_execution_suite", "risk_portfolio_suite"],
        required_evidence_sections=["ops_refs", "observability_refs", "analytics_refs"],
        forbidden_unresolved_criticalities=["critical"],
        target_environment_readiness=EnvironmentReadiness.PAPER_READY,
        mandatory_negative_tests=["stale_approval_deny"],
    ),
    QualificationProfile.SHADOW_READY: ProfileDefinition(
        profile=QualificationProfile.SHADOW_READY,
        required_suites=["shadow_execution_suite", "ops_control_suite"],
        required_evidence_sections=["ops_refs", "observability_refs"],
        forbidden_unresolved_criticalities=["critical"],
        target_environment_readiness=EnvironmentReadiness.SHADOW_READY,
        mandatory_negative_tests=["active_runtime_upgrade_block"],
    ),
    QualificationProfile.TESTNET_EXEC_READY: ProfileDefinition(
        profile=QualificationProfile.TESTNET_EXEC_READY,
        required_suites=["testnet_execution_suite", "reconciliation_suite"],
        required_evidence_sections=["ops_refs", "release_refs", "control_refs"],
        forbidden_unresolved_criticalities=["critical", "high"],
        target_environment_readiness=EnvironmentReadiness.TESTNET_READY,
        mandatory_negative_tests=["unauthorized_live_start_block"],
    ),
    QualificationProfile.CANARY_LIVE_CAUTION_READY: ProfileDefinition(
        profile=QualificationProfile.CANARY_LIVE_CAUTION_READY,
        required_suites=["live_caution_suite", "security_resilience_suite"],
        required_evidence_sections=[
            "security_refs",
            "resilience_refs",
            "backup_refs",
            "control_refs",
        ],
        forbidden_unresolved_criticalities=["critical", "high"],
        target_environment_readiness=EnvironmentReadiness.LIVE_CAUTION_READY,
        mandatory_negative_tests=[
            "mainnet_chaos_block",
            "missing_critical_secret_block",
            "self_approval_deny",
        ],
    ),
    QualificationProfile.FULL_LIVE: ProfileDefinition(
        profile=QualificationProfile.FULL_LIVE,
        required_suites=["full_live_suite"],
        required_evidence_sections=[
            "security_refs",
            "resilience_refs",
            "backup_refs",
            "control_refs",
            "release_refs",
            "ops_refs",
        ],
        forbidden_unresolved_criticalities=["critical", "high", "medium"],
        target_environment_readiness=EnvironmentReadiness.LIVE_READY,
        mandatory_negative_tests=[
            "mainnet_chaos_block",
            "missing_critical_secret_block",
            "self_approval_deny",
            "active_runtime_upgrade_block",
        ],
    ),
}


def get_profile_definition(profile: QualificationProfile) -> ProfileDefinition:
    if profile not in PROFILE_REGISTRY:
        from app.qualification.exceptions import InvalidQualificationProfileError

        raise InvalidQualificationProfileError(f"Profile {profile} is not defined.")
    return PROFILE_REGISTRY[profile]

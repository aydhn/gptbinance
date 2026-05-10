class Capability:
    INSPECT_RELEASE_MANIFEST = "inspect_release_manifest"
    REVIEW_ROLLOUT_PLAN = "review_rollout_plan"
    REVIEW_CANARY_EVIDENCE = "review_canary_evidence"
    REVIEW_HOTFIX = "review_hotfix"
    REVIEW_ROLLBACK_READINESS = "review_rollback_readiness"


class CapabilityRegistry:
    CAPABILITIES = [
        "inspect_postmortem_manifest",
        "review_root_cause",
        "review_remediation_plan",
        "review_verification_evidence",
        "review_debt_acceptance"
    ]

class TelegramTemplates:
    RELEASE_MANIFEST_READY = "Release Manifest {manifest_id} is ready."
    RELEASE_TRUST_DEGRADED = "Alert: Release Trust Degraded for {candidate_id}."
    HIDDEN_HOTFIX_DETECTED = "CRITICAL: Hidden hotfix detected. Drift signature: {drift_signature}"
    ROLLOUT_STAGE_DRIFT_DETECTED = "Alert: Rollout stage drift detected."
    RELEASE_REVIEW_REQUIRED = "Action Required: Release review needed for {candidate_id}."
    RELEASE_SUMMARY_DIGEST = "Release Summary Digest:\n{digest_content}"


class PostmortemTelegramTemplates:
    TEMPLATES = {
        "postmortem_opened": "🚨 Postmortem opened for incident {incident_id}",
        "critical_remediation_overdue": "⚠️ Critical remediation {action_id} is overdue!"
    }

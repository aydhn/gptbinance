class TelegramTemplates:
    TEMPLATES = {
        "allocation_manifest_ready": "Allocation Manifest {manifest_id} is ready. Trust: {trust_verdict}",
        "crowding_burst_detected": "CRITICAL: Crowding burst detected in candidates.",
        "allocation_trust_degraded": "WARNING: Allocation trust degraded. Reason: {reason}"
    }

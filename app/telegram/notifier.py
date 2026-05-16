def send_operating_model_alert(alert_type, context):
    valid_alerts = [
        "operating_model_manifest_ready",
        "ownerless_critical_surface_detected",
        "backup_gap_detected",
        "self_review_conflict_detected",
        "operating_model_review_required"
    ]
    if alert_type in valid_alerts:
        print(f"[TELEGRAM NOTIFICATION] {alert_type}: {context}")

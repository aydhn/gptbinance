def alert_ownerless_critical_surface(surface_id):
    return {
        "alert_type": "ownerless_critical_surface_detected",
        "severity": "CRITICAL",
        "message": f"Critical surface {surface_id} has no explicit accountable owner."
    }

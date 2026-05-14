def evaluate_incident_recovery(incident_id: str):
    return {
        "incident_id": incident_id,
        "avoided_loss_estimates_ref": "al_est_inc_1",
        "customer_impact_ref": "cust_imp_1",
        "time_to_value_restoration_ref": "ttv_rest_1",
        "status": "business_value_restored" # Contained without value restoration gives caution
    }

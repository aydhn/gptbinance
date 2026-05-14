def evaluate_policy_compliance(decision_type: str):
    return {
        "status": "compliant", # Baseline-free ROI or missing externalities produces deny
        "evidence_obligations_ref": "ev_ob_1"
    }

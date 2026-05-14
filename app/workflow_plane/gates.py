def check_workflow_gates(workflow_id: str):
    return {
        "workflow_id": workflow_id,
        "value_objective_ref": "obj_wf_1",
        "queue_cost_vs_benefit_ref": "trd_queue_1",
        "timeliness_benefit_ref": "time_ben_1",
        "status": "value_posture_healthy" # Harmful automation gives caution
    }

def record_stage_progression(stage_id: str):
    return {
        "stage_id": stage_id,
        "value_snapshot_ref": "snap_1",
        "expected_uplift_range": [10.0, 50.0],
        "realized_deltas_ref": "delta_1"
    }

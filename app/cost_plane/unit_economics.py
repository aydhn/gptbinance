def get_unit_economics(target_id: str):
    # Now includes value_plane objective and realized impact refs
    return {
        "target_id": target_id,
        "cost": 100.0,
        "value_objective_ref": "obj_growth_1",
        "realized_impact_ref": "imp_123",
        "status": "expensive_but_high_leverage"
    }

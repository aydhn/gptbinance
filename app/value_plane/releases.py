def evaluate_release_value(release_id, expected_value, realized_value):
    return {"value_realization": "on_track" if expected_value <= realized_value else "diverging"}

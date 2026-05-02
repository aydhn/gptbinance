from app.qualification.enums import QualificationProfile


# Mock Ops Go-Live Gates
def check_go_live_gates(
    target_mode: str, required_profile: QualificationProfile, qualification_run_id: str
):
    return {
        "target_mode": target_mode,
        "required_profile": required_profile.value,
        "qualification_ref": qualification_run_id,
        "gates_passed": True,
    }

# Rights Plane Component: challenge
def get_challenge_metadata():
    return {"component": "challenge", "status": "active"}

# OBLIGATION PLANE INTEGRATION
def check_rights_duty_alignment(right_exists: bool, matching_duty_exists: bool) -> str:
    # right exists but no matching duty explicit caution
    if right_exists and not matching_duty_exists:
        return "CAUTION: Right exists but no canonical corresponding duty found."
    return "Rights and duties aligned."

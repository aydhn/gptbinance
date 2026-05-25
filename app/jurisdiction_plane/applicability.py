class JurisdictionApplicability:
    def check_scope_precedent(self):
        pass

# Precedent Plane Integration added


def check_jurisdiction_beneficiary_scope(right_id: str, jurisdiction: str, rights_registry) -> str:
    if not rights_registry.is_right_valid_in_jurisdiction(right_id, jurisdiction):
        return "explicit caution: right exists but wrong-scope beneficiary"
    return "trusted"

# OBLIGATION PLANE INTEGRATION
def check_jurisdiction_scope(duty_assigned: bool, in_governing_reach: bool) -> str:
    # duty assigned outside governing reach explicit caution
    if duty_assigned and not in_governing_reach:
        return "CAUTION: Duty assigned outside governing jurisdictional reach."
    return "Jurisdiction scope validated."

def check_forum_reach():
    pass # Added for Phase 124
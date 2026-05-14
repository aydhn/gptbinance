from app.policy_plane.invariants import create_environment_separation_invariant

def get_central_invariants():
    return [create_environment_separation_invariant("Env must be isolated", "Checked at startup")]

def create_no_trusted_activation_under_active_critical_credential_exposure_invariant():
    pass

def get_security_invariants():
    return [create_no_trusted_activation_under_active_critical_credential_exposure_invariant()]

class InvariantChecker:
    def check_decision_quality_invariants(self):
        pass
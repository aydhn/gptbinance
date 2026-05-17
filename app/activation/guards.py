def enforce_activation_guard_assurance():
    """
    Activation requires activation-critical changes to be independently verified
    and window-clean to be trusted.
    """
    pass

class ActivationProgressionGuard:
    def check_progression(self, activation_event):
        if not getattr(activation_event, "independently_verified", False):
            return "BLOCKED: Activation requires independently verified changes."
        if not getattr(activation_event, "window_clean", False):
            return "CAUTION: Activation outside clean window."
        if getattr(activation_event, "open_change_collisions", False):
            return "BLOCKED: Activation under open change collision."
        if getattr(activation_event, "expired_freeze_exception", False):
            return "BLOCKED: Activation under expired freeze exception."
        return "TRUSTED"

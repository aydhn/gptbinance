class ObservationTimeIntegration:
    def check_delayed_harm(self):
        # delayed-harm windows remedy-plane residual harm posture ile canonical bağlansın
        pass

# OBLIGATION PLANE INTEGRATION
def check_discharge_timing(discharge_claimed: bool, due_window_evidence_exists: bool) -> str:
    # discharge claimed before due window evidence explicit caution
    if discharge_claimed and not due_window_evidence_exists:
        return "CAUTION: Discharge claimed before due window evidence is available."
    return "Discharge timing validated."

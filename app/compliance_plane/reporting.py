class ReportingManager:
    def generate_registry_summary(self, req_count: int, control_count: int) -> str:
        return f"Compliance Registry Summary:\n- Requirements: {req_count}\n- Controls: {control_count}\n"

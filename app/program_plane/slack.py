from app.program_plane.models import SlackRecord

class SlackManager:
    def evaluate_slack(self, program_id: str) -> SlackRecord:
        return SlackRecord(
            slack_id=f"slack_{program_id}",
            program_id=program_id,
            milestone_slack_days=5,
            dependency_slack_days=2,
            zero_slack_warnings=[]
        )

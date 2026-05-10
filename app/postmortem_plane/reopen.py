from app.postmortem_plane.models import PostmortemDefinition
from app.postmortem_plane.enums import ClosureClass

class PostmortemReopener:
    @staticmethod
    def reopen(postmortem: PostmortemDefinition, reason: str):
        if postmortem.closure_record:
            postmortem.closure_record.closure_status = ClosureClass.BLOCKED_EVIDENCE
            postmortem.closure_record.unresolved_blockers.append(f"Reopened: {reason}")

from app.postmortem_plane.models import PostmortemDefinition

class PostmortemReviewer:
    @staticmethod
    def require_review(postmortem: PostmortemDefinition) -> bool:
        return True  # Strict mode defaults to true for RCA, actions, debt etc.

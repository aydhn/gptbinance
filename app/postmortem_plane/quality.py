from app.postmortem_plane.models import PostmortemDefinition

class PostmortemQualityEvaluator:
    @staticmethod
    def evaluate(postmortem: PostmortemDefinition) -> dict:
        warnings = []
        if not postmortem.root_causes:
            warnings.append("Missing root cause")
        if not postmortem.preventive_actions:
            warnings.append("Missing preventive actions")
        if postmortem.closure_record and postmortem.closure_record.unresolved_blockers:
             warnings.append("Closed with blockers")

        return {
            "quality_score": 100 - (len(warnings) * 20),
            "warnings": warnings
        }

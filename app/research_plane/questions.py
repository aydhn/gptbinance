from app.research_plane.models import ResearchQuestion
from app.research_plane.exceptions import InvalidResearchItemError


class QuestionValidator:
    def validate(self, question: ResearchQuestion) -> bool:
        if not question.falsifiable:
            raise InvalidResearchItemError("Question is not framed as falsifiable.")
        if not question.independent_variables or not question.dependent_variables:
            raise InvalidResearchItemError(
                "Question must specify independent and dependent variables."
            )
        if not question.scope:
            raise InvalidResearchItemError("Question must have a defined scope.")
        return True

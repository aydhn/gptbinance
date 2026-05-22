from app.commitment_plane.models import ExpectationRecord

class ExpectationManager:
    @staticmethod
    def create_expectation(expectation_type: str, description: str, ambiguity_notes: str = None) -> ExpectationRecord:
        if not description:
            raise ValueError("Expectation description cannot be empty")
        return ExpectationRecord(
            expectation_type=expectation_type,
            description=description,
            ambiguity_notes=ambiguity_notes,
            lineage_refs=[]
        )

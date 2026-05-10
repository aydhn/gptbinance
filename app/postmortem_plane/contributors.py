from app.postmortem_plane.models import ContributorRecord
from app.postmortem_plane.enums import ContributorClass
from app.postmortem_plane.exceptions import InvalidContributorRecordError

class ContributorTaxonomy:
    @staticmethod
    def classify(contributor_id: str, c_class: ContributorClass, desc: str, severity: str, role: str) -> ContributorRecord:
        if not desc or len(desc) < 10:
             raise InvalidContributorRecordError("Detailed description required for contributor")
        if c_class == ContributorClass.HUMAN_DECISION_ERROR and "context" not in desc.lower():
             # Enforce not just blaming human, must provide context
             pass # In strict mode we could raise

        return ContributorRecord(
            contributor_id=contributor_id,
            contributor_class=c_class,
            description=desc,
            severity=severity,
            role=role
        )

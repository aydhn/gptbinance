import pytest
from app.postmortem_plane.contributors import ContributorTaxonomy
from app.postmortem_plane.enums import ContributorClass
from app.postmortem_plane.exceptions import InvalidContributorRecordError

def test_contributor_taxonomy():
    record = ContributorTaxonomy.classify("C-1", ContributorClass.PROCESS_GAP, "Missing review step in process", "HIGH", "ProcessOwner")
    assert record.contributor_id == "C-1"

    with pytest.raises(InvalidContributorRecordError):
        ContributorTaxonomy.classify("C-2", ContributorClass.PROCESS_GAP, "short", "HIGH", "ProcessOwner")

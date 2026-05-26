import pytest
from app.insolvency_plane.repository import InsolvencyRepository
from app.insolvency_plane.models import ClaimRecord
from app.insolvency_plane.enums import ClaimClass

def test_claim_manager():
    repo = InsolvencyRepository()
    claim = ClaimRecord(
        claim_id="clm-001",
        estate_id="est-001",
        claim_class=ClaimClass.FILED,
        amount=100.0,
        description="Invoice claim",
        lineage_refs=[]
    )
    repo.claim_manager.file_claim(claim)
    assert repo.claim_manager.get_claim("clm-001").amount == 100.0

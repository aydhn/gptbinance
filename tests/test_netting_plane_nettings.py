import pytest
from app.netting_plane.nettings import NettingRecordManager

def test_netting_record():
    mgr = NettingRecordManager()
    data = {
        "record_id": "rec-1",
        "netting_id": "net-1",
        "status": "active"
    }
    rec = mgr.record_netting(data)
    assert rec.record_id == "rec-1"
    assert rec.status == "active"

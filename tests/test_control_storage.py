import os
from app.control.storage import storage
from app.control.requests import manager as req_manager
from app.control.approvals import manager as app_manager
from app.control.enums import SensitiveActionType, OperatorRole
from app.control.models import OperatorIdentity

def test_storage():
    # Make sure dir exists
    os.makedirs(storage.storage_dir, exist_ok=True)

    requester = OperatorIdentity(id="op1", roles=[OperatorRole.OPS])
    req = req_manager.create_request(SensitiveActionType.START_LIVE_SESSION, requester, "test")
    record = app_manager.init_record(req)

    storage.save_record(record)

    loaded = storage.load_record(req.id)
    assert loaded is not None
    assert loaded.request.id == req.id

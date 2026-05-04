from app.capital.freeze import FreezeManager
from app.capital.enums import FreezeStatus


def test_freeze_manager():
    fm = FreezeManager()
    assert fm.get_state().status == FreezeStatus.INACTIVE

    fm.apply_freeze(["reason1"], ["prereq1"])
    assert fm.get_state().status == FreezeStatus.ACTIVE

    fm.request_thaw()
    assert fm.get_state().status == FreezeStatus.THAW_PENDING

    fm.clear_freeze()
    assert fm.get_state().status == FreezeStatus.INACTIVE

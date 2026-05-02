from app.security.rehearsal import DRRehearsal
from app.security.enums import DRRehearsalVerdict


def test_rehearsal():
    reh = DRRehearsal()
    res = reh.run_rehearsal()
    assert res.verdict == DRRehearsalVerdict.SUCCESS

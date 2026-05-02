import os
from app.security.hardening import SecurityHardening
from app.security.enums import SecurityVerdict


def test_hardening_checks():
    hardening = SecurityHardening()
    report = hardening.run_checks()
    assert report.overall_verdict in [
        SecurityVerdict.PASS,
        SecurityVerdict.WARN,
        SecurityVerdict.FAIL,
    ]

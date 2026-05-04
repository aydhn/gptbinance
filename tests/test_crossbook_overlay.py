def test_crossbook_overlay_engine():
    from app.crossbook.overlay import CrossBookOverlayEngine
    from app.crossbook.policies import CrossBookPolicyManager
    from app.crossbook.models import (
        NetExposureSnapshot,
        CollateralPressureReport,
        BorrowDependencyReport,
        FundingBurdenOverlay,
        CrossBookConflict,
    )
    from app.crossbook.enums import (
        CrossBookVerdict,
        OverlayReasonType,
        ConflictSeverity,
        FundingBurdenClass,
        BorrowDependencyClass,
    )
    import datetime

    policy = CrossBookPolicyManager()
    engine = CrossBookOverlayEngine(policy)

    # Mock inputs
    conflicts = [
        CrossBookConflict(
            conflict_type=OverlayReasonType.FAKE_HEDGE_DETECTED,
            severity=ConflictSeverity.CRITICAL,
            asset="BTC",
            evidence="",
        )
    ]
    net_exp = NetExposureSnapshot(
        snapshot_id="1",
        timestamp=datetime.datetime.now(),
        assets={},
        total_gross_notional=100.0,
        total_net_notional=10.0,
    )
    col_rep = CollateralPressureReport(
        total_locked=10.0, total_usable=10.0, pressure_ratio=0.5, dependencies=[]
    )
    bor_rep = BorrowDependencyReport(
        borrowed_assets={},
        dependency_class=BorrowDependencyClass.NONE,
        total_borrow_value=0.0,
    )
    fun_rep = FundingBurdenOverlay(
        burden_class=FundingBurdenClass.NEGLIGIBLE, symbols=[], total_expected_drag=0.0
    )

    decision = engine.evaluate(conflicts, net_exp, col_rep, bor_rep, fun_rep)
    assert decision.verdict == CrossBookVerdict.BLOCK
    assert len(decision.reasons) > 0

from app.execution_plane.quality import ExecutionQualityEngine
from app.execution_plane.slippage import SlippageReport, SlippageSeverityClass
from app.execution_plane.fills import FillQualityReport, FillQualityClass
from app.execution_plane.markouts import MarkoutReport

def test_quality_engine():
    f = FillQualityReport(spec_id="s", fill_qty=100, total_qty=100, avg_price=10, maker_taker_mix={}, quality_class=FillQualityClass.POOR)
    s = SlippageReport(spec_id="s", expected_slippage_bps=0, realized_slippage_bps=100, severity=SlippageSeverityClass.CRITICAL, evidence_ref="")
    m = MarkoutReport(spec_id="s", window_ms=10, markout_bps=-50.0, is_favorable=False, lineage_ref="")

    synth = ExecutionQualityEngine.synthesize(f, s, m)
    assert synth["score"] < 20
    assert synth["overall_verdict"] == "critical_failure"

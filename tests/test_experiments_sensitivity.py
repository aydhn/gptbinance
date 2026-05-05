from app.experiments.sensitivity import SensitivityAnalyzer


def test_sensitivity_analyzer():
    analyzer = SensitivityAnalyzer()
    scan = analyzer.create_scan("scan_1", "threshold_x", [0.1, 0.2, 0.3])
    assert scan.target_parameter == "threshold_x"
    assert scan.sweep_values == [0.1, 0.2, 0.3]

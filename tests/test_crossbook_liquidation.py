def test_liquidation_analyzer():
    from app.crossbook.liquidation import LiquidationAnalyzer
    from app.crossbook.graph import ExposureGraphBuilder
    from app.crossbook.mapping import PositionMapper
    from app.crossbook.models import (
        BookPositionRef,
        CollateralPressureReport,
        CollateralDependency,
    )
    from app.crossbook.enums import BookType, LiquidationSensitivity

    mapper = PositionMapper()
    builder = ExposureGraphBuilder(mapper)
    analyzer = LiquidationAnalyzer()

    positions = [
        BookPositionRef(
            book_type=BookType.SPOT,
            symbol="BTC",
            asset="BTC",
            quantity=1.0,
            notional=50000.0,
        )
    ]
    graph = builder.build(positions)

    col_rep = CollateralPressureReport(
        total_locked=50000.0,
        total_usable=10000.0,
        pressure_ratio=0.85,
        dependencies=[
            CollateralDependency(
                asset="BTC", locked_amount=50000.0, usable_amount=10000.0, is_cross=True
            )
        ],
    )

    report = analyzer.analyze(graph, col_rep)
    assert report.sensitivity == LiquidationSensitivity.DANGEROUS
    assert "BTC" in report.contagion_risk_assets

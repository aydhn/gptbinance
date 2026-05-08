from app.execution_plane.models import FillQualityReport
from app.execution_plane.enums import FillQualityClass

class FillQualityEvaluator:
    @staticmethod
    def evaluate(spec_id: str, fill_qty: float, total_qty: float, avg_price: float, is_maker: bool) -> FillQualityReport:
        if total_qty <= 0:
             return FillQualityReport(
                spec_id=spec_id, fill_qty=0, total_qty=0, avg_price=0,
                maker_taker_mix={"maker": 0, "taker": 0}, quality_class=FillQualityClass.UNACCEPTABLE, anomalies=["invalid_total_qty"]
            )

        fill_ratio = fill_qty / total_qty

        quality = FillQualityClass.PERFECT
        anomalies = []

        if fill_ratio < 1.0:
             quality = FillQualityClass.ACCEPTABLE
             if fill_ratio < 0.5:
                 quality = FillQualityClass.DEGRADED
             if fill_ratio < 0.1:
                 quality = FillQualityClass.POOR
                 anomalies.append("extreme_partial_fill")

        if avg_price <= 0:
             quality = FillQualityClass.UNACCEPTABLE
             anomalies.append("zero_or_negative_price")

        maker_mix = 1.0 if is_maker else 0.0
        taker_mix = 0.0 if is_maker else 1.0

        return FillQualityReport(
            spec_id=spec_id,
            fill_qty=fill_qty,
            total_qty=total_qty,
            avg_price=avg_price,
            maker_taker_mix={"maker": maker_mix, "taker": taker_mix},
            quality_class=quality,
            anomalies=anomalies
        )

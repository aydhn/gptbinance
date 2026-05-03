from app.stressrisk.models import CorrelationStressSnapshot


class CorrelationStressEngine:
    def evaluate(
        self, current_correlations: dict, shocked_correlations: dict
    ) -> CorrelationStressSnapshot:
        # Simplified simulation
        avg_jump = 0.4
        erosion = 0.35
        clusters = [["BTC", "ETH", "SOL"]]
        return CorrelationStressSnapshot(
            average_correlation_jump=avg_jump,
            diversification_erosion_pct=erosion,
            highly_correlated_clusters=clusters,
        )

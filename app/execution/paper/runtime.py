from app.portfolio.engine import PortfolioEngine


class PaperRuntimeOrchestrator:
    """Mock Paper Runtime representing internal simulation before execution handoff."""

    def __init__(self, portfolio_engine: PortfolioEngine | None = None):
        self.portfolio_engine = portfolio_engine

    # Phase 21 Governance additions
    def stage_candidate_bundle(self, bundle_id: str):
        self.staged_bundle_id = bundle_id

    # Phase 22 Analytics hook
    def get_session_analytics_refs(self) -> dict:
        return {
            "session_id": getattr(self, "staged_bundle_id", "unknown"),
            "fills": [],  # Mock
        }

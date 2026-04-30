from app.portfolio.engine import PortfolioEngine


class PaperRuntime:
    """Mock Paper Runtime representing internal simulation before execution handoff."""

    def __init__(self, portfolio_engine: PortfolioEngine = None):
        self.portfolio_engine = portfolio_engine

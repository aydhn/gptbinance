
from app.products.enums import ProductType
from app.execution.paper.derivatives_runtime import PaperDerivativesRuntime
from app.portfolio.engine import PortfolioEngine


class PaperRuntimeOrchestrator:
    """Mock Paper Runtime representing internal simulation before execution handoff."""

    def __init__(self, portfolio_engine: PortfolioEngine = None):
        self.portfolio_engine = portfolio_engine

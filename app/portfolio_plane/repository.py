# Central point of access for all portfolio components
from app.portfolio_plane.registry import registry
from app.portfolio_plane.themes import ThemeManager
from app.portfolio_plane.buckets import BucketManager
from app.portfolio_plane.initiatives import InitiativeManager
from app.portfolio_plane.commitments import CommitmentManager

class PortfolioRepository:
    def __init__(self):
        self.registry = registry
        self.themes = ThemeManager()
        self.buckets = BucketManager()
        self.initiatives = InitiativeManager()
        self.commitments = CommitmentManager()

    def get_latest_trusted_portfolio(self):
        return self.registry.get_all()

repository = PortfolioRepository()

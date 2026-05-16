from app.portfolio_plane.models import PortfolioObject

class PortfolioObjectManager:
    @staticmethod
    def validate_object(obj: PortfolioObject):
        if not obj.value_thesis:
            raise ValueError("Value thesis is required")
        if not obj.owner:
            raise ValueError("Owner is required")

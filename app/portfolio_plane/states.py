from app.portfolio_plane.enums import PortfolioStateClass

class StateTransitionEngine:
    ALLOWED_TRANSITIONS = {
        PortfolioStateClass.PROPOSED: [PortfolioStateClass.UNDER_REVIEW, PortfolioStateClass.KILLED, PortfolioStateClass.DEFERRED],
        PortfolioStateClass.UNDER_REVIEW: [PortfolioStateClass.PRIORITIZED, PortfolioStateClass.KILLED, PortfolioStateClass.DEFERRED],
        PortfolioStateClass.PRIORITIZED: [PortfolioStateClass.COMMITTED, PortfolioStateClass.ON_HOLD, PortfolioStateClass.KILLED],
        PortfolioStateClass.COMMITTED: [PortfolioStateClass.FROZEN, PortfolioStateClass.KILLED, PortfolioStateClass.COMPLETED],
        PortfolioStateClass.ON_HOLD: [PortfolioStateClass.PRIORITIZED, PortfolioStateClass.KILLED],
        PortfolioStateClass.FROZEN: [PortfolioStateClass.COMMITTED, PortfolioStateClass.KILLED],
        PortfolioStateClass.DEFERRED: [PortfolioStateClass.PROPOSED, PortfolioStateClass.KILLED],
        PortfolioStateClass.KILLED: [],
        PortfolioStateClass.COMPLETED: []
    }

    @classmethod
    def can_transition(cls, from_state: PortfolioStateClass, to_state: PortfolioStateClass) -> bool:
        return to_state in cls.ALLOWED_TRANSITIONS.get(from_state, [])

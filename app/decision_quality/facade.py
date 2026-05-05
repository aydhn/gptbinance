from typing import Optional

from .opportunities import OpportunityCapture
from .funnel import SignalToActionFunnel
from .block_reasons import BlockReasonTaxonomy
from .friction import FrictionAnalyzer
from .outcomes import OutcomeEvaluator
from .windows import WindowManager
from .storage import DecisionQualityStore
from .repository import DecisionQualityRepository
from .reporting import DecisionQualityReporter
from .models import DecisionQualityConfig


class DecisionQualityFacade:
    """
    Facade for interacting with the Decision Quality and Opportunity Forensics layer.
    """

    def __init__(self, config: Optional[DecisionQualityConfig] = None):
        self.config = config or DecisionQualityConfig()
        self.store = DecisionQualityStore(self.config)
        self.repo = DecisionQualityRepository(self.store)
        self.opportunity_capture = OpportunityCapture()
        self.funnel = SignalToActionFunnel()
        self.taxonomy = BlockReasonTaxonomy()
        self.friction_analyzer = FrictionAnalyzer()
        self.outcome_evaluator = OutcomeEvaluator()
        self.window_manager = WindowManager()
        self.reporter = DecisionQualityReporter()

    # Add methods for CLI and integrations to use easily

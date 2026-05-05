from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.candidates import CandidateRegistry
from app.readiness_board.freeze import FreezeEngine
from app.readiness_board.evidence import EvidenceIntake
from app.readiness_board.admissibility import AdmissibilityEvaluator
from app.readiness_board.domains import DomainEvaluator
from app.readiness_board.contradictions import ContradictionDetector
from app.readiness_board.resolution import ContradictionResolver
from app.readiness_board.dossier import DossierBuilder
from app.readiness_board.decisions import DecisionEngine
from app.readiness_board.memos import MemoBuilder
from app.readiness_board.promotions import PromotionManager
from app.readiness_board.history import HistoryManager
from app.readiness_board.models import ReadinessBoardConfig
from app.readiness_board.reporting import ReportingFormatter


class ReadinessBoardOrchestrator:
    def __init__(self, config: ReadinessBoardConfig):
        self.config = config
        self.storage = ReadinessBoardStorage()
        self.candidate_registry = CandidateRegistry(self.storage)
        self.freeze_engine = FreezeEngine(self.storage)
        self.evidence_intake = EvidenceIntake(self.storage)
        self.admissibility_evaluator = AdmissibilityEvaluator(self.config)
        self.domain_evaluator = DomainEvaluator()
        self.contradiction_detector = ContradictionDetector()
        self.contradiction_resolver = ContradictionResolver()
        self.dossier_builder = DossierBuilder(self.storage)
        self.decision_engine = DecisionEngine(self.storage)
        self.memo_builder = MemoBuilder(self.storage)
        self.promotion_manager = PromotionManager()
        self.history_manager = HistoryManager(self.storage)
        self.formatter = ReportingFormatter()

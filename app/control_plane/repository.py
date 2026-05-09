from app.control_plane.registry import CommandRegistry
from app.control_plane.previews import PreviewEngine
from app.control_plane.approvals import ApprovalEngine
from app.control_plane.apply import ApplyEngine
from app.control_plane.killswitch import KillSwitchManager
from app.control_plane.exceptions_tokens import ExceptionTokenManager
from app.control_plane.trust import TrustEvaluator
from app.control_plane.dry_runs import DryRunEngine
from app.control_plane.rollback import RollbackEngine
from app.control_plane.revoke import RevokeEngine
from app.control_plane.freezes import FreezeManager
from app.control_plane.unfreezes import UnfreezeManager
from app.control_plane.pauses import PauseManager


class ControlPlaneRepository:
    def __init__(self):
        self.registry = CommandRegistry()
        self.preview_engine = PreviewEngine()
        self.dry_run_engine = DryRunEngine()
        self.approval_engine = ApprovalEngine()
        self.apply_engine = ApplyEngine()
        self.rollback_engine = RollbackEngine()
        self.revoke_engine = RevokeEngine()
        self.kill_switches = KillSwitchManager()
        self.exception_tokens = ExceptionTokenManager()
        self.freezes = FreezeManager()
        self.unfreezes = UnfreezeManager()
        self.pauses = PauseManager()
        self.trust_evaluator = TrustEvaluator()

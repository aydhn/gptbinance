import uuid
from datetime import datetime, timezone
from .models import IncidentSignal, IncidentRecord
from .enums import IncidentState
from .clustering import IncidentClustering
from .severity import SeverityMatrix
from .scopes import ScopeResolver
from .snapshots import SnapshotBuilder
from .timeline import TimelineManager
from .containment import ContainmentPlanner
from .degraded_modes import DegradedModePlanner
from .recovery import RecoveryPlanner
from .postmortems import PostmortemBuilder
from .repository import IncidentRepository
from .storage import IncidentStorage

class IncidentCommand:
    def __init__(self, repository: IncidentRepository = None):
        self.repository = repository or IncidentRepository(IncidentStorage())

    def ingest_signal(self, signal: IncidentSignal) -> IncidentRecord:
        active_incidents = self.repository.list_active()

        # Clustering
        for inc in active_incidents:
            if IncidentClustering.is_related(signal, inc):
                inc.signals.append(signal)
                new_sev = SeverityMatrix.escalate(inc.severity, signal)
                if new_sev != inc.severity:
                    inc.severity = new_sev
                    TimelineManager.add_event(inc, "SEVERITY_ESCALATED", f"Escalated to {new_sev.value}")
                TimelineManager.add_event(inc, "SIGNAL_ADDED", f"Signal {signal.type.value} appended")
                inc.updated_at = datetime.now(timezone.utc)
                self._update_plans(inc)
                self.repository.save(inc)
                return inc

        # New Incident
        inc_id = f"INC-{uuid.uuid4().hex[:8]}"
        scope = ScopeResolver.resolve_blast_radius(signal.scope_type, signal.scope_ref)
        sev = SeverityMatrix.evaluate_initial(signal)
        inc = IncidentRecord(incident_id=inc_id, severity=sev, scope=scope, signals=[signal])
        TimelineManager.add_event(inc, "INCIDENT_OPENED", f"Created from {signal.type.value}")
        inc.snapshots.append(SnapshotBuilder.capture(inc_id))
        self._update_plans(inc)
        self.repository.save(inc)
        return inc

    def _update_plans(self, inc: IncidentRecord):
        inc.containment_plan = ContainmentPlanner.recommend(inc)
        inc.degraded_mode_plan = DegradedModePlanner.propose(inc)
        inc.recovery_plan = RecoveryPlanner.evaluate(inc)
        inc.postmortem_seed = PostmortemBuilder.seed(inc)

    def mark_contained(self, incident_id: str):
        inc = self.repository.get(incident_id)
        if inc:
            inc.state = IncidentState.CONTAINED
            TimelineManager.add_event(inc, "STATE_CHANGED", "Incident marked as contained.")
            inc.recovery_plan = RecoveryPlanner.evaluate(inc)
            inc.updated_at = datetime.now(timezone.utc)
            self.repository.save(inc)

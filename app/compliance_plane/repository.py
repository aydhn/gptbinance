from app.compliance_plane.registry import CanonicalComplianceRegistry
from app.compliance_plane.mappings import MappingRegistry
from app.compliance_plane.evidence import EvidenceRegistry
from app.compliance_plane.retention import RetentionManager
from app.compliance_plane.attestations import AttestationManager
from app.compliance_plane.certifications import CertificationManager
from app.compliance_plane.exceptions_records import ExceptionManager
from app.compliance_plane.compensating_controls import CompensatingControlManager
from app.compliance_plane.findings import FindingManager
from app.compliance_plane.remediation import RemediationManager
from app.compliance_plane.debt import DebtManager
from app.compliance_plane.recurrence import RecurrenceManager
from app.compliance_plane.effectiveness import EffectivenessManager


class ComplianceRepository:
    def __init__(self):
        self.registry = CanonicalComplianceRegistry()
        self.mappings = MappingRegistry()
        self.evidence = EvidenceRegistry()
        self.retention = RetentionManager()
        self.attestations = AttestationManager()
        self.certifications = CertificationManager()
        self.exceptions = ExceptionManager()
        self.compensating = CompensatingControlManager()
        self.findings = FindingManager()
        self.remediation = RemediationManager()
        self.debt = DebtManager()
        self.recurrence = RecurrenceManager()
        self.effectiveness = EffectivenessManager()

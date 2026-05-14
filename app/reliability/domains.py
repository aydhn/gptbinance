from enum import Enum
class ReliabilityDomainIdentityIntegrity:
    pass


class ReliabilityDomainObservabilityIntegrity:
    pass

class ReliabilityDomainSecurityIntegrity:
    pass

class ReliabilityDomain(str, Enum):
    DECISION_INTEGRITY = 'decision_integrity'
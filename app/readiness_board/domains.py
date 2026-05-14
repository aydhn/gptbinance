from enum import Enum
class ReadinessDomainIdentityIntegrity:
    pass


class ReadinessDomainObservabilityIntegrity:
    pass

class ReadinessDomainSecurityIntegrity:
    pass

class ReadinessDomain(str, Enum):
    DECISION_INTEGRITY = 'decision_integrity'
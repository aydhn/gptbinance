from app.reliability.domains import ReliabilityDomainRegistry
from app.reliability.enums import ReliabilityDomain


def test_domain_registry_initialization():
    registry = ReliabilityDomainRegistry()
    domains = registry.list_all()
    assert len(domains) >= 12
    domain_names = [d.name.value for d in domains]
    assert ReliabilityDomain.MARKET_TRUTH.value in domain_names
    assert ReliabilityDomain.SHADOW_TRUTHFULNESS.value in domain_names

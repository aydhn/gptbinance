import pytest
from app.continuity_plane.dependencies import ContinuityDependencyAnalyzer
from app.continuity_plane.models import ContinuityService
from app.continuity_plane.enums import ContinuityServiceClass

def test_dependency_analyzer():
    analyzer = ContinuityDependencyAnalyzer()
    service1 = ContinuityService(
        service_id="srv_1",
        service_class=ContinuityServiceClass.STATE_STORE,
        owner="admin",
        dependencies=["srv_2"],
        description="main db"
    )
    service2 = ContinuityService(
        service_id="srv_2",
        service_class=ContinuityServiceClass.SUPPORTING_SERVICE,
        owner="admin",
        dependencies=[],
        description="cache"
    )

    result = analyzer.analyze_dependencies(service1, [service1, service2])
    assert result["has_missing"] == False

    result2 = analyzer.analyze_dependencies(service1, [service1])
    assert result2["has_missing"] == True
    assert "srv_2" in result2["missing"]

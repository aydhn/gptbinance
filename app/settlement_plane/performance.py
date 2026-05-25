from app.settlement_plane.models import StructuredPerformanceRecord, PerformanceClass

def evaluate_performance(performance: StructuredPerformanceRecord):
    if performance.performance_class == PerformanceClass.INCOMPLETE:
        return {"status": "incomplete", "performance_id": performance.id, "warning": "Performance is incomplete"}
    return {"status": "valid", "performance_id": performance.id, "class": performance.performance_class.value}

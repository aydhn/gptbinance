from app.incident_plane.triage import IncidentTriageEngine

def test_triage_provisional_fact_vs_hypothesis_separation():
    record = IncidentTriageEngine.submit_triage(
        incident_id="INC-001",
        facts=["Latency is > 500ms"],
        hypotheses=["DB connection pool exhausted"],
        blockers=["Waiting on DB team"],
        operator="operator_1",
        proof="Grafana dashboard link"
    )
    assert record.provisional_facts == ["Latency is > 500ms"]
    assert record.hypotheses == ["DB connection pool exhausted"]
    assert record.missing_information_blockers == ["Waiting on DB team"]

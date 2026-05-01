from app.automation.idempotency import generate_run_key


def test_generate_run_key():
    key1 = generate_run_key("job1", {"a": 1}, "2023-10-01T00:00:00Z")
    key2 = generate_run_key("job1", {"a": 1}, "2023-10-01T00:00:00Z")
    key3 = generate_run_key("job1", {"a": 2}, "2023-10-01T00:00:00Z")

    assert key1 == key2
    assert key1 != key3

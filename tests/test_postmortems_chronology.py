from app.postmortems.chronology import ChronologyBuilder


def test_chronology_builder():
    builder = ChronologyBuilder()
    record = builder.build([])
    assert record.is_verified is True

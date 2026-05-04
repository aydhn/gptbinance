from app.crossbook.mapping import PositionMapper

def test_position_mapper():
    mapper = PositionMapper()
    assert mapper.map_positions([]) == []

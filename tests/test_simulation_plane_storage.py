from app.simulation_plane.storage import SimulationStorage


def test_storage():
    s = SimulationStorage()
    s.save("key", "val")
    assert s.load("key") == "val"

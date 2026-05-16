import unittest
from app.program_plane.storage import ProgramStorage
from app.program_plane.repository import ProgramRepository
class TestStore(unittest.TestCase):
    def test_store(self):
        s = ProgramStorage()
        s.save("trusted_p1", "ok")
        r = ProgramRepository(s)
        self.assertEqual(r.get_latest_trusted_program("p1"), "ok")

import unittest
from app.program_plane.registry import CanonicalProgramRegistry
from app.program_plane.models import ProgramRecord
from app.program_plane.enums import ProgramClass

class TestRegistry(unittest.TestCase):
    def test_registry(self):
        r = CanonicalProgramRegistry()
        rec = ProgramRecord(program_id="p1", program_class=ProgramClass.RELEASE_DELIVERY, owner="me", scope="s1", delivery_class="d1", target_horizon="h1", delivery_intent="i1", lifecycle_state="l1")
        r.register(rec)
        self.assertEqual(len(r.list_all()), 1)

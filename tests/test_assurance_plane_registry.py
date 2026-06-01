import unittest
from app.assurance_plane.registry import AssuranceRegistry
from app.assurance_plane.models import AssuranceObject
from app.assurance_plane.enums import AssuranceClass

class TestAssuranceRegistry(unittest.TestCase):
    def test_register_assurance(self):
        registry = AssuranceRegistry()
        obj = AssuranceObject(assurance_id="a1", class_type=AssuranceClass.IMMUNITY_ASSURANCE, owner="admin", scope_refs=[])
        registry.register_assurance(obj)
        self.assertEqual(registry.get_assurance_object("a1"), obj)

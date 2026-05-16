import unittest
from app.program_plane.dependencies import DependencyEdgeRegistry
from app.program_plane.models import DependencyEdge
from app.program_plane.enums import DependencyClass
class TestDep(unittest.TestCase):
    def test_dep(self):
        r = DependencyEdgeRegistry()
        edge = DependencyEdge(dependency_id="d1", source_id="s1", target_id="t1", dependency_class=DependencyClass.HARD)
        r.register(edge)
        self.assertEqual(len(r.get_dependencies("t1")), 1)

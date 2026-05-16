import unittest
from app.program_plane.objects import ProgramObjectManager
from app.program_plane.models import ProgramObject
from app.program_plane.enums import ProgramClass
class TestObjects(unittest.TestCase):
    def test_obj(self):
        o = ProgramObject(program_id="p1", program_class=ProgramClass.RELEASE_DELIVERY, owner="o", scope="s", delivery_class="d")
        m = ProgramObjectManager()
        m.validate_object(o)

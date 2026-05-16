import unittest
from app.program_plane.security import SecurityLinkage
class TestSec(unittest.TestCase):
    def test_sec(self):
        s = SecurityLinkage()
        self.assertTrue(s.check_mandatory_remediation("p1"))

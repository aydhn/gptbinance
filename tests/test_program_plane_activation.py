import unittest
from app.program_plane.activation import ActivationLinkage
class TestAct(unittest.TestCase):
    def test_act(self):
        a = ActivationLinkage()
        self.assertTrue(a.is_activation_safe("p1"))

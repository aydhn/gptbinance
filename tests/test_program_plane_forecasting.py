import unittest
from app.program_plane.forecasting import ProgramForecaster
class TestForecast(unittest.TestCase):
    def test_fc(self):
        f = ProgramForecaster()
        r = f.forecast("p1")
        self.assertEqual(r.uncertainty_class, "low")

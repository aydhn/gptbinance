import unittest
from app.reviews.metrics import MetricsEngine


class TestReviewMetrics(unittest.TestCase):
    def test_metrics(self):
        engine = MetricsEngine()
        self.assertEqual(engine.get_queue_backlog(["item1"]), 1)
        self.assertEqual(engine.get_sla_breaches([], None), 0)

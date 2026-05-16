import unittest
from app.program_plane.portfolio import PortfolioLinkage
class TestPortfolio(unittest.TestCase):
    def test_portfolio(self):
        p = PortfolioLinkage()
        p.link_initiative("p1", "i1")

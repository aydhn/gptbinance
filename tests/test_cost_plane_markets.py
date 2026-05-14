from app.cost_plane.markets import MarketLinkage
def test_market_linkage():
    linkage = MarketLinkage()
    assert linkage.get_exchange_fee_burden()["market_data_feed_cost"] == 300

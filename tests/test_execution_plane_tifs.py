from app.execution_plane.tifs import TIFPolicyEngine
from app.execution_plane.enums import OrderType, TIFClass

def test_tif_policy():
    allowed_limit = TIFPolicyEngine.get_allowed_tifs(OrderType.LIMIT, is_post_only=False)
    assert TIFClass.GTC in allowed_limit

    allowed_market = TIFPolicyEngine.get_allowed_tifs(OrderType.MARKET, is_post_only=False)
    assert TIFClass.IOC in allowed_market
    assert TIFClass.GTC not in allowed_market

    allowed_post = TIFPolicyEngine.get_allowed_tifs(OrderType.LIMIT, is_post_only=True)
    assert TIFClass.GTX in allowed_post

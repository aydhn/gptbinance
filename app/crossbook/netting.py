"""
netting.py
"""
import uuid
from typing import Dict
from app.crossbook.base import NetExposureEvaluatorBase
from app.crossbook.models import (
    ExposureGraphModel,
    NetExposureSnapshot,
    NetAssetExposure,
    DirectionalExposure,
)
from app.crossbook.enums import ExposureClass, HedgeQuality


class NetExposureEvaluator(NetExposureEvaluatorBase):
    def evaluate(self, graph: ExposureGraphModel) -> NetExposureSnapshot:
        assets_exposure: Dict[str, NetAssetExposure] = {}
        total_gross = 0.0
        total_net = 0.0

        for asset, node in graph.nodes.items():
            long_notional = sum(p.notional for p in node.positions if p.quantity > 0)
            short_notional = sum(
                abs(p.notional) for p in node.positions if p.quantity < 0
            )

            net_notional = long_notional - short_notional

            total_gross += long_notional + short_notional
            total_net += abs(net_notional)

            # Determine exposure class
            exp_class = ExposureClass.DIRECTIONAL_LONG
            if net_notional < 0:
                exp_class = ExposureClass.DIRECTIONAL_SHORT
            elif (
                long_notional > 0
                and short_notional > 0
                and abs(net_notional) < (long_notional * 0.1)
            ):
                exp_class = ExposureClass.NEUTRAL_HEDGED

            # Mock hedge quality
            hq = HedgeQuality.POOR
            if exp_class == ExposureClass.NEUTRAL_HEDGED:
                hq = HedgeQuality.ACCEPTABLE

            assets_exposure[asset] = NetAssetExposure(
                asset=asset,
                directional=DirectionalExposure(
                    long_notional=long_notional,
                    short_notional=short_notional,
                    net_notional=net_notional,
                ),
                exposure_class=exp_class,
                hedge_quality=hq,
            )

        return NetExposureSnapshot(
            snapshot_id=str(uuid.uuid4()),
            timestamp=graph.timestamp,
            assets=assets_exposure,
            total_gross_notional=total_gross,
            total_net_notional=total_net,
        )

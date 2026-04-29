import logging
from typing import Any, Dict
from app.execution.live.models import ExecutionRequest, ExchangeAck, CancelRequest
from app.execution.live.exceptions import OrderSubmissionError, CancelError
from datetime import datetime

logger = logging.getLogger(__name__)


class BinanceTestnetExecutor:
    """Executes orders on Binance Testnet."""

    def __init__(self, rest_client: Any):
        self.rest_client = rest_client

    async def submit_order(self, request: ExecutionRequest) -> ExchangeAck:
        try:
            logger.info(f"Submitting order to testnet: {request.client_order_id}")
            # Mock submission
            # payload = self._build_payload(request)
            # response = await self.rest_client.post("/api/v3/order/test" if dry_run else "/api/v3/order", data=payload)
            response = {
                "clientOrderId": request.client_order_id,
                "orderId": "mock_exchange_id_123",
                "status": "NEW",
            }
            return ExchangeAck(
                client_order_id=response["clientOrderId"],
                exchange_order_id=str(response["orderId"]),
                raw_response=response,
            )
        except Exception as e:
            logger.error(f"Failed to submit order {request.client_order_id}: {e}")
            raise OrderSubmissionError(str(e))

    async def cancel_order(self, request: CancelRequest) -> Dict[str, Any]:
        try:
            logger.info(f"Cancelling order on testnet: {request.client_order_id}")
            # Mock cancel
            response = {"clientOrderId": request.client_order_id, "status": "CANCELED"}
            return response
        except Exception as e:
            logger.error(f"Failed to cancel order {request.client_order_id}: {e}")
            raise CancelError(str(e))

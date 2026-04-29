from typing import Optional
import logging
from typing import Dict, Any, List
from datetime import datetime
from app.execution.live.base import ReconciliationEngineBase, OrderStateStoreBase
from app.execution.live.models import ReconciliationReport, OrderStateSnapshot
from app.execution.live.enums import ReconciliationStatus, OrderLifecycleStatus

logger = logging.getLogger(__name__)


class ReconciliationEngine(ReconciliationEngineBase):
    def __init__(self, state_store: OrderStateStoreBase, binance_client: Any):
        self.state_store = state_store
        self.binance_client = binance_client

    async def run_reconciliation(self) -> ReconciliationReport:
        logger.info("Starting reconciliation process")
        report = ReconciliationReport(status=ReconciliationStatus.MATCH)

        # 1. Get local open orders
        local_open_orders = self.state_store.get_all_open_orders()

        # 2. Get exchange open orders
        try:
            # Placeholder for actual REST call
            exchange_open_orders_raw = await self.fetch_exchange_open_orders()
            exchange_orders_map = {
                str(o["clientOrderId"]): o for o in exchange_open_orders_raw
            }
        except Exception as e:
            logger.error(f"Failed to fetch exchange open orders: {e}")
            report.status = ReconciliationStatus.UNRESOLVED_ANOMALY
            report.unresolved_anomalies.append("Failed to fetch exchange open orders")
            return report

        # 3. Compare
        for local_order in local_open_orders:
            client_id = local_order.client_order_id
            if client_id not in exchange_orders_map:
                # Local order thinks it's open, but exchange doesn't have it.
                # Could be filled, cancelled, or never successfully submitted.
                report.drift_items.append(f"Order {client_id} missing on exchange")
                # Attempt to repair by fetching specific order status
                try:
                    repaired_status = await self.check_and_repair_order(local_order)
                    if repaired_status:
                        report.repaired_items.append(
                            f"Repaired {client_id} to status {repaired_status}"
                        )
                    else:
                        report.unresolved_anomalies.append(
                            f"Could not resolve status for {client_id}"
                        )
                except Exception as e:
                    report.unresolved_anomalies.append(
                        f"Error repairing {client_id}: {e}"
                    )

        if report.drift_items:
            report.status = ReconciliationStatus.DRIFT_DETECTED
            if len(report.repaired_items) == len(report.drift_items):
                report.status = ReconciliationStatus.REPAIRED

        return report

    async def fetch_exchange_open_orders(self) -> List[Dict[str, Any]]:
        # Mock implementation
        return []

    async def check_and_repair_order(
        self, order: OrderStateSnapshot
    ) -> Optional[OrderLifecycleStatus]:
        # Mock implementation
        # Fetch specific order from REST and update state_store
        # e.g., if filled, update store and return FILLED
        return None

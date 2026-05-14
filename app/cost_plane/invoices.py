from app.cost_plane.models import VendorInvoiceRecord
import uuid

class InvoiceManager:
    def __init__(self):
        self._records: list[VendorInvoiceRecord] = []

    def record_invoice(self, vendor_name: str, total_amount: float, currency: str, reconciled: bool, freshness_warnings: list[str] = None) -> VendorInvoiceRecord:
        record = VendorInvoiceRecord(
            invoice_id=str(uuid.uuid4()),
            vendor_name=vendor_name,
            total_amount=total_amount,
            currency=currency,
            reconciled=reconciled,
            freshness_warnings=freshness_warnings or []
        )
        self._records.append(record)
        return record

    def list_records(self) -> list[VendorInvoiceRecord]:
        return self._records

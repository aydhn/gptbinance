from app.cost_plane.invoices import InvoiceManager

def test_invoices():
    manager = InvoiceManager()
    record = manager.record_invoice("AWS", 1500.0, "USD", True)
    assert record.reconciled

# 083 User-Data Stream ve Reconciliation Politikası

## User-Data Stream
REST API tek başına yeterince hızlı değildir. WebSocket üzerinden gelen `executionReport` mesajları `ExecutionParser` ile domain event'lerine dönüştürülüp lokal state güncellenir.

## Reconciliation (Uzlaşma)
Borsa durumu ile lokal durum arasındaki farklar (drift), `ReconciliationEngine` ile tespit edilir.
Ağ bağlantısı kopması veya kaçan bir ACK durumunda, açık emirlerin borsa ile senkronize edilmesi sağlanır.

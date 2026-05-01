# Retry, Backoff, Idempotency ve Failure Escalation Politikası

## Idempotency ve Duplicate-Run
Bir iş aynı input ve aynı zaman penceresi için ikinci defa tetiklenmemelidir.
`idempotency.py` içinde yer alan `generate_run_key(job_id, inputs, scheduled_time)` kullanılarak hash üretilir.
Eğer bu anahtarla çalışan veya başarılı olan bir job varsa tekrarlanmaz, böylece "replay" hatalarının (örn. iki defa bakiye hesaplama) önüne geçilir.

## Retry ve Backoff
`RetryPolicy` tarafından yönetilir.
- Sadece `retryable_exceptions` listesindeki hatalarda retry yapılır.
- Sonsuz retry yasaktır (`max_attempts` ile sınırlandırılır).
- Exponential backoff seçeneği aktifleştirilirse cooldown süresi katlanarak artar.

## Failure Escalation (Hata Tırmandırma)
Bir job tüm attempt haklarını bitirdiğinde (`RetryVerdict.EXHAUSTED`), durum kalıcı olarak `FAILED` işaretlenir ve `TelegramNotifier` üzerinden "RETRY EXHAUSTED" formatında acil bir uyarı atılır.

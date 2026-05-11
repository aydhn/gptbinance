# Compliance Integrity, Readiness, Activation ve Policy Release Entegrasyonu

## Compliance Integrity Domain
Compliance, Readiness Board ve Reliability sistemlerinde bağımsız bir domain (`compliance_integrity`) olarak ele alınır.

## Activation ve Release Blokları
Kritik uyumluluk açıklarına sahip, süresi dolmuş sertifikasyonları olan veya aşırı uyumluluk borcu (exception burden/debt) bulunan sistemlerin yeni bir release alması veya canlıya (live) çıkması (activation) engellenir (block/caution semantics).

## Policy ve Control Plane Entegrasyonu
Policy Plane tarafından üretilen yükümlülükler (obligations), Compliance Plane'deki gereksinimlerle (requirements) eşleşir. Control Plane'deki onay ve işlem makbuzları (receipts), Compliance Plane için otomatik kanıt (evidence) olarak toplanır.

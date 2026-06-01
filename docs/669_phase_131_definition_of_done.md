# Phase 131 Definition of Done

## Tamamlananlar
- Unified drift plane framework kuruldu.
- Canonical drift registry ve typed baseline/signal/regression/recurrence/restriction modelleri eklendi.
- Baseline integrity, threshold breach, guardrail deviation, restriction reimposition, scar reactivation ve re-normalization semantikleri oluşturuldu.
- Replay / paper / probation / live drift equivalence analitiği ve trusted drift verdict engine yapısı kuruldu.
- CLI üzerinden drifts, baselines, signals vb. yönetimi eklendi.
- Gerekli tüm testler yazıldı ve doğrulandı.
- Dokümantasyon (`docs/`) eklendi.

## Bilerek Ertelenenler
- Drift verilerinin görsel dashboard'lar üzerinde sunumu (bu faz, metric dashboard fazı değildir).
- Observability alert konfigürasyonlarının tam detaylı entegrasyonu (temel bağlam sağlandı).
- Policy motorunun çok gelişmiş kurallarının tamamı (çekirdek logic sağlandı).

## Sonraki Faza Geçiş Şartları
- Tüm testlerin başarılı olması.
- Hiçbir "hidden drift", "threshold gaming" veya "recurrence theater" zafiyetine izin verilmemesi.
- CLI komutlarının eksiksiz çalışması.

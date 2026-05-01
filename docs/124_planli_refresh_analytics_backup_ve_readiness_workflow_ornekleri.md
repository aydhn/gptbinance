# Planlı Refresh, Analytics, Backup ve Readiness Workflow Örnekleri

Bu fazda tanımlanan örnek workflow'lar, sistemin gelecekteki otomasyon omurgasını oluşturur:

## 1. Nightly Research Refresh Workflow
`nightly_research_refresh_workflow`
Gece yarısı tetiklenir. `data_refresh` -> `feature_refresh` -> `analytics_summary` adımlarını sırayla (dependency kurallarına uyarak) çalıştırır. Biri çökerse zincir kopar.

## 2. Morning Readiness Workflow
`morning_readiness_workflow`
Sabah trading seansından önce ops readiness durumlarını (API anahtarları, balance) check eder. Hata bulursa telegram üzerinden uyarı gönderir.

## 3. Post-Incident Diagnostics Workflow
`post_incident_diagnostics_workflow`
Bir olay (incident) yaşandıktan sonra sistemin health ve drift check gibi durumlarını analiz etmek için manuel veya webhook tabanlı tetiklenebilir.

## Neden Bu Workflow'lar Seçildi?
Bu akışlar, bir trading sisteminin manuel denetimlerden kurtulup, kendi kendine tutarlılık sağlayan (ama gate'li) bir altyapıya kavuşmasını sağladığı için örnek olarak tanımlanmıştır.

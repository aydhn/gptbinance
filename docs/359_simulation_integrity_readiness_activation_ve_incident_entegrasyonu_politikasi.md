# Simulation Integrity, Readiness, Activation ve Incident Entegrasyonu Politikası

## Simulation Integrity Domain
Readiness ve Reliability domainleri arasına `simulation_integrity` eklenmiştir. Bir stratejinin live ortama terfi edebilmesi için sağlam simülasyon kanıtlarına ihtiyacı vardır.

## Readiness Blockers & Activation Evidence
- **Missing Assumptions:** Manifestosu olmayan simülasyonlar aktivasyon sürecini bloke eder.
- **OOS Contamination:** OOS verisinde sızıntı tespit edilmesi kritik bir engelleyicidir.
- Aktivasyon aşamasında simülasyon kanıt sınıfı doğrulanmalıdır.

## Incidents & Alerts
Kritik lookahead şüphesi, gizli varsayım tespiti veya OOS kirlenmesi olay (incident) olarak kaydedilir ve alert (uyarı) üretir.

## Evidence Graph & Review Packs
Simülasyon tanımları, koşuları ve varsayım manifestoları evidence graph'ın bir parçasıdır. Walk-forward ve OOS review paketleri incelemeler (reviews) için kullanılır.

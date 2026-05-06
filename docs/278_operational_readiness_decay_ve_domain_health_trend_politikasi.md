# Operational Readiness Decay ve Domain Health Trend Politikası

## Readiness Decay (Hazırlık Çürümesi)
Sistem "incident-free" (olaysız) olsa dahi operasyonel sağlığı zamanla bozulabilir:
- **Stale Evidence:** Board onayları ve kanıtlar çok eskiyse.
- **Unresolved Debt:** Remediation borçları (CAPA) uzun süre açık kalırsa.
- **Recurring Incidents:** Aynı tip problemler sürekli tekrar ediyorsa.

Readiness Decay Engine bu unsurları birleştirerek her domain için bir "Decay Severity Score" hesaplar ve bunu scorecard'lara girdi olarak verir.

## Trend Analizi
Geçmiş scorecard'lara bakılarak "Improving", "Stable", "Degrading", "Volatile" gibi trendler belirlenir. Bu trendler, günlük/haftalık operasyonel review ritüellerine dahil edilir.

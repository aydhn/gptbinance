# Baseline Scope, Drift Signalleri, Metric Erosion, Threshold, Guardrail, Control ve Authority Drift Politikası

Bu politika, sistemin temel işletim durumundan (baseline) sapmalarını ve bu sapmaların farklı boyutlarını tanımlar.

*   **Baselines:** Sistemin beklenen normal durumunu (scope) net bir şekilde tanımlar.
*   **Signals:** Beklenen durumdan sapmanın erken uyarılarıdır. Her signal bir breach (ihlal) anlamına gelmez, ancak incelenmelidir.
*   **Metric Erosion:** Metriklerdeki yavaş (progressive) veya kademeli (stepwise) aşınmaları tanımlar.
*   **Thresholds:** Kesin sınırları belirler. Aşılması durumunda breach (ihlal) oluşur ve aksiyon (restriction) gerektirir.
*   **Guardrails:** Sistemin sınırları aşmasını engelleyen kontrollerdir. Bunların zayıflaması veya sessizce kaldırılması ciddi bir risktir.
*   **Control Drift:** Yönetişim ve kontrol mekanizmalarındaki sapmaları ifade eder.
*   **Authority Drift:** Yetki sınırlarının yavaş yavaş genişlemesi veya belirsizleşmesidir.

**Temel Kural:** Signal != Breach != Justified Restriction. Her aşama ayrı değerlendirilmeli ve kanıtlarla desteklenmelidir.

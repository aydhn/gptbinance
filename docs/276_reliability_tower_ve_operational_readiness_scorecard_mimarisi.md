# Phase 54 - Reliability Tower ve Operational Readiness Scorecard Mimarisi

Bu doküman, Phase 54 kapsamında kurulan "Reliability Tower" (Güvenilirlik Kulesi) sisteminin temel mimarisini açıklamaktadır.

## Amaç
Teknik olarak çalışan bir sistemin operasyonel olarak ne kadar sağlıklı olduğunu (stale evidence, unresolved debt, recurring incidents bağlamında) ölçmek ve disiplin altına almaktır.

## Mimari Bileşenler
1. **Reliability Domains:** market_truth, shadow_truthfulness, lifecycle_health, incident_operations, remediation_closure vb. alanlarda sağlığı böler.
2. **SLO & Error Budget:** Her domain için ölçülebilir hedefler ve bu hedeflerin ne kadar aşılabileceğini belirten bütçeler.
3. **Burn Rate & Decay:** Bütçenin ne kadar hızlı tüketildiği (fast burn vs slow burn) ve geçmiş kanıtların/eski borçların operasyonel güveni nasıl çürüttüğü (readiness decay).
4. **Health Scorecards:** Tüm bu girdilerin birleşip her domain için (Healthy, Caution, Degraded, Blocked, Review_Required) gibi verdict'ler ürettiği kartlar.
5. **Freeze & Hold Recommendations:** Scorecard'ların ürettiği, operasyonu durdurmaya yönelik "tavsiye" niteliğindeki çıktılar. (Asla otomatik zorlama değil).

## Prensipler
- Neden sihirli skor yok? Çünkü sistemin bir yeri çok kötüyken diğer yeri iyi olabilir. Skor ortalaması yanıltıcıdır; domain-bazlı kısıtlamalar (blockers) gerçeği söyler.
- Neden otomatik freeze yok? Çünkü güvenilirlik metrikleri tavsiye verir, insan veya release board (Human-in-the-Loop) bu bağlamı değerlendirerek nihai kararı verir.

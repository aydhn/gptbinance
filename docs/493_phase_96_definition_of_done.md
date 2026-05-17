# Phase 96 Definition of Done

**Bu Fazın Tamamlanma Ölçütleri:**
- Change Plane framework'ü ve Canonical Change Registry çalışır durumda.
- Request, approval, window, execution, verification ayrımı yapılmış, modelleri oluşturulmuştur.
- Equivalence, divergence, risk, collision, exceptions ve debt mekanizmaları mevcuttur.
- Release, Activation, Policy_Kernel gibi dış domainler Change Plane gereksinimleriyle güncellenmiştir.
- CLI üzerinden change plane metadata raporlanabilmektedir.
- Güçlü bir test süiti vardır.

**Bilerek Ertelenenler:**
- Derin entegrasyonlu CLI raporlamasının UX geliştirmeleri (sadece raw json veya text basılabilir).
- Detaylı event tracking veri tabanı yapısı (şu an Pydantic modellerine dayanıyor).

**Sonraki Faza Geçiş Şartları:**
- Tüm entegrasyonlar syntax error vermemeli.
- Testler %100 passing olmalı.
- Hidden hotfix gibi governance karşıtı yollar sistemde tamamen bloklanmış olmalı.

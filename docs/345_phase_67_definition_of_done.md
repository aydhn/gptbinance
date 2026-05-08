# Phase 67: Definition of Done

## Tamamlanma Ölçütleri
- [x] Performance Plane base modelleri ve exception tipleri yaratıldı.
- [x] Canonical benchmark registry ve window semantics kuruldu.
- [x] Attribution tree (Selection, Timing, Allocation, Execution, vb.) logic'i eklendi.
- [x] Drag ve Opportunity surface tracking (caveatlerle beraber) aktive edildi.
- [x] Replay vs Live Equivalence ve Trust Verdict hesaplayıcıları yazıldı.
- [x] CLI komutları (örn. `--show-attribution-tree`, `--show-opportunity-surfaces`) eklendi.
- [x] Core Position/Execution/Allocation/Risk plane'lerden performance plane'e data export pipeline'ı kuruldu.
- [x] Incident/Observability/Readiness entegrasyonları yapıldı.
- [x] Tests çalıştırıldı ve pass oldu.

## Bilinçli Ertelenenler
- Complex orderbook impact / tam kapsamlı "unresolved counterfactual" hesaplamaları (simülasyon derinliği gerektirir).
- ML-driven attribution prediction.
- Sadece deterministic pipeline kuruldu; attribution'daki "timing vs signal" ayrımındaki fuzzy mantık ileriki ML tuning'e bırakıldı.

## Sonraki Faza Geçiş Şartları (Phase 68 Önerisi)
- **Phase 68:** Tactical Replay-Runtime Parity Loop ve Automated Drift Remediation Katmanı.
- *Amaç:* Performance Equivalence reporlarının "Material Divergence" gösterdiği durumlarda otomatik olarak Replay Engine'in assumptions (slippage, fee vs) parametrelerini tune etmesi ve Live ile uyumlanmasını sağlayan geri besleme döngüsü.

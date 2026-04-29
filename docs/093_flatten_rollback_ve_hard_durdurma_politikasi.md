# Phase 17: Flatten, Rollback ve Hard Halt Politikası

Live session tehlikeye girdiğinde farklı seviyede acil durum prosedürleri vardır:

## 1. Flatten
- **Ne yapar?** Açık order'ları iptal eder, var olan pozisyonları piyasa fiyatından zıt işlemle kapatır.
- **Ne zaman kullanılır?** Daily loss cap aşıldığında veya manuel CLI (`--flatten-live-session`) çağrıldığında.
- **Sonuç:** Session durumu HALTED olur, yeni intent dondurulur, portföy sıfırlanır.

## 2. Rollback
- **Ne yapar?** Rollout'u tamamen geri alır. Mainnet execution'ı `disarm` eder. Opsiyonel olarak `HARD` seviyesinde ise flatten tetikler.
- **Ne zaman kullanılır?** Anormal execution fırtınası veya manuel CLI (`--rollback-live-session`).
- **Sonuç:** Mainnet kapısı kalıcı olarak kilitlenir. Güvenli geri dönüş garantilenir.

## 3. Hard Halt (Kill Switch)
- **Ne yapar?** Sürecin en alt seviyede durmasıdır. Ops Control Plane'in global kill switch'i ile tetiklenir.
- **Sonuç:** Start gate'ler geçilemez, devam eden session derhal HALTED durumuna geçer.

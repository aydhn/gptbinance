# Phase 13: Rejim ve Volatiliteye Duyarlı Risk Ayarlama Politikası

## Rejim Ayarlamaları
Sistem, `RegimeRepository` üzerinden alınan pazar bağlamı (context) ile stratejileri değerlendirirken aynı zamanda riski de ölçekler.
- **Normal Rejim:** Beklenen pazar koşulları. Çarpan: `1.0`
- **Caution Rejimi:** Pazar yönü belirsiz veya uyumsuz. Çarpan: `0.5` (Daha küçük pozisyonlar)
- **Restrictive Rejim:** Yüksek gürültü, kalitesiz veriler. Çarpan: `0.25` veya tam veto.

## Volatilite Ayarlamaları
Mevcut volatilite (Örn: ATR) ile geçmiş volatilite karşılaştırılarak ani oynamalara (volatility expansion) karşı pozisyon boyutu küçültülür.
- Eğer mevcut ATR, geçmişin 2 katından fazlaysa, sistem pozisyon büyüklüğünü yarıya indirir.
- Amaç: Volatilitesi artan sembolde aynı büyüklükte pozisyon alarak hesap riskini (Capital at Risk) gereksiz yere büyütmemek.

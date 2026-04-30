# Phase 18: Sleeve Bütçeleri, Concentration ve Sermaye Disiplini

Sermaye dağıtımı, fırsat kalitesinin yanında sistemin hayatta kalma kapasitesini merkeze alır. Tüm sermayeyi tek yöne, tek stratejiye ya da tek bir enstrümana yığmamak esastır.

## Policy Kuralları
- **Symbol Limits:** Hiçbir sembol (örn. BTCUSDT) toplam sermayenin %20/25'inden fazlasını işgal edemez (`max_symbol_weight`).
- **Strategy Sleeve Limits:** Aynı strateji ailesi (örn. "Core_Trend") portföyün %50'sinden fazlasına hakim olamaz.
- **Reserve Cash:** Her zaman belirli bir nakit oranı (`reserve_cash_ratio`, default %20) korunmalıdır. Gelen allocation talebi eğer nakdi bu sınırın altına indirirse, reddedilir veya küçültülür.

## Concentration (Yoğunlaşma)
Concentration modülü, symbol ve strategy dağılımlarını sürekli denetler ve "NORMAL", "CAUTION", "BREACH" seviyeleri üretir. CAUTION seviyesinde allocator yeni intentleri bu sleeve'ler için reddetmeye başlar.

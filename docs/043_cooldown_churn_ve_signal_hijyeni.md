# Phase 07: Cooldown, Churn ve Signal Hijyeni

## Gereksiz Sinyal Spam'i Neden Tehlikelidir?
Her barda aynı sinyalin tekrar tekrar üretilmesi, yön değişim spam'i veya aynı stratejinin anlamsız churn (hızlı gir-çık) üretmesi sistemin performansını ve okunabilirliğini bozar. Gereksiz işlem (overtrading), maliyetleri (fee) artırır ve sermayeyi eritir.

## Cooldown Neden Gereklidir?
Belirli bir sinyal veya işlem niyetinin ardından stratejinin bir süre beklemesini (dinlenmesini) sağlar.
- Sembol bazlı
- Strateji bazlı
- Yön bazlı (Long/Short) uygulanabilir.

## Churn Azaltma Politikası
Peş peşe aynı yönde veya hızlı zıt yönde sinyal üretimini engelleyen guard'lar içerir. Bir stratejinin veya sembolün aşırı aktif (hyperactive) hale gelip sistemi boğmasına engel olur.

## Future Live Trading Güvenliği İle İlişkisi
Canlı işlemlerde (live execution), churn ve spam doğrudan sermaye kaybına yol açar. Cooldown mekanizması, strateji katmanından itibaren sıkı bir "signal hijyeni" uygulayarak ilerideki "Live Guard" kontrollerinin yükünü hafifletir ve sistem kararlılığını korur.

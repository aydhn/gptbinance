# 193. Liquidity, Spread, Turnover Intelligence ve Profile-Aware Eligibility Politikası

Sembollerin trade edilebilirliği yalnızca veri yapısıyla değil, piyasa kalitesiyle de ölçülür.

## Liquidity, Spread ve Turnover Ölçüleri
Sistem, kaba (coarse) 24 saatlik piyasa verilerini kullanarak:
- **Liquidity**: Hacim (volume) ve değer (quote volume) metriklerini değerlendirerek sembolleri sınıflandırır (Yüksek, Orta, Düşük, Çok Düşük).
- **Spread**: Alış (Bid) ve Satış (Ask) farkını hesaplayarak spread genişliğini sınıflandırır (Dar, Normal, Geniş, Çok Geniş).
- **Turnover**: İşlem sayısını ve aktiviteyi ölçerek düşük turnover riskini tespit eder.

## Profile-Aware Symbol Eligibility
Sembol uygunluğu, çalışma profiline (ProfileContext) göre değişiklik gösterir:
- **paper_default**: Daha esnek kurallara sahiptir, daha fazla sembolü kabul edebilir.
- **testnet_exec**: Yalnızca testnet ortamında desteklenen sembolleri kabul eder.
- **canary_live_caution**: Çok katı kurallara sahiptir. Sadece yüksek likiditeye, dar spreade ve güncel metadata'ya sahip semboller (TradabilityClass: PREMIUM veya STANDARD) kabul edilir. Düşük likidite veya geniş spread doğrudan engelleme (Block) sebebi olabilir.

## Low-Liquidity Riskleri
Düşük likidite veya geniş spread tespit edilen semboller, portföy ve strateji katmanlarında kısıtlamalara (daha düşük alokasyon tavanı, artırılmış slippage beklentisi) tabi tutulur veya doğrudan reddedilir.

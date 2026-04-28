# Rejim Motoru Mimarisi

Rejim (Context) motoru, sistemde stratejilerin hangi piyasa ortamında çalıştığını anlamalarını sağlayan kritik bir katmandır.

## Neden Ayrı Bir Katman?
Stratejiler, kendilerine verilen feature'lar üzerinden doğrudan sinyal üretebilir. Ancak aynı feature değerleri farklı bağlamlarda (trend, yatay piyasa, yüksek volatilite) farklı anlamlar taşır. Rejim katmanı, bu bağlamı (context) soyutlayarak strateji motorunun kararlarını filtrelemesini, ağırlıklandırmasını veya reddetmesini sağlar.

## Zincir: Feature -> Regime -> Strategy Suitability
1. **Feature Engine**: Ham piyasa verilerinden anlamlı öznitelikler (SMA, RSI, ATR) üretir.
2. **Regime Engine**: Bu feature'ları kullanarak piyasanın mevcut durumunu sınıflandırır (Trend, Volatilite, Mean-Reversion, Structure).
3. **Strategy Suitability**: Sınıflandırılmış bu rejimlerin, hangi strateji aileleri (Trend Following, Mean Reversion vb.) için uygun olduğunu puanlar ve öneriler üretir.

Bu yapı sayesinde doğrudan "Al/Sat" sinyali üretilmez, ancak stratejilere "Şu an trend takibi yapmak için uygun bir ortamdayız" mesajı iletilir.

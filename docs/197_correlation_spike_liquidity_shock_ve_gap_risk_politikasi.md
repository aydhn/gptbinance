# Correlation Spike, Liquidity Shock ve Gap Risk Politikası

## Stressed Correlation
Normal zamanlarda ilişkisiz hareket eden varlıklar, piyasa şokları sırasında (örn. ani panik satışları) aynı anda düşme eğilimi göstererek korelasyonlarını 1.0'e yaklaştırır. Bu "diversification erosion" (çeşitlendirme erozyonu) durumunu saptamak için sistem, korelasyon katsayılarını yapay olarak artırarak portföyün toplam riskini hesaplar.

## Liquidity Collapse & Spread Widening
Piyasa derinliği azaldığında:
- Slipaj (slippage) varsayılanın ötesine sıçrar.
- Alım-satım spread'i dramatik şekilde genişler (spread widening).
Sistem, emir büyüklükleri ve tarihsel likidite profillerini göz önüne alarak, "liquidity shock" altındaki execution bozulma maliyetini (execution deterioration cost) hesaplar.

## Gap Risk
Piyasa açılışlarında veya çok ani haber akışlarında fiyat kademeleri atlayarak değişebilir. Bu durumda stop-loss emirleri hedeflenen fiyattan çalışmayabilir. Bu senaryolar (gap down/up), doğrudan fiyat seviyesine doğrudan şok çarpanı uygulanarak simüle edilir.

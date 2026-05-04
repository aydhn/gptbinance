# 206 Cross Book Exposure Ve Teminat Governance Mimarisi

Bu belge, Spot, Margin ve Futures defterlerindeki pozisyonların nasıl birleşik bir grafikte ele alındığını ve neden otomatik netleştirme yapılmadan yalnızca görünürlük sağlandığını açıklar.

## Spot/Margin/Futures Birleşik Exposure Yaklaşımı
Aynı underlying asset (örneğin BTC), spot tarafta owned, margin tarafta borrowed ve futures tarafta directional exposure olarak bulunabilir. Tüm bu parçalar `UnifiedExposureNode` olarak tek grafikte birleşir.

## Neden Auto-Hedging Yapılmıyor?
Otomatik hedging risklidir çünkü execution maliyeti ve mode-conflict (cross vs isolated) problemleri yaratır. Sistem yalnızca dürüst maruziyet görünürlüğü sağlar.

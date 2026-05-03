# Event-Aware Entegrasyon Politikası

## Strategy Entegrasyonu
Stratejiler, `event_sensitivity` parametresiyle (yüksek/düşük vb.) olaylardan nasıl etkilendiklerini beyan ederler. Olay pencerelerinde hassas stratejiler geçici olarak askıya alınabilir.

## Portfolio Entegrasyonu
Event Risk Overlay "REDUCE_ONLY" veya "BLOCK" kararı verirse, tahsis motoru (portfolio allocator) bütçeyi (budget) kısabilir veya sıfırlayabilir.

## Execution Entegrasyonu
Canlı (live) veya kağıt (paper) ticarette emrin geçirilmesinden hemen önce EventGate kararı kontrol edilir. Eğer olay engeli (BLOCK) varsa, emir borsaya iletilmez.

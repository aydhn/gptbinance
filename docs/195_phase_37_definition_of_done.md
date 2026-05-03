# Phase 37: Definition of Done

Bu fazın tamamlanması için aşağıdaki kriterlerin karşılanması gerekmektedir:

## Tamamlanan Özellikler
1. **Instrument Registry**: Sembollerin, ürün tipi farkındalığıyla normalize edilmesi ve saklanması.
2. **Exchange Filters Validation**: Tick size, step size ve min notional filtrelerinin modellerinin oluşturulması ve doğrulama mantığının kurulması.
3. **Liquidity/Spread/Turnover Intelligence**: Kaba piyasa verileri kullanılarak likidite, spread ve turnover sınıflandırmalarının (severity) yapılması.
4. **Tradability ve Profile-Aware Eligibility**: Sembollerin, profillere özgü (örn. canary_live_caution vs paper_default) uygunluk kararlarının üretilmesi.
5. **Lifecycle Management**: Listing, delisting ve statü değişikliklerinin yakalanıp olaylaştırılması.
6. **Snapshot ve Diff**: Universe snapshot'larının üretilmesi ve geçmişe yönelik farklılık (diff) analizi.
7. **Downstream Integration Stub'ları**: Etki analizlerinin temel modellemesinin yapılması.
8. **CLI Entegrasyonu Planı**: CLI komutlarının mantığının yazılması (eklenmesi için `main.py` güncelleme önerisi).

## Kesinlikle Yapılmayanlar (Bilinçli Ertelenenler)
- **HTML Scraping**: Borsa verileri dışında hiçbir kaynaktan veri alınmamıştır.
- **Yüksek Frekanslı Microstructure**: Emir defteri bazlı milisaniyelik spread/likidite analizi bu fazın kapsamı dışındadır.
- **Otomatik Hype-Chasing**: Haberlere veya sosyal medya hype'ına dayalı sembol ekleme mekanizmaları dahil edilmemiştir.
- **Sessiz Sembol Ekleme**: Kayıt dışı veya audit edilmemiş universe değişiklikleri engellenmiştir.

## Sonraki Faza Geçiş Şartları
Bu faz, sistemin trade ettiği enstrümanları tanımlamasını, filtrelemesini ve kalitesini ölçmesini sağlar. Bir sonraki faza (Phase 38) geçmek için, registry'nin düzgün yüklenebildiği ve snapshot'ların profile göre doğru symbol listesini üretebildiği testlerle kanıtlanmış olmalıdır.

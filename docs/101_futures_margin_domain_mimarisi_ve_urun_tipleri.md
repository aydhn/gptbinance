# Futures ve Margin Domain Mimarisi ve Ürün Tipleri

Bu belge, sistemin geleneksel Spot akışını bozmadan nasıl Futures ve Margin ürünlerine genişlediğini anlatır.

## Motivasyon
Spot ticaret basittir: alırsın, satarsın, elindeki kadar satabilirsin. Ancak Futures ve Margin ticareti kısa pozisyonlar, kaldıraç (leverage), teminatlandırma (liquidation), ve periyodik maliyetler (funding, borrow interest) getirir. Bu karmaşıklığı Spot kodunun içine "if futures:" şeklinde gömmek sistemi kırılgan ve tehlikeli hale getirir.

## Çözüm: Product Domain Layer
Sistem artık `app/products/` altında merkezi bir kayıt defteri (`ProductRegistry`) kullanır.
Her ürün tipi (`SPOT`, `MARGIN`, `FUTURES_USDM`, vb.) bir `ProductDescriptor` ile tanımlanır.

### Descriptor Neleri Belirler?
- **Capabilities**: Short yapılabilir mi? Maksimum kaldıraç kaç? Hangi margin (Cross/Isolated) ve pozisyon modları (One-way/Hedge) destekleniyor?
- **Readiness**: Ürün canlı yayına hazır mı (`LIVE`), yoksa güvenlik amacıyla sadece `TESTNET_ONLY` veya `PAPER_ONLY` mi?
- **Risk & Costs**: Liquidation ve funding/borrow maliyetleri var mı? Reduce-only zorunlulukları aktif mi?

### Uygulama (Derivatives Base)
`app/execution/derivatives/` paketi bu karmaşıklığı yönetir:
- Leverage Manager ve Margin Mode Manager: Bu ayarların sadece izin verilen sınırlarda (örn. max 5x) değiştirilmesini sağlar.
- Position Mode Manager: Hedge ve One-Way modlarını ayırır.

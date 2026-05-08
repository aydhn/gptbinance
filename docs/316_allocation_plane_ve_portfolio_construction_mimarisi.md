# Allocation Plane & Portfolio Construction Mimarisi

Allocation Plane, sistemde üretilen raw strateji sinyallerinin portföye girmeye layık "tahsis adayları" haline gelmesini yönetir.

Sinyaller, `sleeves` (bütçe paketleri) altında değerlendirilir.
Doğrudan `size`'a dönüşmez; arbitrasyon, nettign, diversification ve constraint'lerden geçer.

## Akış
1. Signals -> Candidates
2. Sleeves -> Budgets
3. Arbitration -> Sizing -> Netting
4. Allocation Intents -> Allocation Manifests

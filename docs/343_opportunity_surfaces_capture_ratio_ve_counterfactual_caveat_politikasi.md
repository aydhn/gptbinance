# Opportunity Surfaces, Capture Ratio ve Counterfactual Caveat Politikası

Bu sistem, kaçırılan fırsatları takip eder, ama onları cebimizde gibi göstermez.

## Sınıflar
- **CAPTURED:** Gerçekten realize edilen fırsat.
- **FOREGONE_SAME_ASSUMPTIONS:** Execution vb. olmasaydı *aynı faraziyelerle* alınabilecek kar.
- **RISK_BLOCKED:** Cooldown veya risk breach sebebiyle alınamayan emirlerin maliyeti.
- **CAPACITY_CLIPPED:** Portföy/Bütçe limiti yüzünden kırpılan emirlerin maliyeti.
- **UNRESOLVED_COUNTERFACTUAL:** Çok fazla faraziyeye (örn. orderbook tepkisi) dayalı hesaplar.

## Kurallar
- Missed-profit *asla* guaranteed profit değildir.
- Risk-blocked veya Capacity-clipped opportunity reportları her zaman `< 1.0` confidence score ve caveat array'i taşımalıdır.
- Capture Ratio: `Signal Intent -> Allocation Size -> Execution Fill -> Position Realized` adım adım zincir kopmalarını ölçer.

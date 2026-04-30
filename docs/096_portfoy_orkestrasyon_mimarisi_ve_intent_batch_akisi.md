# Phase 18: Portföy Orkestrasyon Mimarisi ve Intent Batch Akışı

## Mimari Yaklaşım

Risk motoru tekil sinyalleri değerlendirir ("Bu işlem güvenli mi?"). Ancak aynı anda birden çok risk-approved sinyal geldiğinde, sınırlı sermayenin hangilerine, hangi oranda ve nasıl dağıtılacağı portföy orkestrasyonunun işidir.

Portföy motoru (PortfolioEngine), bir `PortfolioIntentBatch` (risk-approved intents) alır, pazar korelasyonu, aşırı yoğunlaşma, sleeve kısıtları ve kullanılabilir bütçeyi değerlendirir.

## Akış

1. Strategy -> Raw Intents
2. Risk Engine -> Risk-Approved Intents (`PortfolioIntentBatch`)
3. Portfolio Engine:
   - Concentration ve Correlation güncellemesi
   - Overlap tespiti
   - Adayları skorla ve sırala (`OpportunityRank`)
   - Bütçe, sleeve limitleri (`allocator.py`) çerçevesinde onayla / küçült / ertele / reddet
4. Execution Engine -> Yalnızca Portfolio-Approved Kararları işler

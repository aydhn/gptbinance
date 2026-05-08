# Balance Equivalence, Divergence ve Account Scope Politikası

## Equivalence
Replay, paper, testnet ve live (runtime vs venue vs shadow) evrenlerinde equivalence testleri ile cashflow, balance ve collateral stateleri karşılaştırılır. Kısmi equivalence (partial) sınıfları tanımlanmıştır.

## Divergence
Mismatches (ör. runtime vs venue balance) gizlenmez; explicit divergence sınıfları üretilir.
Severity bazlı (low, medium, high, critical) sınıflandırma yapılarak downstream operasyonlarına block / caution eklenir.

## Account Scope
Her bir scope kendi aggregation'ında scope-safe'tir. Replay veya Paper evrenleriyle Live datası karıştırılamaz.

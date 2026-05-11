# Precedence, Conflict Resolution ve Temporal Scope Politikası

## Precedence (Öncelik)
* **Deny-Overrides**: Eğer herhangi bir kural `DENY` diyorsa, işlem engellenir.
* **Specific-over-General**: Belirli kurallar, genel kurallara göre önceliklidir.

## Conflicts (Çakışmalar)
* Duplicate veya dead kurallar `ConflictDetector` tarafından yakalanır.
* Çakışmalar sessizce çözülmez (silent conflict collapse yasaktır).

## Temporal Scope
* Kurallar `effective_from` ve `effective_until` ile zaman sınırına sahip olabilir.

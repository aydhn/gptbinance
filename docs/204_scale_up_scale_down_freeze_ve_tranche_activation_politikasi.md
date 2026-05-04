# Scale-up, Scale-down, Freeze ve Tranche Activation Politikası

## Ne Zaman Scale-up?
1. Escalation Engine "Pass" verirse (Evidence bundle temiz).
2. İnsan onayı (`governance_capital_committee`) alınırsa.

## Ne Zaman Scale-down / Reduce?
1. Loss budget aşıldığında (Hard breach).
2. Kötüleşen performans veya event-risk overlay'i "reduce" uyarısı verdiğinde.

## Ne Zaman Freeze?
1. Ledger reconciliation uyuşmazlığı tespit edildiğinde.
2. Açıklanamayan bakiye düşüşleri olduğunda.
3. Arka arkaya çok fazla kritik system hatası alındığında.

## Tranche Activation
Sermaye artırımları tier limiti içinde de dilimler (tranche) halinde yapılır. Böylece limiti tamamen kullanmak yerine 1/4'lük dilimlerle açılış yapılabilir.

## Transition Dry-Run
Bütün bu Scale-up/down işlemleri `--show-capital-transition-plan` komutu ile önceden simüle edilir (Dry-Run). Sistem hangi adımların uygulanması gerektiğini (pozisyon kapat, onaya sun vb.) liste olarak döner.

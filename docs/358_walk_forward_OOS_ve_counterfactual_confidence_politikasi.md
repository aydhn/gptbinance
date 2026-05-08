# Walk-Forward, OOS ve Counterfactual Confidence Politikası

## Walk-Forward Disiplini
Stratejilerin zaman içindeki dayanıklılığını ölçmek için walk-forward analizleri (rolling retrain windows) zorunludur. Fold'lar arası performans istikrarı değerlendirilir.

## OOS Hygiene (Out-of-Sample Hijyeni)
In-sample (train) verisi ile out-of-sample (test) verisi kesin olarak ayrılmalıdır. Sızıntı (leakage) veya geleceği görme (lookahead) şüphesi olan simülasyonlar güvenilir kabul edilmez.

## Counterfactual Confidence Classes
"Böyle olsaydı" senaryoları (hypothetical fills, risk-blocked alternatives) gerçeğe eşdeğer tutulamaz. Counterfactual sonuçlar High, Medium, Low veya Speculative olarak sınıflandırılmalıdır.

## Neden Hypothetical != Realized
Gerçekleşmemiş işlemlerin getiri potansiyeli, piyasa etkisini (market impact) barındırmaz. Bu nedenle hypothetical fırsatlar realized (gerçekleşmiş) karlar gibi sunulamaz.

# ML Katmanı Mimarisi ve Yardımcı Öğrenme Politikası

ML katmanı, mevcut kural tabanlı sistemin yerini almak için değil, ona "yardımcı kalite/seçim filtresi" sağlamak için kurulmuştur.
Bu mimari `dataset -> label -> split -> train -> calibrate -> register -> infer` zinciri etrafında şekillenir.

Mevcut strateji motoru (Strategy Engine), risk motoru (Risk Engine) ve portföy motoru (Portfolio Engine) ana karar vericiler olmaya devam eder.

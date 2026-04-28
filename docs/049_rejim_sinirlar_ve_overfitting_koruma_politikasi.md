# Rejim Sınırları ve Overfitting Koruma Politikası

Bu fazda karmaşık Makine Öğrenmesi (ML) veya Gizli Markov Modelleri (HMM) yerine tamamen kural tabanlı, yorumlanabilir rejim modelleri tercih edilmiştir.

## Neden Yorumlanabilir Modeller?
Erken aşamada kara kutu (black box) modeller kullanmak, overfitting riskini artırır ve sistemin neden başarısız olduğunu anlamayı imkansızlaştırır. Kural tabanlı modeller, "Neden güçlü trend dedik?" sorusuna "Çünkü hızlı SMA, yavaş SMA'nın üzerinde ve RSI 60'ın üstünde" gibi net cevaplar verebilir.

## Future ML Modellerine Geçiş
Sistemin kural tabanlı rejim ve strateji omurgası tam olarak test edilip onaylandıktan sonra, feature seti genişletilerek ve test veri seti kirlenmeden ayrıntılı ML modelleri eklenebilir.

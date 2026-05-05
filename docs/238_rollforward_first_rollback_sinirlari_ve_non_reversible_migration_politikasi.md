# Rollforward-First, Rollback Sınırları ve Non-Reversible Migration Politikası

Her migration geri alınabilir (reversible) değildir. Schema rewrite veya destructive veri mutasyonu gerektiren işlemler "non-reversible" olarak işaretlenmelidir.

- **Rollforward-First:** Geri dönüşün imkansız veya çok riskli olduğu durumlarda sistem, hataları düzeltmek için "quarantine" moduna geçip yeni düzeltme (rollforward) migration'ları bekler.
- **Automatic Rollback Yok:** Rollback otomatik çalıştırılmaz; manual onay veya script'ler gerektirir.

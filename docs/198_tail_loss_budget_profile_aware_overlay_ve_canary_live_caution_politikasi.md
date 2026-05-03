# Tail-Loss Budget, Profile-Aware Overlay ve Canary Live Caution Politikası

## Profile-Specific Budgets
Her profilin riske dayanıklılığı farklıdır:
- **`paper` / `testnet`**: Varsayılan olarak daha toleranslı bütçeler kullanır; ağırlıklı olarak "advisory" (tavsiye/uyarı) niteliğinde çalışır.
- **`derivatives_testnet`**: Kaldıraçlı ve funding rate risklerini içeren işlemler olduğu için funding/borrow şoklarında çok daha katı eşiklere sahiptir.
- **`canary_live_caution` & `live`**: Sermaye kaybı riskine karşı "Hard Limits" içerir. Senaryo başına veya günlük total stress bütçesi aşıldığında sistem "Block" veya "Reduce" kararı üretir.

## Canary Live Caution Davranışı
Eğer sistem "canary" olarak tanımlı bir canlı ortamda çalışıyorsa, en ufak bir bütçe ihlali veya likidite kuruması uyarısı dahi sistemin çalışmasını derhal kısıtlayıcı bir overlay (`BLOCK` veya `EXIT_ONLY_ADVISORY`) üretmesine neden olur.

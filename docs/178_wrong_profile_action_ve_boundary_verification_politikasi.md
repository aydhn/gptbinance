# Wrong Profile Action ve Boundary Verification Politikası

Yanlış terminalde veya yanlış profilde komut çalıştırma (wrong-context command) ciddi bir operasyonel risktir.

## Koruma Yöntemleri
- Komutlar, işlem yapmadan önce aktif bağlamın yetkilerini (Profile Sensitivity, Live-affecting flags) doğrular.
- Authorization Manager ve Readiness Checker, Context Snapshot'ını talep eder.
- Kritik eylemlerde explicit scope (örn: `--use-profile live_canary`) zorunludur.

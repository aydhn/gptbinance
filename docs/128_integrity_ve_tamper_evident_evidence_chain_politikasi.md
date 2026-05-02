# Integrity ve Tamper-Evident Evidence Chain Politikası

## Hash Manifests
- Backup'lar ve state dosyaları için SHA256 checksum tabanlı manifestler üretilir.

## Append-Only Evidence Chain
- Her yeni audit log kaydı, bir önceki kaydın Hash değerini kendi içinde taşır (`previous_hash`).
- Bu şekilde zincirin geçmişte değiştirilmesi (tampering), zincir doğrulaması (`verify_chain`) aşamasında tespit edilebilir hale gelir (`TAMPER_SUSPECTED`).

## Audit Zinciri Neden Önemli?
Sistemin manipüle edilmediğinden ve olayların kronolojik olarak doğru işlediğinden emin olmak (örneğin security breach senaryosunda) en önemli önceliktir.

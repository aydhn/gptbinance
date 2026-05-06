# Cross-Domain Evidence Packs ve Dependency Traversal Politikası

Farklı etki alanları (Market Truth, Portfolio, Risk vb.) tarafından üretilen kanıtlar, tek bir analiz paketi (Evidence Pack) altında toplanabilir.

## Evidence Packs
Bir kurul (Readiness Board) veya olay komutası (Incident Command) için ilgili tüm ilişkili kanıtları içeren taşınabilir paketlerdir. Paketin güncelliği ve eksiksizliği (completeness) ölçülebilir olmalıdır. Bayat (stale) kanıt içeren paketler otomatik olarak uyarı üretir.

## Dependency Fanout (Bağımlılık Yayılımı)
Bir kanıtın (evidence) değişmesi veya geçersiz kılınması (invalidated_by) durumunda, bu kanıta dayanan (downstream dependent) tüm kararların ve raporların etkilenmesi "Dependency Fanout" olarak adlandırılır. `DependencyEngine`, bu etkiyi hesaplar ve bir kök hatanın ne kadar geniş bir alanı etkilediğini bulur.

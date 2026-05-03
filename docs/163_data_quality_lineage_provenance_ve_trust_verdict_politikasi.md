# Data Quality, Lineage, Provenance ve Trust Politikası

## Quality Rules
Dataset'ler zorunlu kurallarla (örn: primary key duplicate, timestamp gaps, impossible values) skorlanır.
Skor breakdown ve severity analizi ile TrustVerdict üretilir.

## Lineage ve Provenance
Dataset nereden üretildi, hangi transformation ile geldi görünür olmalıdır. Incomplete lineage trust skorunu (CAUTION) etkiler.

## Trust Verdict
Sadece tek bir skor değil; reasons ve evidence breakdown taşır. Caution vs Blocked ayrımı kritiktir.

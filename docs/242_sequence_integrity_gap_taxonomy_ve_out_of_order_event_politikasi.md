# Sequence Integrity, Gap Taxonomy & Out-of-Order Events

## Sequence Integrity
Websocket veya REST'ten gelen olayların update ID'lerinin monetonik şekilde arttığı kontrol edilir.
Her stream için bağımsız `SequenceIntegrityEngine` çalışır.

## Gap Taxonomy
Aşağıdaki Gap (boşluk) türleri tanımlanmıştır:
- TRANSIENT_GAP
- PERSISTENT_GAP
- SUSPECTED_DATA_LOSS
- STALLED_FEED
- DUPLICATE_CLUSTER_SIDE_EFFECT
- SNAPSHOT_MISMATCH_GAP

## Out-of-Order Handling
Olaylar geciktiğinde gizlice yeniden sıralanmaz (No silent resorting).
Bunun yerine `SEVERE_OUT_OF_ORDER` veya `SLIGHTLY_LATE` severity etiketiyle loglanır.

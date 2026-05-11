# Schema, Manifest, Runtime State Transition ve Backward Compatibility Politikası

Bu politika, sistem bileşenlerinin evrimi sırasındaki uyumluluk kurallarını belirler.

## Kurallar
1.  **Schema Evolution:** Şema değişiklikleri mutlaka Migration Registry üzerinden yürütülür.
2.  **Backward/Forward Compatibility:** Her `TransitionContract`, işlemin geriye veya ileriye dönük uyumluluk durumunu net bir şekilde belirtmelidir.
3.  **Dual-Read / Dual-Write:** Zorunlu kesintilerin önüne geçmek için ikili okuma ve yazma desteklenir, ancak bu süre sınırlıdır ve `DualWriteRecord` olarak izlenir.
4.  **No Permanent Compatibility Limbo:** Hiçbir sistem bileşeni sonsuza kadar "eski ve yeni uyumlu" bir arafta bırakılamaz. Mutlaka bir cutover planlanmalıdır.

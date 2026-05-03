# Schema Evolution ve Compatibility Politikası

## Şema Versiyonlama
Her şema kaydı bir id ve version taşır.

## Compatibility Tipleri
- **Fully Compatible**: Değişiklik yok.
- **Backward Compatible**: Yeni (ve zorunlu olmayan) alan eklendi.
- **Incompatible (Breaking)**: Alan silindi, tip değişti, nullability kısıtlandı.

## Migration
Breaking changes, live ve paper runtime'ı riske atacağı için "requires migration" bayrağı üretir.

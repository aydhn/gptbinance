# Macro, Exchange Maintenance ve Blackout Politikası

## Makro Olaylar
Önemli ekonomik duyurular öncesinde (pre-event) ve sonrasında (post-event) pozisyon alma veya küçültme kararları alınır. Olayın önem seviyesi (severity) bu pencerelerin süresini belirler.

## Borsa Bakımları
Borsa bakımları genellikle tam blok (FULL_HALT) gerektirir. Bu durumlarda, olay penceresinde pozisyon alınmaz ve var olan açık emirler iptal edilebilir/dondurulabilir.

## Manuel Blackout
Operatörler tarafından acil durumlarda `add_manual_blackout` CLI aracıyla manuel olarak ticareti durdurma pencereleri tanımlanabilir.

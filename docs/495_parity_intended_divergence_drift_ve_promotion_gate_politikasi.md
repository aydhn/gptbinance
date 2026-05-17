# Parity, Intended Divergence, Drift ve Promotion Gate Politikası

Parity, kodun ötesine geçer: config, dependency ve data-shape parity gereklidir. Sadece aynı Docker imajını kullanmak, ortamların aynı olduğunu (same posture) garanti etmez.

Divergence, eğer bilinçli ise (örneğin maliyet tasarrufu için), bu durum `IntendedDivergenceRecord` olarak kaydedilir. Accidental drift ise anında raporlanır.

Promotion paths ve gates, ortamlar arası geçişleri (örneğin Replay -> Paper -> Probation -> Live) sıkı kurallara bağlar. Gate'ler test ve izolasyon durumlarını doğrulamadan geçişe izin vermez.

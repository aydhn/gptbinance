# Approvals, Dual Control & Exceptions

- Onaysız action "IMMEDIATE" sınıfı değilse (kill switch gibi) reddedilir.
- Exception token'lar TTL'e bağlıdır. Sınırsız bypass verilemez.
- Kill switch çekildiğinde restore süreci denetimli (guarded) yapılmalıdır.

# Concentration, Cluster, Cooldown ve Re-entry Politikası

## Concentration and Cluster Burdens
Bir asset'in (symbol) veya birden fazla asset grubunun (cluster) tüm portföye oranı hesaplanıp `ConcentrationState` oluşturulur.
Eğer Cluster Registry'ye tanımlanmış korele semboller varsa (örn: ETH ve BTC), sahte çeşitlendirme (false diversification) engellenir ve risk bu "cluster" üzerinden hesaplanır.

## Cooldown Kuralları
Bir Hard veya Emergency breach, ya da spesifik bir loss eventi olduğunda, domain/target seviyesinde cooldown tetiklenir (örn: 60 dakika block).
- Sessiz bypass yasaktır.
- Cooldown aktif olduğu sürece `active_cooldowns=True` olarak Re-entry Gate'leri bloklar.

## Re-entry Gates
Risk düşürüldüğünde dahi "hemen pozisyon açalım" mantığı reddedilir.
- Cooldown dolmalı.
- State Authoritative olmalı (approximate olmamalı).
- Liquidation proximity Safe'e çekilmiş olmalı.
Bu şartlar "cleared" olmazsa ReentryGate "False" döner ve işlem yapılması engellenir.

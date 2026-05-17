# Standard, Normal, Emergency Change; Approval, Window, Freeze Politikası

- **Standard vs Normal vs Emergency Change:**
  Standard değişiklikler önceden onaylı, düşük riskli, rutin işlemlerdir. Normal değişiklikler tam bir approval chain gerektirir. Emergency değişiklikler ise hızlı reaksiyon gerektiren ancak sonradan mutlaka normalize edilmesi (post-incident review vs. ile) gereken süreçlerdir. Asla "normal" yerine kullanılmamalıdır.

- **Approval Chains:**
  Onay zincirleri, değişikliğin türüne (ve hedeflediği surface'a) göre işletilir. Emergency approval var diye approval bypass yapılmış sayılmaz, sadece onay sınıfı değişir ve ardından ek gözden geçirmeler gerektirir.

- **Change Windows:**
  Değişikliklerin sadece Maintenance, Release, veya Emergency gibi uygun pencereler (windows) içerisinde yapılmasına izin verilir. Plansız/penceresiz (unscheduled) bir değişiklik trusted sayılamaz.

- **Freezes and Freeze Exceptions:**
  Code freeze dönemlerinde standart değişikliklere izin verilmez. Sadece onaylanmış, geçerlilik süresi (expiry) olan 'Freeze Exception' ile işlem yapılabilir. Kalıcı, süresiz freeze exception kabul edilemez.

- **Emergency Normalization Riskleri:**
  Her şeyi acil (emergency) ilan ederek süreci hızlandırma alışkanlığı, risk yönetimini sıfırlar ve yasaktır.

- **Why Approval != Safe Change:**
  Sadece bir onaycıdan "Approve" almak, rollback planının geçerli veya verification'ın yapıldığı anlamına gelmez. Approval bir adımdır, nihai güvenlik kanıtı değildir.

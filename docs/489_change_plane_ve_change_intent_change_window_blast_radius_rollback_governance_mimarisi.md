# Change Plane ve Change Intent, Change Window, Blast Radius, Rollback Governance Mimarisi

- **Requests -> Impact -> Approvals/Windows -> Execution -> Verification -> Rollback/Closure -> Trust Akışı:**
  Sistem her değişikliği sıradan bir deployment gibi değil; niyetin oluşturulduğu, etkisinin hesaplandığı, yetkili kişilerce onaylandığı, güvenli bir pencereye planlandığı, uygulandığı, doğrulandığı ve gerekli durumlarda rollback edildiği veya kapatıldığı bir iş akışı olarak görür. Trust, bu aşamaların tamamından geçer.

- **Neden Deploy != Governed Change:**
  Deploy yalnızca kodu bir ortama itme işlemidir. Governed change ise bu işlemin iş hedefleriyle uyumlu, riskleri hesaplanmış ve onaylanmış olmasını sağlar. Sadece "deploy edildi" demek, değişikliğin güvenilir ve kontrollü olduğu anlamına gelmez.

- **Neden "No Hidden Hotfix":**
  Gizli yapılan hotfixler, sistemin durumunu izlenemez hale getirir, ileride sorun teşkil edebilecek debt (borç) biriktirir ve sürpriz sonuçlar doğurur. Tüm acil durum değişiklikleri dahi "Emergency" class altında izlenmeli ve sonrasında standartlaştırılarak kapatılmalıdır.

- **Change Governance Mantığı:**
  Change Plane, tüm değişiklikleri Canonical Change Registry'de toplar, tiplerine göre ayırır (Standard, Normal, Emergency vs.) ve Equivalence, Trust, Blast Radius, Rollback Readiness gibi özelliklerini değerlendirerek material-change governance omurgasını oluşturur.

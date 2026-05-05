# Market Truth Layer & Data-Plane Safety Architecture

## Amaç
Bu döküman Market Truth Layer (Piyasa Gerçekliği Katmanı) mimarisini açıklamaktadır.
Sistem, karar vermek için kullanılan piyasa verisinin doğruluğunu, tazeliğini, sıralamasını ve stream/snapshot uyumunu sürekli doğrular.

## Kaynaklar ve Saat
- Veriler yalnızca resmi ve ücretsiz Binance Websocket / REST API'lerinden alınır. Scraping kesinlikle yasaktır.
- Canonical Market Clock kullanılarak yerel saat, borsa sunucu saati arasındaki kaymalar ölçülür.

## Neden Ayrı Bir Katman?
Çoğu trading hatası mantık hatası değil, eski, eksik ya da yanlış sıralanmış verilere dayanılarak alınan kararlardır.
Bu katman sayesinde sessizce uydurulmuş eksik veriler (interpolation) engellenir, güvenli (data-plane safety) işlemler yapılır.

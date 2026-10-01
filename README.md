# Save the World

Web kamerası ve el hareketleriyle kontrol edilen, uzay temalı bir 2D arcade oyunu. Amaç, UFO'dan Dünya'ya düşen tehlikeli nesneleri parmakları birleştirerek (pinch) yok etmek. Bu depo şu anda **erken prototip** aşamasında; tam oyun henüz yapılmadı.

## Şu anda ne çalışıyor?

`main.py` bir Pygame penceresi açıyor ve OpenCV ile kameradan görüntü okuyor. MediaPipe Hands ilk algılanan eli takip ediyor:

- Yeşil daire işaret parmağının ucunu (landmark 8), mavi daire başparmağın ucunu (landmark 4) gösteriyor.
- Kamera görüntüsü sağ-sol aynalanıyor; video oyun penceresinde gösterilmiyor.
- Parmak uçları arasındaki mesafe, bilek (0) ile orta parmak kökü (9) arasındaki mesafeye bölünerek bir pinch oranı elde ediliyor.
- Oran `0.35` altına düşünce pinch başlıyor; `0.45` üstüne çıkınca bitiyor. İki ayrı eşik, ölçümdeki küçük oynamalara karşı durumu sabit tutuyor.
- Pencere başlığında oran ve `True`/`False` pinch durumu görünüyor. El kaybolunca pinch durumu kapanıyor.

Şu anda **düşen nesne, çarpışma, skor, can, menü ve UFO yok**. Ekran siyah; renkli daireler geçici görseller. `clock.tick(140)` ekip tercihiyle bırakıldı.

## Çalıştırma

Gerekenler: Python 3.10, çalışan bir web kamerası ve Windows PowerShell. Projede kullanılan sürümler: Pygame 2.6.1, MediaPipe 0.10.20 ve OpenCV 4.11.0.86.

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pygame==2.6.1 mediapipe==0.10.20 opencv-contrib-python==4.11.0.86
.\.venv\Scripts\python.exe main.py
```

Kamera başka bir uygulamada açıksa onu kapatın. `cv2.VideoCapture(0)` varsayılan kamerayı kullanır. Pencerenin kapatma düğmesi programı sonlandırır.

## Dosyalar

- `main.py`: Şimdilik tüm çalışan prototip burada. Bilerek tek dosya tutuluyor.
- `README.md`: Ekip için proje ve kurulum özeti.
- `.gitignore`: Sanal ortamı ve yerel çalışma notlarını depodan uzak tutar.

## Sıradaki küçük adım

`main.py` içinde **tek bir kırmızı yer tutucu nesne** ekranın üstünden aşağı düşecek. Önce sadece konumunu güncelleyip çizeceğiz; yeniden doğma, pinch ile yok etme ve skor sonraki adımlar. Bu adım henüz uygulanmadı.

## Planlanan oyun

Oyuncu, düşen nesnenin üzerindeyken pinch yaparak onu yok edecek. Kaçırılan her nesne Dünya'ya ulaşınca 10 candan biri eksilecek; can sıfırlanınca oyun bitecek. Daha sonra yavaşça artan zorluk, başlangıç ekranı, UFO giriş sahnesi, skor ve yerel yüksek skor eklenecek. Oynanış oturduktan sonra geçici şekillerin yerini piksel görseller alacak. İki oyunculu LAN modu en son tasarlanacak; kamera görüntüsü ağ üzerinden gönderilmeyecek.

Geliştirme yaklaşımı: Her seferinde küçük, anlaşılır bir değişiklik; önce çalışan tek oyunculu oyun, sonra temizlik ve ek özellikler.

# Save the World

Web kamerası ve el hareketleriyle oynanan, uzay temalı bir 2D arcade oyunu. Yukarıdan inen düşman UFO'ları, parmaklarını birbirine kıstırarak (pinch) yok et ve Dünya'yı işgalden koru. Oynanış el hareketleriyle, menü ve skor kaydı klavyeyle kontrol edilir.

## Oynanış

- Yukarıdan inen **UFO'lar** Dünya'ya (alttaki mavi bölge) ulaşırsa **1 can kaybedersin**. Oyuna 5 canla başlarsın.
- İşaret parmağı ile başparmağını birbirine **kıstırıp (pinch)** bir UFO'nun üzerine getirince onu yok edersin. Başarılı bir saldırıdan sonra yeni saldırı hakkı 1 saniyede dolar; durumu HUD'da görebilirsin.
- Her 10 saniyede bir üretilen **yeşil kalpler** Dünya'ya inince **+1 can** verir. Kalbi pinch ile yakalarsan 1 can kaybedersin.
- **ULTI**: parmaklarını belirli bir şekilde tutunca ekrandaki tüm UFO'lar yok olur (beyaz flash). HUD yeniden "HAZIR" gösterdiğinde tekrar kullanabilirsin; ulti zamanlayıcısı 15 saniyedir.
- Skor, hayatta kaldığın süreyle artar. Can 0'a inince oyun biter; ismini girip skorunu yerel tabloya kaydedebilirsin.
- İlk 30 saniyede UFO'ların düşüş hızı ve çıkma sıklığı kademeli olarak artar; ardından aynı düzeyde kalır.

### El göstergesi

- İşaret + başparmak ucu: büyük **camgöbeği** daire, aralarında bir çizgi (pinch yapınca yeşile döner).
- Orta / yüzük / serçe parmak uçları: küçük **turuncu** daireler.
- Webcam görüntüsü arkada soluk şekilde görünür, elini nerede tuttuğunu görürsün.

## Kontroller

| Ekran | Tuş | İşlev |
|-------|-----|-------|
| Menü | `ENTER` | Oyunu başlat |
| Menü | `H` | Nasıl oynanır |
| Menü | `S` | Skor tablosu |
| Oyun sonu | yazı + `ENTER` | İsmini yaz, skoru kaydet |
| Skor tablosu | `R` | Tekrar oyna |
| Skor tablosu | başka tuş | Menüye dön |
| Her yer | `ESC` | Oyundan çık |

Oyun **tam ekran** açılır; 800×600'lük oyun alanı ekrana oranı bozulmadan (letterbox) ölçeklenir. Pencere kapatma düğmesi olmadığı için çıkış `ESC` iledir.

## Özellikler

- El takibiyle pinch kontrolü (MediaPipe Hands)
- İlk 30 saniyede artan zorluk (UFO hızı ve sıklığı)
- Ana menü, nasıl oynanır, oyun, oyun sonu ve yerel skor tablosu ekranları
- İsimle yerel yüksek skor kaydı (`scores.txt`)
- Kodla çizilmiş basit pixel-art (UFO, kalp, ana gemi, dünya)
- Uzay arka planı (yıldızlar + Dünya) ve soluk kamera arka planı
- Hasar/ulti ekran flash efektleri ve sol üstte HUD (can, skor, saldırı, ulti durumu)

## Çalıştırma (kaynaktan)

Gerekenler: Python 3.10, çalışan bir web kamerası. Projede kullanılan sürümler: Pygame 2.6.1, MediaPipe 0.10.20, OpenCV 4.11.0.86.

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -m pip install pygame==2.6.1 mediapipe==0.10.20 opencv-contrib-python==4.11.0.86
.\.venv\Scripts\python.exe main.py
```

Kamera başka bir uygulamada açıksa önce onu kapatın. `cv2.VideoCapture(0)` varsayılan kamerayı kullanır.

`muzik.mp3` oyunun arka plan müziğidir. Dosya bulunamazsa oyun sessiz devam eder.

## Windows için .exe üretme (arkadaşa göndermek için)

```powershell
pip install pyinstaller
pyinstaller --onedir --collect-all mediapipe --collect-all cv2 --name SaveTheWorld main.py
```

Derleme sonrası `dist\SaveTheWorld\` klasörü oluşur. **Klasörün tamamını** ZIP'leyip gönder; karşı taraf `SaveTheWorld.exe`'ye çift tıklayıp oynar (Python kurmasına gerek yok, ama **webcam gerekir**). Müzik istiyorsan `muzik.mp3`'ü de bu klasöre kopyala.

## Dosyalar

- `main.py`: Oyunun tamamı. Bilerek tek dosya tutuldu.
- `README.md`: Proje ve kurulum özeti.
- `muzik.mp3`: Arka plan müziği.
- `scores.txt`: İlk skor kaydedildiğinde oluşur; yerel yüksek skorları tutar.
- `.gitignore`: Sanal ortamı ve yerel çalışma dosyalarını depodan uzak tutar.

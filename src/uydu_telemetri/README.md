# uydu_telemetri

 basit bir telemetri simülasyonu.
Publisher node uydu verisi gönderiyor, subscriber node alıp ekrana yazıyor.

## Nasıl Çalıştırılır

source install/setup.bash

Normal başlatma:
ros2 launch uydu_telemetri satellite_launch.py

Farklı parametrelerle:
ros2 launch uydu_telemetri satellite_launch.py satellite_name:=TURKSAT-6A publish_rate:=0.5

## Parametreler
- satellite_name: hangi uydu simüle edilecek (varsayılan: TURKSAT-5A)
- publish_rate: kaç saniyede bir veri gönderilecek (varsayılan: 1.0)

## Kullandığım ROS2 Kavramları
- Publisher ve subscriber node yazımı
- Parametre tanımlama ve launch dosyasından parametre geçme
- Birden fazla node'u launch dosyasıyla başlatma

# ROS2 

ROS2 Jazzy kullanarak uydu telemetri simülasyonu.

## Klasörler
- uydu_telemetri_msgs: özel mesaj tipi
- uydu_telemetri: publisher, subscriber ve launch dosyaları
- bag_kaydi: kaydedilen bag dosyası

## Çalıştırmak İçin

colcon build

source install/setup.bash

ros2 launch uydu_telemetri satellite_launch.py

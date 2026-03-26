# uydu_telemetri_msgs

Bu paket projede kullandığım özel mesaj tipini içeriyor.

## Mesaj: TelemetriVerisi.msg

İki alan var:
- string uydu_adi - uydunun adı
- int32 sinyal_gucu - sinyal gücü dBm cinsinden

## Build etmek için

colcon build --packages-select uydu_telemetri_msgs
source install/setup.bash

## Kullandığım ROS2 Kavramları
- .msg dosyasıyla özel mesaj tanımlama
- Custom message için ayrı bir CMake paketi açmak gerektiğini öğrendim


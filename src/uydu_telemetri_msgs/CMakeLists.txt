cmake_minimum_required(VERSION 3.8)
project(uydu_telemetri_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# register our custom message file
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TelemetriVerisi.msg"
)

ament_package()
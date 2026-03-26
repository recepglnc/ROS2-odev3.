import rclpy
from rclpy.node import Node
from uydu_telemetri_msgs.msg import TelemetriVerisi

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')

        self.declare_parameter('satellite_name', 'TURKSAT-5A')
        self.declare_parameter('publish_rate', 1.0)

        self.satellite_name = self.get_parameter('satellite_name').value
        publish_rate = self.get_parameter('publish_rate').value

        self.publisher = self.create_publisher(TelemetriVerisi, 'telemetry_topic', 10)

        self.timer = self.create_timer(publish_rate, self.publish_data)

        self.signal_value = 50

        self.get_logger().info(f'Publisher started for {self.satellite_name}')

    def publish_data(self):
        msg = TelemetriVerisi()
        msg.uydu_adi = self.satellite_name
        msg.sinyal_gucu = self.signal_value

        self.publisher.publish(msg)
        self.get_logger().info(
            f'Sent --> Satellite: {msg.uydu_adi} | Signal: {msg.sinyal_gucu} dBm'
        )

        # decrease signal each time, reset when it drops too low
        self.signal_value -= 1
        if self.signal_value < 20:
            self.signal_value = 50


def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
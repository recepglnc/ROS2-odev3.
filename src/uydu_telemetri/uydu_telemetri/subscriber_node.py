import rclpy
from rclpy.node import Node
from uydu_telemetri_msgs.msg import TelemetriVerisi

class SubscriberNode(Node):

    def __init__(self):
        super().__init__('subscriber_node')

        self.subscription = self.create_subscription(
            TelemetriVerisi,
            'telemetry_topic',
            self.on_message_received,  
            10
        )

        self.get_logger().info('Subscriber ready, waiting for telemetry...')

    def on_message_received(self, msg):
        
        self.get_logger().info(
            f'[GROUND STATION] {msg.uydu_adi} --> Signal: {msg.sinyal_gucu} dBm'
        )

        # warn if signal is getting weak
        if msg.sinyal_gucu < 30:
            self.get_logger().warn('WARNING: Signal strength is low!')


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
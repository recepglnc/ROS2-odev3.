from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    
    satellite_arg = DeclareLaunchArgument(
        'satellite_name',
        default_value='TURKSAT-5A',
        description='Name of the satellite to simulate'
    )

    rate_arg = DeclareLaunchArgument(
        'publish_rate',
        default_value='1.0',
        description='How often to publish data (seconds)'
    )

    publisher_node = Node(
        package='uydu_telemetri',
        executable='publisher_node',
        name='publisher_node',
        parameters=[{
            'satellite_name': LaunchConfiguration('satellite_name'),
            'publish_rate': LaunchConfiguration('publish_rate'),
        }]
    )

    subscriber_node = Node(
        package='uydu_telemetri',
        executable='subscriber_node',
        name='subscriber_node',
    )

    return LaunchDescription([
        satellite_arg,
        rate_arg,
        publisher_node,
        subscriber_node,
    ])
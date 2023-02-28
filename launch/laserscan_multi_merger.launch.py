from launch import LaunchDescription
from launch.actions import GroupAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import SetParameter


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default=True)

    destination_frame = 'virtual_base_laser_link'
    scan_destination_topic = '/scan_raw'
    laserscan_topics = '/scan_front_raw /scan_rear_raw'
    time_increment = 0.0
    scan_time = 0.0
    range_min = 0.05
    range_max = 25.0
    angle_min = -3.1459
    angle_max = 3.1459
    angle_increment = 0.005769

    load_nodes = GroupAction(
        actions=[
            SetParameter('use_sim_time', use_sim_time),
            Node(
                package='ira_laser_tools',
                executable='laserscan_multi_merger',
                name='laserscan_multi_merger',
                output='screen',
                respawn=True,
                respawn_delay=2.0,
                parameters=[{'destination_frame': destination_frame,
                             'scan_destination_topic': scan_destination_topic,
                             'laserscan_topics': laserscan_topics,
                             'time_increment': time_increment,
                             'scan_time': scan_time,
                             'range_min': range_min,
                             'range_max': range_max,
                             'angle_min': angle_min,
                             'angle_max': angle_max,
                             'angle_increment': angle_increment,
                             }],
                arguments=['--ros-args', '--log-level', 'info'],),
        ]
    )

    ld = LaunchDescription()

    ld.add_action(load_nodes)

    return ld
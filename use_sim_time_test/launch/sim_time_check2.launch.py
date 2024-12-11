from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

ARGUMENTS = [
    DeclareLaunchArgument("use_sim_time", default_value="false", description="Use simulation time")
]


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")

    node = Node(
        package="use_sim_time_test",
        executable="sim_time_check_node2",
        name="sim_time_check_node2",
        output="screen",
        parameters=[{"use_sim_time": use_sim_time}],
    )

    ld = LaunchDescription(ARGUMENTS)
    ld.add_action(node)
    return ld

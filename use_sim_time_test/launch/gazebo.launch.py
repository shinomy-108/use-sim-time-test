from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    # Get the launch directory
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")

    gz_sim_launch = PathJoinSubstitution([pkg_ros_gz_sim, "launch", "gz_sim.launch.py"])

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gz_sim_launch]),
        launch_arguments=[("gz_args", ["empty.sdf", " -r", " -v 4"])],
    )

    clock_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        name="clock_bridge",
        output="screen",
        arguments=["/clock" + "@rosgraph_msgs/msg/Clock" + "[ignition.msgs.Clock"],
    )

    ld = LaunchDescription()
    ld.add_action(gz_sim)
    ld.add_action(clock_bridge)
    return ld

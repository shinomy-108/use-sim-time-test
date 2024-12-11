#include <rclcpp/rclcpp.hpp>

#include <std_msgs/msg/string.hpp>

#include <chrono>

using namespace std::chrono_literals;

class SimTimeCheckNode : public rclcpp::Node
{
public:
  SimTimeCheckNode() : Node("sim_time_check_node")
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("sim_time_check", 10);

    timer_ = this->create_wall_timer(std::chrono::seconds(1), [this]() { this->timer_callback(); });
  }

private:
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;

  void timer_callback()
  {
    rclcpp::Time now = this->now();

    auto message = std_msgs::msg::String();
    message.data = "Simulated time is " + std::to_string(now.seconds());
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
  }
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SimTimeCheckNode>();

  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}

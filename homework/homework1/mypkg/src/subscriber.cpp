#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

using namespace std::chrono_literals;

class Subscriber : public rclcpp::Node{

    private:
        std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Float64>> subscription_;

    public:
        Subscriber() : Node("temperature_monitor"){
                auto topic_callback = [this](std_msgs::msg::Float64::UniquePtr msg){
                    RCLCPP_INFO(this->get_logger(), "I heard: '%f'", msg->data);
                    if (msg->data > 25){
                    RCLCPP_WARN(this->get_logger(), "TEMPERATURE OVER 25");
                }
                };
                subscription_ = this->create_subscription<std_msgs::msg::Float64>("/temperature", 10, topic_callback);
            }
};

int main(int argc, char * argv[]){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Subscriber>());
    rclcpp::shutdown();
    return 0;
}

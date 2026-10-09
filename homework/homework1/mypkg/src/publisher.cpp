#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

using namespace std::chrono_literals;

class Publisher : public rclcpp::Node{
    
    private:
        std::shared_ptr<rclcpp::TimerBase> timer_;
        std::shared_ptr<rclcpp::Publisher<std_msgs::msg::Float64>> publisher_;
        float temperature_;

    public:
        Publisher() : Node("temperature_sensor"), temperature_(20){
            publisher_ = this->create_publisher<std_msgs::msg::Float64>("/temperature", 10);

            //callback to publish the temperature
            auto timer_callback = [this](){
                auto message = std_msgs::msg::Float64();
                message.data = temperature_;
                temperature_ += 0.5;
                RCLCPP_INFO(this->get_logger(), "Publishing: '%f'", message.data);
                this->publisher_->publish(message);
            };
            
            timer_ = this->create_wall_timer(1000ms, timer_callback);
        }
};

int main(int argc, char * argv[]){
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Publisher>());
    rclcpp::shutdown();
    return 0;
}

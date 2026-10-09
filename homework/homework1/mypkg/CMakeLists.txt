cmake_minimum_required(VERSION 3.8)
project(mypkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(pub src/publisher.cpp)
ament_target_dependencies(pub rclcpp std_msgs)

add_executable(sub src/subscriber.cpp)
ament_target_dependencies(sub rclcpp std_msgs)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)

  set(ament_cmake_copyright_FOUND TRUE)

  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(TARGETS
  pub
  sub
  DESTINATION lib/${PROJECT_NAME})

ament_package()

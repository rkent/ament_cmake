cmake_minimum_required(VERSION 3.20)
project(python_package_with_scripts_with_msg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)


find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
"msg/Dummy.msg"
)

find_package(ament_cmake_python REQUIRED)
ament_python_install_package(${PROJECT_NAME}  SCRIPTS_DESTINATION lib/python_package_with_scripts)



ament_package()
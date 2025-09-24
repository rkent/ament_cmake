cmake_minimum_required(VERSION 3.20)
project(python_package_version)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)


find_package(ament_cmake_python REQUIRED)
ament_python_install_package(${PROJECT_NAME}  VERSION 6.7.89)



ament_package()
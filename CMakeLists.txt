cmake_minimum_required(VERSION 3.10)
project(EULER_PROJECT)

set(CMAKE_CXX_STANDARD 17)

include_directories(src)

add_subdirectory(libs/googletest)

add_subdirectory(src/euler_project)
add_subdirectory(src/euler_project_run)
add_subdirectory(tests/euler_project_test)

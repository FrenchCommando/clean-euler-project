cmake_minimum_required(VERSION 3.10)
project(tests)

enable_testing()
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})
set(EULER_PROJECT_TEST_FILES
        euler_project_tests.cpp
    )
add_executable(runEulerProjectTests ${EULER_PROJECT_TEST_FILES})
target_link_libraries(runEulerProjectTests gtest gtest_main)
target_link_libraries(runEulerProjectTests euler_project)

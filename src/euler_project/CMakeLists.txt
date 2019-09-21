cmake_minimum_required(VERSION 3.10)
project(euler_project)

set(CMAKE_CXX_STANDARD 17)

set(EULER_PROJECT_SOURCE_FILES
        EulerProject.cpp EulerProject.h
    )

add_library(euler_project ${EULER_PROJECT_SOURCE_FILES})

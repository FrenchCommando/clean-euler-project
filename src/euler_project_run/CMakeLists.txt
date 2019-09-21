cmake_minimum_required(VERSION 3.10)
project(euler_project_run)

set(CMAKE_CXX_STANDARD 17)

set(EULER_PROJECT_RUN_FILES
        EulerProjectRun.cpp
        )

add_executable(euler_project_run ${EULER_PROJECT_RUN_FILES})

set_target_properties(euler_project_run PROPERTIES ENABLE_EXPORTS 1)

target_link_libraries(euler_project_run
                      euler_project
                     )

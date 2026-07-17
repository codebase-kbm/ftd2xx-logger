cmake_minimum_required(VERSION 3.29)

project(ftd2xx_logger LANGUAGES C CXX)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

add_library(ftd2xx SHARED
    src/
)

target_include_directories(ftd2xx PRIVATE
    ${PROJECT_SOURCE_DIR}/include
)

target_compile_definitions(ftd2xx PRIVATE
    WIN32_LEAN_AND_MEAN
)

set_target_properties(ftd2xx PROPERTIES
    OUTPUT_NAME "ftd2xx"
)
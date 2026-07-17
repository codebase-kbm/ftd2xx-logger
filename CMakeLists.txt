cmake_minimum_required(VERSION 3.29)

project(ftd2xx_logger LANGUAGES C CXX)

set(CMAKE_C_STANDARD 17)
set(CMAKE_CXX_STANDARD 17)

add_library(ftd2xx SHARED
    src/dllmain.cpp
    src/logger.cpp
    generated/ftd2xx/loader.cpp
    generated/ftd2xx/proxy.cpp
)

target_include_directories(ftd2xx PRIVATE
    src/
    generated/ftd2xx
    definitions/ftd2xx
)

target_compile_definitions(ftd2xx PRIVATE
    WIN32_LEAN_AND_MEAN
    FTD2XX_EXPORTS
)

set_target_properties(ftd2xx PROPERTIES
    OUTPUT_NAME "ftd2xx"
)

target_link_options(ftd2xx PRIVATE
    "/DEF:${CMAKE_CURRENT_SOURCE_DIR}/generated/ftd2xx/ftd2xx.dll.def"
)
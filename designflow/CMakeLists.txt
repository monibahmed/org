

cmake_minimum_required(VERSION 2.8)

project(example)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

include_directories(SYSTEM ${CONAN_INCLUDE_DIRS})

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})


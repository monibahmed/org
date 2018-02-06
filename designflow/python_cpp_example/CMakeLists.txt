cmake_minimum_required(VERSION 2.8.12)
project(python_cpp_example)

# Set source directory
set(SOURCE_DIR "python_cpp_example")

# Tell CMake that headers are also in SOURCE_DIR
include_directories(${SOURCE_DIR})
set(SOURCES "${SOURCE_DIR}/math.cpp")

# Generate Python module
add_subdirectory(lib/pybind11)
pybind11_add_module(python_cpp_example ${SOURCES} "${SOURCE_DIR}/bindings.cpp")


SET(TEST_DIR "tests")
SET(TESTS ${SOURCES}
    "${TEST_DIR}/test_main.cpp"
    "${TEST_DIR}/test_math.cpp")

# Generate a test executable
include_directories(lib/catch/include)
add_executable("${PROJECT_NAME}_test" ${TESTS})

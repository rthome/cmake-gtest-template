cmake_minimum_required(VERSION 3.10)

project(foobar CXX)
set(CMAKE_CXX_STANDARD 17)

enable_testing()

add_subdirectory(libfoobar)
add_subdirectory(foobar)
add_subdirectory(foobar-test)

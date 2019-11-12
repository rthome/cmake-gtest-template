# cmake-gtest-template

A simple CMake template for a C++ executable using a static library for logic and GTest for unit testing.

I tried to use a relatively modern CMake style, but my experience is somewhat limited.

## Project Structure

    template
    │   CMakeLists.txt
    │
    ├───foobar
    │       CMakeLists.txt
    │       main.cpp
    │
    ├───foobar-test
    │       CMakeLists.txt
    │       CMakeLists.txt.in
    │       example.cpp
    │
    └───libfoobar
            CMakeLists.txt
            example.cpp
            example.h

GTest is checked out from [from git](https://github.com/google/googletest) during configuration and automatically built and linked together with `foobar-test`. Tests are also properly registered with CTest.

## Usage

Look at the structure in `template/` or run `generate.py`:

    generate.py -t <path to target folder>  <project name>

This will copy the example project in `template/` and do a very simple rename & replace for directories and file contents with the project name you specified. This process isn't very smart and might mess something up...

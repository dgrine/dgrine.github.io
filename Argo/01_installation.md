# Installation

Since Argo consists of just a single header file without any external dependencies, __no building or installation is required__. Simply make the header file available to your project.

## Basic integration

Clone the repository

```bash
git clone https://github.com/dgrine/Argo.git
```

Alternatively, you can [download the latest archive](...) directly.

Next, add the `Argo/single_include` directory as an include directory to your compiler flags.

That's it! You can now include Argo in your C++ projects:

```C++
#include "argo/Argo.hpp"
```

## CMake integration

#### Using Git submodules

When the the Argo repository is included in your project, it suffices to add the Argo subdirectory in your `CMakeLists.txt`:

```CMake
add_subdirectory(argo)
```
This will create the target `Argo` as an `interface` library.

That's it! You can now link your targets against `Argo`:

```CMake
target_link_libraries(my-app PRIVATE Argo)
```

__Note__ If required, you can also build Argo as a static library by setting `ARGO_STATIC_LIB:BOOL=TRUE`. Aside from slightly reduced compilation times, there's no compelling reason in doing so. As such, the header-only approach is recommended.

#### Using ExternalProject_Add

The following shows integration via CMake's `ExternalProject_Add` command:

```CMake
cmake_minimum_required(VERSION 3.5)

project(App)

include(ExternalProject)
find_package(Git REQUIRED)
ExternalProject_Add(Argo
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}/extern/argo
    GIT_REPOSITORY https://github.com/dgrine/Argo
    TIMEOUT 10
    UPDATE_COMMAND ${GIT_EXECUTABLE} pull
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
    LOG_DOWNLOAD ON)
ExternalProject_Get_Property(Argo SOURCE_DIR)
set(ARGO_ROOT ${SOURCE_DIR})

add_executable(app main.cpp)
add_dependencies(app Argo)
set_target_properties(app PROPERTIES CXX_STANDARD 11) #Your project should be C++ >= 11
target_include_directories(app PRIVATE ${ARGO_ROOT}/single_include)
```

cmake_minimum_required(VERSION 3.10)
project(RubiksCubeRenderer VERSION 0.1.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find OpenGL
find_package(OpenGL REQUIRED)

# Include directories
include_directories(${OPENGL_INCLUDE_DIRS})

# Source files
set(RENDERER_SOURCES
    renderer/cube_renderer.cpp
)

set(RENDERER_HEADERS
    renderer/cube_renderer.h
)

# Create shared library
add_library(rubiks_renderer SHARED ${RENDERER_SOURCES} ${RENDERER_HEADERS})

# Link OpenGL libraries
target_link_libraries(rubiks_renderer ${OPENGL_LIBRARIES})

# Set output directory
set_target_properties(rubiks_renderer PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
)

# Install targets
install(TARGETS rubiks_renderer
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

install(FILES ${RENDERER_HEADERS}
    DESTINATION include/rubiks
)

cmake_minimum_required(VERSION 3.10)
project(am_blender_cpp VERSION 0.1.0)

add_subdirectory(extern/pybind11)

add_subdirectory(blender)
add_subdirectory(blender/intern)
add_subdirectory(blender/extern)
add_subdirectory(blender/source/blender/bmesh)
# # source after intern and extern to gather all
# # internal and external library information first, for test linking
# add_subdirectory(blender/source)

pybind11_add_module(am_blender_cpp src/main.cpp)
#include "../include/main.hpp"
#include <iostream>
#include <pybind11/pybind11.h>


namespace vehicles {

Motorcycle::Motorcycle(std::string name) {
    _name = name;
}

std::string Motorcycle::get_name() const {
    return _name;
}

void Motorcycle::ride(std::string road) const {
    std::cout << "Zoom Zoom on road: " << road << std::endl;
}

}


PYBIND11_MODULE(am_blender_cpp, m) {
    m.doc() = "am_blender_cpp module";
    m.def("get_name", &get_name, "A function which says hello");
}
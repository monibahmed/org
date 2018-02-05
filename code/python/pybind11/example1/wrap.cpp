#include "../pybind11/include/pybind11/pybind11.h"
#include "funcs.hpp"

namespace py = pybind11;

using namespace pybind11::literals;

// PYBIND11_PLUGIN(wrap) {
//   py::module m("wrap", "pybind example plugin");
//   m.def("add", &add, "A function which adds two numbers",
//         "i"_a=1, "j"_a=2);
//   return m.ptr();
// }

PYBIND11_PLUGIN(wrap, m) {
  m.doc() = "pybind example plugin";
  m.def("add", &add, "A function which adds two numbers",
        "i"_a=1, "j"_a=2);
  return m.ptr();
}

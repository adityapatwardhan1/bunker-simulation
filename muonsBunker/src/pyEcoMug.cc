// Python binding for EcoMug cosmic muon generator
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "EcoMug.h"

namespace py = pybind11;
PYBIND11_MODULE(pyEcoMug, m) {
  m.doc() = "pybind11 EcoMug plugin";
  py::class_<EcoMug>(m, "EcoMug")
    .def(py::init<>())
    .def(py::init<const EcoMug &>())
    .def("GetGenerationPosition", &EcoMug::GetGenerationPosition, "Get the generation position")
    .def("GetGenerationMomentum", static_cast<double (EcoMug::*)() const>(&EcoMug::GetGenerationMomentum), "Get the generation momentum")
    .def("GetGenerationMomentum", static_cast<void (EcoMug::*)(std::array<double,3>&) const>(&EcoMug::GetGenerationMomentum), "Get the generation momentum")
    
    .def("GetGenerationTheta", &EcoMug::GetGenerationTheta, "Get the generation theta")
    .def("GetGenerationPhi", &EcoMug::GetGenerationPhi, "Get the generation phi")
    .def("GetCharge", &EcoMug::GetCharge, "Get charge")
    .def("SetUseSky", &EcoMug::SetUseSky, "Set generation from sky")
    .def("SetUseCylinder", &EcoMug::SetUseCylinder, "Set cylindrical generation")
    .def("SetUseHSphere", &EcoMug::SetUseHSphere, "Set half-sphere generation")
    .def("SetGenerationMethod", &EcoMug::SetGenerationMethod, "Set the generation method (Sky, Cylinder or HSphere)")
    .def("GetGenerationMethod", &EcoMug::GetGenerationMethod, "Get the generation method (Sky, Cylinder or HSphere)")
    .def("SetDifferentialFlux", &EcoMug::SetDifferentialFlux, "Set the differential flux J.  Accepted functions are like double J(double momentum, double theta) momentum has to be in GeV/c and theta in radians")
    .def("SetSeed", &EcoMug::SetSeed, "Set the seed for the internal PRNG (if 0 a random seed is used)")
    .def("SetMinimumMomentum", &EcoMug::SetMinimumMomentum, "Set minimum generation Momentum")
    .def("SetMaximumMomentum", &EcoMug::SetMaximumMomentum, "Set maximum generation Momentum")
    .def("SetMinimumTheta", &EcoMug::SetMinimumTheta, "Set minimum generation Theta")
    .def("SetMaximumTheta", &EcoMug::SetMaximumTheta, "Set maximum generation Theta")
    .def("SetMinimumPhi", &EcoMug::SetMinimumPhi, "Set minimum generation phi")
    .def("SetMaximumPhi", &EcoMug::SetMaximumPhi, "Set maximum generation phi")
    .def("GetMinimumMomentum", &EcoMug::GetMinimumMomentum, "Get minimum generation Momentum")
    .def("GetMaximumMomentum", &EcoMug::GetMaximumMomentum, "Get maximum generation Momentum")
    .def("GetMinimumTheta", &EcoMug::GetMinimumTheta, "Get minimum generation Theta")
    .def("GetMaximumTheta", &EcoMug::GetMaximumTheta, "Get maximum generation Theta")
    .def("GetMinimumPhi", &EcoMug::GetMinimumPhi, "Get minimum generation phi")
    .def("GetMaximumPhi", &EcoMug::GetMaximumPhi, "Get maximum generation phi")
    .def("SetSkySize", &EcoMug::SetSkySize, "Set sky size")
    .def("SetSkyCenterPosition", &EcoMug::SetSkyCenterPosition, "Set sky center position")
    .def("SetCylinderRadius", &EcoMug::SetCylinderRadius)
    .def("SetCylinderHeight", &EcoMug::SetCylinderHeight)
    .def("SetCylinderCenterPosition", &EcoMug::SetCylinderCenterPosition)
    .def("SetCylinderMinPositionPhi", &EcoMug::SetCylinderMinPositionPhi)
    .def("SetCylinderMaxPositionPhi", &EcoMug::SetCylinderMaxPositionPhi)
    .def("GetCylinderRadius", &EcoMug::GetCylinderRadius)
    .def("GetCylinderHeight", &EcoMug::GetCylinderHeight)
    .def("GetCylinderCenterPosition", &EcoMug::GetCylinderCenterPosition)
    .def("SetHSphereRadius", &EcoMug::SetHSphereRadius)
    .def("SetHSphereCenterPosition", &EcoMug::SetHSphereCenterPosition)
    .def("SetHSphereMinPositionPhi", &EcoMug::SetHSphereMinPositionPhi)
    .def("SetHSphereMaxPositionPhi", &EcoMug::SetHSphereMaxPositionPhi)
    .def("SetHSphereMinPositionTheta", &EcoMug::SetHSphereMinPositionTheta)
    .def("SetHSphereMaxPositionTheta", &EcoMug::SetHSphereMaxPositionTheta)
    .def("GetHSphereRadius", &EcoMug::GetHSphereRadius)
    .def("GetHSphereCenterPosition", &EcoMug::GetHSphereCenterPosition)
    .def("Generate", &EcoMug::Generate)
    .def("GenerateFromCustomJ", &EcoMug::GenerateFromCustomJ);
    } // keep adding as more is needed

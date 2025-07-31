## Examining Muon Scattering Tomography for Imaging Nuclear Materials
Aditya Patwardhan's project for the 2023 Internship at the Institute for Computing in Research. Licensed under the GNU General Public License 3.0.

## Description
In a world where many countries have nuclear weapons, non-proliferation efforts have become important. This project examines using muon scattering tomography for monitoring nuclear material. Muon scattering tomography uses the scattering angles of muons passing through objects to image the objects. A 12cmx12cmx12cm cube of iron and of plutonium are visualized by plotting muonic scattering angles reconstructed from trajectories detected by plastic scintillators.

The LaTeX code to build a paper and slide presentation explaining this work are included in this repository.

## Prerequisites
To run this simulation, one needs a Python3 interpreter, the Python package manager Pip, Gnuplot, the Geant4 library and its Python binding, NumPy, and Matplotlib.

In the Debian distribution of Linux, one can install the Python3 interpreter by running
```
sudo apt install python3
```
The command in other Linux distributions should be similar.

To install Python Pip, run
```
sudo apt install python3-pip
```

To install Gnuplot, run
```
sudo apt install gnuplot
```

To install Geant4, use the instructions located at
```
https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/installguide.html#buildandinstall
```
and
```
https://geant4-userdoc.web.cern.ch/UsersGuides/InstallationGuide/html/postinstall.html
```

Download the source code (tar.gz) at
```
https://geant4.web.cern.ch/download/11.1.1.html
```

Before installing the Python binding for Geant4, the pybind11 library must be installed as a dependency:
```
pip3 install pybind11
```

Install geant4_pybind (Python binding for Geant4):
```
pip3 install geant4-pybind
```
A folder called geant4_pybind should be created.

To install NumPy, run:
```
pip3 install numpy
```

To install Matplotlib, run:
```
pip3 install matplotlib
```

To compile the paper and slide presentation, one needs to convert LaTeX files into PDFs. To install the required packages, run
```
sudo apt install texlive-latex-recommended texlive-latex-extra
```

## Cloning the Repository and Setup
Clone this repository:
```
git clone https://github.com/adityapatwardhan1/bunker-simulation.git
```
Make the cloned repository a subfolder inside geant4_pybind

In bunkerProject/muonsBunker/, run:
```
pip install -e . -vvv
```

## Running the Simulation
To run the simulation, one must define the cubes that will exist in the geometry. 

Set the dimensions of the cubes in cubeInfo.txt, separating the fields by commas. The first 3 fields are the x, y, and z coordinates of the cube's center point (in meters). The 4th field is half the side length of the cube (in meters). The last field is the symbol of the element the cube is made of.

The lower layers detector are placed at a height of 0m and the upper layers at a height of 0.8m. Knowing this is necessary to ensure the cubes do not collide with the detector itself.

One can set the number of muons to be used for the simulation by changing the number at the end of the last command in simpleRun.mac. For example, for the simulation to use 200000 muons, the last line should be
```
/run/beamOn 200000
```

One can set the detector geometry in inputMuons.ini, 1 is for the sky (flat plane) and 2 is for a half-sphere. 

To run the simulation, run:
```
python3 simulation.py simpleRun.mac
```

The output of the above command will state "close file : ../results/testFolder/resultsMonthDayTime_nt_Hits.csv" (the raw data filename) at the end.

## Analyzing the Data
Multiple additional scripts exist for analyzing the raw output data.

The program write_voxelized_data_to_csv.py divides the data into voxels for image creation and writes the voxels to a CSV. To create an image of a cube of side length 120mm, with 10mmx10mmx10mm voxels, using a raw data file "../results/testFolder/resultsWedJul121256_nt_Hits.csv" created in a simulation with 200000 muons, one would run

```
python3 write_voxelized_data_to_csv.py "../results/testFolder/resultsWedJul121256_nt_Hits.csv" 200000 10
```

To write the percentage of voxels detected for each cube as a function of voxel resolution to a CSV, run
```
python3 write_voxel_size_vs_accuracy_to_csv.py "../results/testFolder/resultsWedJul121256_nt_Hits.csv" 200000
```

Each voxel resolution in the output CSV is a factor of the cube's millimeter side length (so that the cube can be divided into voxels evenly.)

To write the average scattering angle over all voxels of the cube to a CSV, run
```
python3 write_average_scattering_angles_from_voxels_to_csv.py "../results/testFolder/resultsWedJul121256_nt_Hits.csv" 200000 120
```
This writes the average scattering angle for voxel resolutions that are factors of the cube's millimeter side length.

## Visualizing the Images
After running write_voxelized_data_to_csv.py,
A file ../results/testFolder/results{time}ntHitsVoxelsResolution{some resolution}mm.csv will be created.
To start Gnuplot, run
```
gnuplot
```
A Gnuplot prompt should appear.
To read CSV files, run
```
set datafile separator ','
```
Going with the previous example, to make a 2D plot of the (x, y) position of each voxel of closest approach versus the scattering angle of the corresponding muons, run
```
plot "../results/testFolder/resultsWedJul121256VoxelsResolution10mm.csv" u 2:3:5 palette pt 5
```
The point size can be changed by appending a pointsize to the above command. For example, to use pointsize 3, run
```
plot "../results/testFolder/resultsWedJul121256VoxelsResolution10mm.csv" u 2:3:5 palette pt 5 pointsize 3
```
To make a 3D plot of the (x, y, z) position of each voxel of closest approach versus the scattering angle of the corresponding muons, run
```
splot "../results/testFolder/resultsWedJul121256VoxelsResolution10mm.csv" u 2:3:4:5 palette pt 5
```

## Visualizing the Accuracy
After running write_voxel_size_vs_accuracy_to_csv.py, a file path will be outputted as the location where this information is stored.
To plot this in Gnuplot, run
```
gnuplot
set datafile separator ','
set key autotitle columnhead
plot "../results/testFolder/resultsWedJul121256CubeHitPercentages.csv" u 6:7:(sprintf("%.3f, %.3f"), $6, $7) with linespoints pt 7
```
This can be done with multiple files of different cubes.
For example, to plot the accuracy information of three files, run
```
plot "../results/testFolder/resultsWedJul121256CubeHitPercentages.csv" u 6:7:(sprintf("%.3f, %.3f"), $6, $7) with linespoints pt 7, "../results/testFolder/resultsThuJul133456CubeHitPercentages.csv" u 6:7:(sprintf("%.3f, %.3f"), $6, $7) with linespoints pt 7, "../results/testFolder/resultsFriJul143456CubeHitPercentages.csv" u 6:7:(sprintf("%.3f, %.3f"), $6, $7) with linespoints pt 7
```

## Visualizing the Scattering Angles
After running write_average_scattering_angles_from_voxels_to_csv.py, a file path will be outputted as the location where this information is stored.
To plot this in Gnuplot, run
```
gnuplot
set datafile separator ','
set key autotitle columnhead
plot "../results/testFolder/resultsWedJul121256AverageScatteringAnglesCubeSideLength120mm.csv" u 1:2:(sprintf("%.3f, %.3f"), $1, $2) with linespoints pt 7
```
Plotting the accuracy and the scattering angles is very similar.

## Building the Paper and Slide Presentation
The LaTeX source code to build a paper and slide presentation explaining this research are located in the paper/ and presentation/ folders, respectively.

To build the PDF paper, inside paper/, run
```
pdflatex AdityaPatwardhan-paper.tex
```

To build the PDF presentation, inside presentation/, run
```
pdflatex AdityaPatwardhan-presentation.tex
```

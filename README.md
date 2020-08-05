# RADWave:  Python code for ocean surface wave analysis by satellite radar altimeter
## CMSC6950-FinalProject

RADWave documentation is found at [radwave.readthedocs.io](https://radwave.readthedocs.io/)

RADWave is a python package built to characterise wave conditions based on altimeter data.

## Installation
### Dependencies
You will need Python 3.5+. Also, the following packages are required:

* numpy
* scipy
* pandas
* scikit-image
* seaborn
* geopy
* cartopy
* netCDF4
* shapely
* pymannkendall

### Installing using pip
You can install RADWave using the `pip` package manager with your version of Python:
```
pip install radwave
```
If you encountered an error regarding compiling files whie installing `radwave` using pip. Since you have installed all of the dependencies before, instal `radwave` using this command with `pip` package manager:
```
pip install --no-dependencies RADWave
```

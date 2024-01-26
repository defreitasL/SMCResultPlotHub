
# SMCResultPlotHub
Package for read and vizualize SMC simulations results.

---
## :zap: Main methods

* MallaSMC:
```python
# MallaSMC class represents a structured mesh for SMC (SistemadeModelado Costero) simulations.
MallaSMC(meshName, moplaPath)

Attributes:
    - name (str): The name of the mesh.
    - moplaPath (str): The path where Mopla files are located.
    - angMalla (float): The angle of the mesh in radians.
    - x0 (float): Minimum x-coordinate after rotation.
    - y0 (float): Minimum y-coordinate after rotation.
    - x0o (float): Original x-coordinate.
    - y0o (float): Original y-coordinate.
    - Ly (float): Length of the mesh in the y-direction.
    - Lx (float): Length of the mesh in the x-direction.
    - dy (float): Grid spacing in the y-direction.
    - dx (float): Grid spacing in the x-direction.
    - ny (int): Number of grid points in the y-direction.
    - nx (int): Number of grid points in the x-direction.
    - x (numpy.ndarray): X-coordinates of the mesh.
    - y (numpy.ndarray): Y-coordinates of the mesh.
    - z (numpy.ndarray): Bathymetry data of the mesh.
```

* readData:
```python
# Reads and processes wave height and direction data for a given mesh and case.
hs, dd = readData(MallaSMC, caso)

Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.
Returns:
    - Tuple: Tuple containing wave height (hs) and direction (dd) data arrays.
```

* readDataCOPLA:
```python
# Reads and processes velocity field data from COPLA simulations.
V, vx, vy = readDataCOPLA(MallaSMC, caso)

Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.

Returns:
    - Tuple: Tuple containing velocity (V), velocity x-component (vx), and velocity y-component (vy) data arrays
```

* readDataMC:
```python
# Reads and processes data for Monte Carlo simulations.

eta, dd, hs, phase, phasez, rot, YY, XX = readDataMC(malla, caso, zoomFlag)

Parameters:
    - malla (MallaSMC): The MallaSMC object representing the mesh.
    - caso (str): The case identifier.
    - zoomFlag (bool): Flag indicating whether the case was executed with zoom.

Returns:
    - Tuple: Tuple containing free surface elevation (eta), direction (dd), height (hs), phase, phase zoom (phasez), breaking points (rot), YY, and XX data arrays.
```

## :package: Package structures
````

SMCResultPlotHub
|
├── LICENSE
├── README.md
├── build
├── dist
├── SMCResultPlotHub
│   ├── __init__.py
│   ├── EMD.py
│   ├── graphEMD.py
│   ├── MallasSMC.py
│   ├── perfRot.py
│   ├── poi.py
│   ├── readData.py
│   └── utils
│       ├── __init__.py
│       └── utils.py
└── .gitignore

````
## :house: Local installation
* Using conda + pip:
```bash
# Create conda env and install python libreries

# pip install git+https://github.com/defreitasL/SMCResultPlotHub.git

```bash
---
## :recycle: Continuous integration (CI)

* Pre-commit with **black formatter** hook on `commit`. ([.pre-commit-config.yaml](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.pre-commit-config.yaml))
* Github workflow with conda based **deployment** and **testing** on `tag`. ([Github action](https://github.com/IHCantabria/TESEO.Apiprocess/blob/main/.github/workflows/main.yml))


---
## :heavy_check_mark: Testing
* To run tests manually:
```bash
# Unzip data for testing stored in "data.zip" in "tests/" folder
7z x tests/data.zip -otests/ 

# Run pytests from console
pytest
```
---

## :incoming_envelope: Contact us
:snake: For code-development issues contact :man_technologist: [Lucas de Freitas](https://github.com/defreitasL) @ :office: [IHCantabria](https://github.com/IHCantabria)

## :copyright: Credits
Developed by :man_technologist: [German Aragon](https://ihcantabria.com/en/directorio-personal/investigador/german-aragon/) @ :office: [IHCantabria](https://github.com/IHCantabria).

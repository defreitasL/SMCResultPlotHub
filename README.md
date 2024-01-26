
# SMCResultPlotHub
Package for read and vizualize SMC simulations results.

---
## :zap: Main methods


* Method X:
```python
# Method description
methodX(arg_1=1, arg_2='aaa')

```

## :package: Package structures
````
TESEO.Apiprocess
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

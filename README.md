# PyBbMm - BbMm Python Librairy

It is mainly a Python wraps of the _libBbMm_ elements.
_PyBbMm_ also introduce some user-friendly python class to better manage _BbMm_ compcepts.

## Install

The _pyBbMm_ package do not relies on any dependances, but supose that you are on a x86 Linux version.
Install is performed with _pip_ after cloning this repository.

```sh
git clone https://bitbucket.org/ktorz/wraps-python.git
pip install ./wraps-python
```

The 'example-421.py' file provides a simple example for _pyBbMm_ inspired from the _421_ game. The command `python3 example-421.py` should instanciate a model for _421_ and test _2_ transitions. 

- packaging: https://packaging.python.org/en/latest/

## Test

_pyBbMm_ is developed according to the test-driven methode based on `pytest` framework.

```sh
pip install pytest
pytest
```

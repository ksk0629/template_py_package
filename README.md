# INTRODUCTION
This is an exmple project for packaging my own python project.

# PRELIMINARIES
- Install `build` if you need to build the project: `pip install build`.

# HOW TO INSTALL

## FOR USERS
Run the following command to install the package.

`pip install -e .`

## FOR DISTRUBUTERS
Run the following command to build the package.

`python -m build`

Then `dist` directory will be created under the root in which the package is installed by the following command.

`pip install dist/example_package-0.0.1-py3-none-any.whl`

The filename depends on the settings written in the `pyproject.toml`.

## FOR DEVELOPERS
Run the following command to install the package and the dependencies.

`pip install -e ".[dev]"`

# HOW TO RUN TESTS
Run the following command.

`python -m pytest`.

# REFERENCE
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
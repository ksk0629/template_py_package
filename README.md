# INTRODUCTION
This is an exmple project for packaging my own python project.

# PRELIMINARIES
- Install `build`: `pip install build`.

# HOW TO BUILD
Run the following command.
`python3 -m build`

Then `dist` directory will be created under the root.

# HOW TO INSTALL
Run the following command.
`pip install dist/example_package-0.0.1-py3-none-any.whl`

The version or something depends on the settings written in the `pyproject.toml`.

# REFERENCE
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
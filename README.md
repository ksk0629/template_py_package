# INTRODUCTION
This is an exmple project for packaging my own python project.

# PRELIMINARIES
- Install `build`: `pip install build`.
- Install `pytest`: `pip install pytest`.

# RUN TESTS
Run the following command.
`python -m pytest`.

# HOW TO BUILD
Run the following command.
`python -m build`

Then `dist` directory will be created under the root.

# HOW TO INSTALL
If you built the project, then run the following command.
`pip install dist/example_package-0.0.1-py3-none-any.whl`

The version or something depends on the settings written in the `pyproject.toml`.

As well as you can install the project directly with running the following command.
`pip install -e .`

# REFERENCE
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
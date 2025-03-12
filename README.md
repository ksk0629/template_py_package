[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# INTRODUCTION
This is an exmple project for packaging my own python project. This assumes you to use `poetry`.

# INSTALLATION

<details>
<summary>for users</summary>
Run the following command to install the package.

`poetry install --without dev`

</details>

<details>
<summary>for developers</summary>

- Install the package

Tun the following command to install the package **with** dev-dependencies.

`poetry install`

You should run the above command with `--without dev` if you would like to verify if your package works without dev-dependencies.

- Build the package

Run the following command to build the package.

`poetry build`

This makes `whl` and `tar.gz` without dev-dependencies at a `dist` directory, which will be generated once you run the command. The filenames generated by the command depend on the settings written in the `pyproject.toml`.

</details>

# TEST
Run either the following three commands.

- `poetry run pytest`
- `poetry run pytest --cov=. --cov-report term-missing`
- `poetry run pytest --cov=. --cov-report=html`

The first one will do test, the second one will show the coverage-report in your terminal and the last one will generate it as html.

# REFERENCE
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [pytest：フィクスチャ(fixture)の使い方](https://qiita.com/_akiyama_/items/9ead227227d669b0564e) (Japanese)
- [GitHub Actions integration](https://black.readthedocs.io/en/stable/integrations/github_actions.html)
- [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html)
- [docstrings](https://qiita.com/futakuchi0117/items/4d3997c1ca1323259844)

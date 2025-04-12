# Currency Converter CLI

A simple Python app to convert between currencies using a public api. Includes test coverage and GitHub Actions CI.

## How to run
```bash
cd currency_converter
python converter.py 100 USD EUR
```

## Run tests
```bash
PYTHONPATH=$(pwd) pytest
```


## GitHub CI
On each push or pull request, the tests are run automatically via GitHub Actions.

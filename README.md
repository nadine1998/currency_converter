# Currency Converter CLI

A simple Python app to convert between currencies using static rates. Includes test coverage and GitHub Actions CI.

## How to run
```bash
cd currency_converter
python converter.py --amount 200 --from EUR --to USD
```

## Run tests
```bash
PYTHONPATH=$(pwd) pytest
```

## GitHub CI
On each push or pull request, the tests are run automatically via GitHub Actions.

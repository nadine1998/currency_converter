import pytest
from currency_converter.converter import convert


def test_usd_to_eur():
    assert convert(100, "USD", "EUR") == 91.0


def test_eur_to_usd():
    assert convert(100, "EUR", "USD") == 110.0


def test_same_currency():
    assert convert(100, "USD", "USD") == 100


def test_invalid_currency():
    with pytest.raises(ValueError):
        convert(100, "XXX", "EUR")

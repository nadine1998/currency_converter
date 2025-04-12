import pytest
from unittest.mock import patch
from currency_converter.converter import convert

# Sample mock response for the API
mock_response = {
    "provider": "https://www.exchangerate-api.com",
    "WARNING_UPGRADE_TO_V6": "https://www.exchangerate-api.com/docs/free",
    "terms": "https://www.exchangerate-api.com/terms",
    "base": "USD",
    "date": "2025-04-08",
    "time_last_updated": 1744070401,
    "rates": {"USD": 1, "EUR": 0.915, "GBP": 0.783, "JPY": 147.3, "AUD": 1.66},
}


# Test the convert function for USD to EUR
@patch("currency_converter.converter.requests.get")
def test_convert_usd_to_eur(mock_get):
    # Mock the response from the API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    amount = 100
    from_currency = "USD"
    to_currency = "EUR"

    # Perform the conversion
    result = convert(amount, from_currency, to_currency)

    # Assert that the conversion is correct
    expected_result = round(amount * mock_response["rates"][to_currency], 2)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


# Test the convert function for the case where from_currency equals to_currency
@patch("currency_converter.converter.requests.get")
def test_convert_same_currency(mock_get):
    amount = 100
    from_currency = "USD"
    to_currency = "USD"

    # No conversion needed, it should return the original amount
    result = convert(amount, from_currency, to_currency)

    assert result == amount, f"Expected {amount}, but got {result}"


# Test the convert function when the API response is missing rates
@patch("currency_converter.converter.requests.get")
def test_convert_missing_rates(mock_get):
    # Modify the mock response to simulate missing rates
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "provider": "https://www.exchangerate-api.com",
        "rates": {},
    }

    amount = 100
    from_currency = "USD"
    to_currency = "EUR"

    # Perform the conversion, expecting an error to be raised
    with pytest.raises(
        RuntimeError, match="Conversion error: Unable to get rate for EUR"
    ):
        convert(amount, from_currency, to_currency)


# Test the convert function when the API request fails
@patch("currency_converter.converter.requests.get")
def test_convert_api_failure(mock_get):
    # Simulate a network error by raising an exception
    mock_get.side_effect = Exception("Network error")

    amount = 100
    from_currency = "USD"
    to_currency = "EUR"

    # Perform the conversion, expecting an error to be raised
    with pytest.raises(RuntimeError, match="Network error: Network error"):
        convert(amount, from_currency, to_currency)

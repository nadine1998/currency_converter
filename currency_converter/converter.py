import requests
import sys


def convert(amount: float, from_currency: str, to_currency: str) -> float:
    # Ensure the function is being called
    print(f"Converting {amount} from {from_currency} to {to_currency}")

    if from_currency.upper() == to_currency.upper():
        print(f"No conversion needed. Same currency: {from_currency}")
        return amount

    # Define the URL for the API call
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"

    try:
        # Call the API and print the raw response
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an error for 4xx/5xx responses

        # Debugging: Print the full API response to check
        print(f"API Response Status Code: {response.status_code}")
        # print(f"API Response JSON: {response.json()}")

        data = response.json()

        if "rates" not in data:
            raise ValueError("Error fetching conversion rates.")

        # Fetch the conversion rate for the target currency
        rate = data["rates"].get(to_currency.upper())
        if rate is None:
            raise ValueError(f"Unable to get rate for {to_currency.upper()}")

        # Return the converted amount
        result = round(amount * rate, 2)
        print(f"{amount} {from_currency} = {result} {to_currency}")  # Print the result
        return result

    except requests.RequestException as e:
        print(f"Network error: {e}")
        raise RuntimeError(f"Network error: {e}")
    except ValueError as e:
        print(f"Conversion error: {e}")
        raise RuntimeError(f"Conversion error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise RuntimeError(f"Network error: {e}")


# Running the function from command line arguments (for testing purposes)
if __name__ == "__main__":
    try:
        amount = float(sys.argv[1])  # Get amount from command line args
        from_currency = sys.argv[2]  # Get 'from' currency
        to_currency = sys.argv[3]  # Get 'to' currency
        convert(amount, from_currency, to_currency)
    except IndexError:
        print("Please provide valid command line arguments.")
        print("Usage: python converter.py <amount> <from_currency> <to_currency>")
    except ValueError as e:
        print(f"Invalid input: {e}")

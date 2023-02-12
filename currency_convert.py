def currency_converter(amount, from_currency, to_currency):
    # URL to get the exchange rate
    URL = "https://api.exchangerate-api.com/v4/latest/" + from_currency

    # Get the exchange rate from the API
    import requests
    exchange_data = requests.get(URL).json()
    exchange_rate = exchange_data['rates'][to_currency]

    # Calculate the converted amount
    converted_amount = amount * exchange_rate

    return converted_amount

# Example usage
amount = 100
from_currency = "USD"
to_currency = "EUR"
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")

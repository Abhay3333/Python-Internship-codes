from forex_python.converter import CurrencyRates

# Create an instance of the CurrencyRates class
c = CurrencyRates()


# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    # Use the convert method from the CurrencyRates class
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount


# Get user input
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ").upper()
to_currency = input("Enter the currency to convert to: ").upper()

# Convert currency
result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")

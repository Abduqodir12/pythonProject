import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/bb2e134333b0372b457c0b73/pair/USD/UZS'

# Making our request
response = requests.get(url)
data = response.json()
kurs = data["conversion_rate"]
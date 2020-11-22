import json

import requests


response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
json_data = json.loads(response.text)
rates_data = json_data['rates']
japanese_yen = rates_data['JPY']

print("$1 USD is qual to: " + u"\u00A5" + "{0:.2f}".format(japanese_yen))

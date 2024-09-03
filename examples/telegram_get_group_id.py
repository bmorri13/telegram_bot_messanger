import requests
import json

TELEGRAM_BOT_TOKEN = 'XXX:XXXXX-XX-XXX'
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"

# Make the request and store the response
response = requests.get(url)

# Convert the response to JSON and pretty-print it
result = json.dumps(response.json(), indent=4)
print(result)
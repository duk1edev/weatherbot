# create bot in FatherBot from API Telegram
import requests
import settings

TOKEN = settings.TOKEN

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

updates = 'getUpdates'

url = URL.format(TOKEN=TOKEN, method=updates)

response = requests.get(url)

print(type(response.text))





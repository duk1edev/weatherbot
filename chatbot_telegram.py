# create bot in FatherBot from API Telegram
import requests


TOKEN = '1270287398:AAG4_GtteWenSMEWtM-29Z-HtYHscjAlAvc'

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

updates = 'getUpdates'

url = URL.format(TOKEN=TOKEN, method=updates)

response = requests.get(url)

print(response.text)




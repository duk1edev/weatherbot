import settings

TOKEN = settings.TOKEN

URL = 'https://api.telegram.org/bot{TOKEN}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID = 1113088870

UPDATE_IO_FILE_PATH = 'update_id'

with open(UPDATE_IO_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = settings.WEATHER_TOKEN

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

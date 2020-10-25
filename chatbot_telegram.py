# create bot in FatherBot from API Telegram
import requests
import const
import json
import time
from pprint import pprint


def answer_user_bot(data):
    data = {
        'chat_id': const.MY_ID,
        'text': data
    }
    url = const.URL.format(TOKEN=const.TOKEN, method=const.SEND_METH)
    response = requests.post(url, data=data)
    print(response)


def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']

    temp = round(data['main']['temp'] - 273.15, 1)
    city = data['name']
    msg = f'The weather in {city}. Temp is {temp}. State is {weather_state}'
    # pprint(msg)
    return msg


def get_weather(location):
    url = const.WEATHER_URL.format(city=location, token=const.WEATHER_TOKEN)
    response = requests.get(url)
    data = json.loads(response.content)
    if response.status_code != 200:
        return 'city not found'
    # pprint(data)
    return parse_weather_data(data)

    #pprint(response.content)


def get_message(data):
    return data['message']['text']
    # print(text)


def save_update_id(update):
    # pprint(update)
    with open(const.UPDATE_IO_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.URL.format(TOKEN=const.TOKEN, method=const.UPDATE_METH)
        content = requests.get(url).text

        data = json.loads(content)
        # if data.get('result'):
        #     pass
        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            # print(elem['message']['chat']['id'])
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        # pprint(needed_part)
        #break
        time.sleep(1)


if __name__ == '__main__':
    main()

# send to bot
# url = URL.format(TOKEN=TOKEN, method=updates)
# response = requests.get(url)
# json_content = json.loads(response.text)
# print(json_content)

# data = {
#     'chat_id': '1113088870',
#     'text': 'Hello!My name is WeatherBot!'
# }
#
#
# # send message to
# url = URL.format(TOKEN=TOKEN, method=send)
# response = requests.post(url, data=data)
# print(response)
#
# print(response.text)

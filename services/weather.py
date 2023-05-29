import requests
from pprint import pprint
#from config import API
import datetime

data = None
weat = None

def city_weather(city, token):
    global data, weat

    code_to_smile = {
        'Clear': 'Ясно ☀',
        'Clouds': 'Облачно ☁',
        'Rain': 'Дождь 🌦',
        'Drizzle': 'Дождь 🌧',
        'Thunderstorm': 'Гроза ⛈',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман 🌫'
    }

    try:
        weat = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric'
        )
        data = weat.json()
        #pprint(data)
        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не пойму что там за погода 😳'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        return (f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
              f'Погода в городе {city}:\nТемпература воздуха: {cur_weather}°C {wd}\nВлажность: {humidity}%\n'
              f'Давление: {pressure} мм.рт.ст\nВетер: {wind} м/с\nВремя восхода солнца: {sunrise}\n'
              f'Время захода солнца: {sunset}\n'
              f'Продолжительность светового дня: {length_of_day}'
              )

    except Exception as ex:
        return 'Город указан не верно 😳\nПроверьте название города'

def main():
    city = input('Введите город: ')
    city_weather(city, API)


if __name__ == '__main__':
    main()
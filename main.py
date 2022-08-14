import requests
import datetime
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        cur_weather_temp = data['main']['temp']
        cur_weather_feels = data['main']['feels_like']
        cur_weather_humidity = data['main']['humidity']
        cur_weather_pressure = data['main']['pressure']
        cur_weather_sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        cur_weather_sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        cur_weather_wind_speed = data['wind']['speed']

        print(f'на текущую дату и время погода в городе {city} {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
            f'текущая погода в городе: {city} \nТемпература: {cur_weather_temp} °\nОщущается как: {cur_weather_feels} °\n'
            f'Влажность: {cur_weather_humidity} % \nДавление: {cur_weather_pressure} мм.рт.ст \nВосход: {cur_weather_sunrise} ч.мин.сек\n'
            f'Заход: {cur_weather_sunset} ч.мин.сек\nСкорость ветра: {cur_weather_wind_speed} м/сек'
            )

    except Exception as ex:
        print(ex)
        print('проверьте название города')

def weather():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

print(weather())



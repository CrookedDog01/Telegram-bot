import requests
import telebot
import os

API_KEY = '6af80ca9335d8c2ee01e57d5b80a90f0'
bot = telebot.TeleBot(os.getenv('TOKEN'))

def get_weather(message):

    city = message.text
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_info = (f'Сейчас в городе {city} {weather_description}\n'
                        f'Температура: {temperature}°C\n'
                        f'Влажность: {humidity}%\n'
                        f'Скорость ветра: {wind_speed} м/c')
        bot.send_message(message.chat.id, weather_info)
    else:
        bot.send_message(message.chat.id, 'Извините, я не могу найти информацию о данном городе.')
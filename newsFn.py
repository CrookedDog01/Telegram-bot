import telebot
from telebot import types
import requests
import random
import os

news_api = '8c2b0f80fe0f4e99ab363f43a2d214e9'
bot = telebot.TeleBot(os.getenv('TOKEN'))
news_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def start_news(message):


    if message.text == 'Показать новости всех категорий':

        num_news = random.choice(news_list)
        news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country=ru&category=general&apiKey={news_api}')
        data = news_data.json()

        if data['status'] == 'ok':
            author = data['articles'][num_news]['author']
            title = data['articles'][num_news]['title']
            url = data['articles'][num_news]['url']
            news_info = (f'Источник {author} сообщяет\n{title}\n' + f'[подробнее...]({url})')
            bot.send_message(message.chat.id, news_info, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'Неполучилось загрузить новости')

    if message.text == 'Новости игр и технологий':

        num_news = random.choice(news_list)
        news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey={news_api}')
        data = news_data.json()

        if data['status'] == 'ok':
            author = data['articles'][num_news]['author']
            title = data['articles'][num_news]['title']
            url = data['articles'][num_news]['url']
            news_info = (f'Источник {author} сообщяет\n'
                         f'{title}\n' + f'[подробнее...]({url})')
            bot.send_message(message.chat.id, news_info, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'Неполучилось загрузить новости')

    if message.text == 'Новости спорта':

        num_news = random.choice(news_list)
        news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country=ru&category=sports&apiKey={news_api}')
        data = news_data.json()

        if data['status'] == 'ok':
            author = data['articles'][num_news]['author']
            title = data['articles'][num_news]['title']
            url = data['articles'][num_news]['url']
            news_info = (f'Источник {author} сообщяет\n'
                         f'{title}\n' + f'[подробнее...]({url})')
            bot.send_message(message.chat.id, news_info, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'Неполучилось загрузить новости')

    if message.text == 'Новости науки':

        num_news = random.choice(news_list)
        news_data = requests.get(f'https://newsapi.org/v2/top-headlines?country=ru&category=science&apiKey={news_api}')
        data = news_data.json()

        if data['status'] == 'ok':
            author = data['articles'][num_news]['author']
            title = data['articles'][num_news]['title']
            url = data['articles'][num_news]['url']
            news_info = (f'Источник {author} сообщяет\n\n'
                         f'{title}\n' + f'[подробнее...]({url})')
            bot.send_message(message.chat.id, news_info, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, 'Неполучилось загрузить новости')
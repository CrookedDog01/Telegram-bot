import telebot
from telebot import types
import os
import time
from weatherFn import get_weather
from newsFn import start_news

bot = telebot.TeleBot(os.getenv('TOKEN'))


def get_news():

    answer3 = bot.send_message(message.chat.id, 'Минуточку')
    time.sleep(1)

    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Показать новости всех категорий')
    btn2 = types.KeyboardButton('Новости игр и технологий')
    btn3 = types.KeyboardButton('Новости спорта')
    btn4 = types.KeyboardButton('Новости науки')
    keyword.add(btn1)
    keyword.add(btn2)
    keyword.add(btn3)
    keyword.add(btn4)

    answer = bot.send_message(message.chat.id, 'Выбирите нужную категорию', reply_markup=keyword)
    bot.register_next_step_handler(answer3, start_news)

def more_news(message):

    if message == 'Да':
        get_news()
    else:
        start()

@bot.message_handler(commands=["start"])
def start(message):

    keyword = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Показать погоду')
    btn2 = types.KeyboardButton('Показать новости')
    keyword.add(btn1, btn2)
    bot.send_message(message.chat.id, f'\fПривет {message.from_user.first_name}, я чат бот, меня зовут Диана.\n'
                                'Я умею очень многое\n'
                                'Выберите то, что вам нужно,\n'
                                'или введи /help для помощи',
                     reply_markup=keyword)
    time.sleep(2)
    bot.send_message(message.chat.id, 'Жду ваш запрос')


@bot.message_handler(commands=["help"])
def help(message):

    bot.send_message(message.chat.id, 'Комманды для бота:\n')


@bot.message_handler(content_types=["text"])
def handle_text(message):

    if (message.text == 'Показать погоду'):

        bot.send_message(message.chat.id, 'Секунду...')
        time.sleep(1)
        answer2 = bot.send_message(message.chat.id, 'Введите название города')
        bot.register_next_step_handler(answer2, get_weather)

    if (message.text == 'Показать новости'):
        get_news()
        time.sleep(10)
        answer = bot.send_message(message.chat.id, '_', reply_markup=types.ReplyKeyboardRemove())
        keyword1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Да')
        btn2 = types.KeyboardButton('Нет')
        keyword1.add(btn1,btn2)
        bot.send_message(message.chat.id, 'Показать еще новости', reply_markup=keyword1)

        if message.text == 'Да':
            get_news()
        else:
            start


bot.polling(none_stop=True, interval=0)
import requests
from bs4 import BeautifulSoup as b
import telebot
import random

URL = 'https://www.anekdot.ru/release/anekdot/year/2022/'
API_KEY = '5280346188:AAFfK3zyhYrZTepk1WaSZmvvPNy1SZm1FuI'
def my_anekdot_parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekgot = soup.find_all('div', class_='text')
    return [i.text for i in anekgot]

my_list = my_anekdot_parser(URL)
random.shuffle(my_list)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['начать'])

def hello(message):
    bot.send_message(message.chat.id,'Привет! Чтобы посмеяться введите любую цифру:')


@bot.message_handler(content_types=['text'])

def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, my_list[0])
        del my_list[0]
    else:
        bot.send_message(message.chat.id, 'Не не не, введи только цифру:')

bot.polling()
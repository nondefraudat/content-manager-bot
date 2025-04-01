from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from sys import argv

ACCESS_KEY=argv[1]

bot = TeleBot(ACCESS_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Ок, работаем...")

bot.polling(non_stop=True, interval=0)

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from sys import argv

ACCESS_KEY=argv[1]

bot = AsyncTeleBot(ACCESS_KEY)

@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.from_user.id, "Ок, работаем...")

bot.polling(non_stop=True, interval=0)

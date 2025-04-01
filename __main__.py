from sys import argv
from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, \
	InlineKeyboardButton, Message, CallbackQuery, User
from asyncio import run

ACCESS_KEY=argv[1]
bot = AsyncTeleBot(ACCESS_KEY)

async def unknown_request(user_id: int, request: str):
	await bot.send_message(user_id, f'Неизвестный запрос: "{request}"')

async def main_menu(user_id: int):
	markup = InlineKeyboardMarkup([
			[ InlineKeyboardButton('Администрирование', callback_data='/administration') ],
			[ InlineKeyboardButton('Каналы', callback_data='/channels') ],
			[ InlineKeyboardButton('Тайминги', callback_data='/timings') ]
		])
	await bot.send_message(user_id, 'Главное меню', reply_markup=markup)

async def administration(user_id: int):
	markup = InlineKeyboardMarkup([
			[ InlineKeyboardButton('Добавить администратора', callback_data='/pass') ],
			[ InlineKeyboardButton('Удалить администратора', callback_data='/pass') ],
			[ InlineKeyboardButton('Назад', callback_data='/start') ]
		])
	await bot.send_message(user_id, 'Администрирование', reply_markup=markup)

async def channels(user_id: int):
	markup = InlineKeyboardMarkup([
			[ InlineKeyboardButton('Добавить канал', callback_data='/pass') ],
			[ InlineKeyboardButton('Удалить канал', callback_data='/pass') ],
			[ InlineKeyboardButton('Назад', callback_data='/start') ]
		])
	await bot.send_message(user_id, 'Каналы', reply_markup=markup)

async def timings(user_id: int):
	markup = InlineKeyboardMarkup([
			[ InlineKeyboardButton('Добавить тайминг', callback_data='/pass') ],
			[ InlineKeyboardButton('Удалить тайминг', callback_data='/pass') ],
			[ InlineKeyboardButton('Назад', callback_data='/start') ]
		])
	await bot.send_message(user_id, 'Тайминги', reply_markup=markup)

@bot.message_handler(commands=['start'])
async def process_message(message: Message):
	await main_menu(message.from_user.id)

@bot.callback_query_handler()
async def process_callback(query: CallbackQuery):
	match query.data:
		case '/start': await main_menu(query.from_user.id)
		case '/administration': await administration(query.from_user.id)
		case '/channels': await channels(query.from_user.id)
		case '/timings': await timings(query.from_user.id)
		case _: await unknown_request(query.from_user.id, query.data)

run(bot.polling())

import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command

TOKEN = os.getenv('TOKEN')
bot = Bot(token = TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO, filename = "mylog.log")


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!\nЯ - бот, который будет переводить ФИО с кириллицы на латинницу!\nДля начала попробуй написать мне своё ФИО и я тебе его переведу!'
    logging.info(f'{user_name} {user_id}: запустил бота впервые')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_latin_fio(message: Message):
    translation_rules = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Е',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
    'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': 'IE',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA', ' ': ' '}
    rus_fio = message.text.upper()
    en_fio = ''
    for char in rus_fio:
        if char in translation_rules:
            en_fio += translation_rules[char]
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'{user_name} {user_id}: {text}')
    await message.answer(text=en_fio)


if __name__ == '__main__':
    dp.run_polling(bot)
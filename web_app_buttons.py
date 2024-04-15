from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.types.web_app_info import WebAppInfo


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

web_app_button = KeyboardButton(
    text='Start Web app',
    web_app=WebAppInfo(url='https://stepic.org/')
)

web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_button]],
    resize_keabord=True
)


@dp.message(Command(commands=['web_app_start']))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Experiments with web_app',
        reply_markup=web_app_keyboard
    )


if __name__ == "__main__":
    dp.run_polling(bot)
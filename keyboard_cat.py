from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

button_1 = KeyboardButton(text='dogs')
button_2 = KeyboardButton(text='cucumbers')
keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True,
    one_time_keyboard=True # добавили сворачивающуюся клавиатуру
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="What are cats afraid most of all?",
        reply_markup=keyboard
    )


@dp.message(F.text == 'dogs')
async def process_reply_dog(message: Message):
    await message.answer(
        text='Yep, they are afraid of dogs.',
        # reply_markup=ReplyKeyboardRemove()
    )


@dp.message(F.text == 'cucumbers')
async def process_reply_cucucmber(message: Message):
    await message.answer(
        text='Cucumbers are not scary.',
        # reply_mark=ReplyKeyboardRemove()
    )

if __name__ == "__main__":
    dp.run_polling(bot)


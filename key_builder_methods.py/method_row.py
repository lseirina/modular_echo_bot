"""Метод row у класса ReplyKeyboardBuilder позволяет расположить
кнопки клавиатуры автоматически,
в зависимости от параметра width - желаемого количества кнопок в ряду."""
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i + 1}') for i in range(6)
]
buttons_2: list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i + 7}') for i in range(3)
]
kb_builder = ReplyKeyboardBuilder()
kb_builder.row(*buttons_1, width=4)
kb_builder.row(*buttons_2, width=2)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='These are buttons.',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


if __name__ == "__main__":
    dp.run_polling(bot)
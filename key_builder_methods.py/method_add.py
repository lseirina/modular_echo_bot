"""метод add() добавляет кнопки с нового ряда только если в предыдущем ряду
для новых кнопок уже нет места.
Кнопки будут добавляться в ряд пока их там не станет 8."""
from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i + 1}') for i in range(5)
]
buttons_2: list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i + 6}') for i in range(10)
]

kb_builder = ReplyKeyboardBuilder()
kb_builder.row(*buttons_1, width=3)
kb_builder.add(*buttons_2)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='These are buttons',
        reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


if __name__ == '__main__':
    dp.run_polling(bot)

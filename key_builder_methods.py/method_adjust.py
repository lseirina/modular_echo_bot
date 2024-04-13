from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

buttons_1: list[KeyboardButton] = [
    KeyboardButton(text=f'Button {i + 1}') for i in range(8)
]

kb_builder = ReplyKeyboardBuilder()
kb_builder.add(*buttons_1)
kb_builder.adjust(2, 1)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="This is a keyboard.",
        reply_markup=kb_builder.as_markup(resize_keboard=True)
    )


if __name__ == "__main__":
    dp.run_polling(bot)
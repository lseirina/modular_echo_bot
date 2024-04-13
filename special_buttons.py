from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN = '6883498485:AAGtOZFurG3T-H2oDNwhQcUqeUzlMfqcJHE'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

cont_button = KeyboardButton(
    text='Send contact',
    request_contact=True
)
loc_button = KeyboardButton(
    text='Send location',
    request_location=True
)

poll_button = KeyboardButton(
    text='Create poll/quize',
    request_poll=KeyboardButtonPollType()
)


kb_builder = ReplyKeyboardBuilder()
kb_builder.row(cont_button, loc_button, poll_button, width=1)

keyboard = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True

)
@dp.message(CommandStart())
async def procces_start_command(message: Message):
    await message.answer(
        text='Expirient with different buttons',
        reply_markup=keyboard
    )


if __name__ == "__main__":
    dp.run_polling(bot)
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


@dp.message(CommandStart())
async def process_star_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

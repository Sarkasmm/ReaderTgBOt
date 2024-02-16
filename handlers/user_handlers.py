from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram.filters import CommandStart, Command
from keyboards.keyboard import create_start_menu, create_inline_menu

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_start_menu()
    await message.answer(text=LEXICON_RU.start,
                         reply_markup=keyboard)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    keyboard = create_inline_menu()
    await message.answer(text=LEXICON_RU.help,
                         reply_markup=keyboard)

@router.message(Command(commands='continue'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU.continue_)

@router.message(Command(commands='bookmarks'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU.bookmarks)




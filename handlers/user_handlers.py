from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from database.database import users_db, create_user
from filters.filters import IsDelBookmarkCallbackData, IsDigitCallbackData
from keyboards.bookmarks_kb import (create_bookmarks_keyboard,
                                    create_edit_keyboard)
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon import LEXICON_RU
from services.file_handling import book

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU[message.text])
    create_user(message.from_user.id)

@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU[message.text])
    create_user(message.from_user.id)

@router.message(Command(commands='continue'))
async def process_continue_command(message: Message):
    create_user(message.from_user.id)
    text = book[users_db[message.from_user.id].page]
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(users_db[message.from_user.id].page)
    )

@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    create_user(message.from_user.id)
    if users_db[message.from_user.id].bookmarks:
        await message.answer(
            text=LEXICON_RU[message.text],
            reply_markup=create_bookmarks_keyboard(
                *users_db[message.from_user.id].bookmarks
            )
        )
    else:
        await message.answer(text=LEXICON_RU['no_bookmarks'])

@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    create_user(message.from_user.id)
    users_db[message.from_user.id].page = 1
    text = users_db[message.from_user.id].get_current_page()
    await message.answer(
        text=text,
        reply_markup=create_pagination_keyboard(users_db[message.from_user.id].page)
    )

@router.callback_query(F.data.in_(['forward', 'backward']))
async def process_page_button_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    if callback.data == 'forward':
        users_db[callback.from_user.id].next_page()
    else:
        users_db[callback.from_user.id].previous_page()

    text = users_db[callback.from_user.id].get_current_page()

    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(users_db[callback.from_user.id].page)
    )

    await callback.answer()

@router.callback_query(lambda x: '/' in x.data and x.data.replace('/', '').isdigit())
async def process_bookmark_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    users_db[callback.from_user.id].append_bookmarks()
    await callback.answer(LEXICON_RU['add_bookmark'])

@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    text = users_db[callback.from_user.id].get_current_page()
    users_db[callback.from_user.id].page = int(callback.data)
    await callback.message.edit_text(
        text=text,
        reply_markup=create_pagination_keyboard(users_db[callback.from_user.id].page)
    )
    await callback.answer()

@router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    await callback.message.edit_text(text=LEXICON_RU['cancel_text'])
    await callback.answer()

@router.callback_query(F.data == 'edit_bookmarks')
async def process_edit_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    await callback.message.edit_text(
        text=LEXICON_RU[callback.data],
        reply_markup=create_edit_keyboard(
            *users_db[callback.from_user.id].bookmarks
        )
    )

@router.callback_query(IsDelBookmarkCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    create_user(callback.from_user.id)
    if users_db[callback.from_user.id].bookmarks:
        users_db[callback.from_user.id].delete_bookmarks(int(callback.data[:-3]))
        await callback.message.edit_text(
            text=LEXICON_RU['/bookmarks'],
            reply_markup=create_edit_keyboard(
                *users_db[callback.from_user.id].bookmarks
            )
        )
    else:
        await callback.message.edit_text(text=LEXICON_RU['no_bookmarks'])
    await callback.answer()
















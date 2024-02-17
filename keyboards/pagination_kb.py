from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU
from services.file_handling import book


def _pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    kb_builder.row(*[InlineKeyboardButton(text=LEXICON_RU.get(button, button), callback_data=button) for button in buttons])

    return kb_builder.as_markup()

def create_pagination_keyboard(page=1):
    middle_button = f"{page}/{len(book)}"
    if page == 1:
        return _pagination_keyboard(middle_button, 'forward')
    elif page == len(book):
        return _pagination_keyboard('backward', middle_button)
    else:
        return _pagination_keyboard('backward', middle_button, 'forward')
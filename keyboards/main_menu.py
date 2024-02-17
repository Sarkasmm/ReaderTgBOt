from lexicon.lexicon import LEXICON_COMMANDS_RU

from aiogram import Bot
from aiogram.types import BotCommand

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=com, description=desc)
        for com, desc in LEXICON_COMMANDS_RU.items()
    ]

    await bot.set_my_commands(main_menu_commands)
from aiogram import Router
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.misc.texts import mess

user_router = Router()
user_router.message.filter(AdminFilter())


@user_router.message(commands=["start"])
async def user_start(message: Message):
    await message.reply(mess['start'])

from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from aiogram.dispatcher.filters.content_types import ContentTypesFilter

from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup

from tgbot.misc.texts import mess, make_mess
from tgbot.misc.states import makeImg
from tgbot.misc.generate import generate
from tgbot.filters.admin import AdminFilter

img_gen_router = Router()
img_gen_router.message.filter(AdminFilter())


@img_gen_router.message(commands=["make"])
async def user_start(message: Message, state=FSMContext):
    # await message.reply(make_mess['start'])
    # await message.answer(make_mess['enter_way'])
    await generate()
    # await state.set_state(makeImg.way)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.way)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(way=text)
    await message.answer(make_mess['enter_leverage'])
    await state.set_state(makeImg.lavarage)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.lavarage)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(lavarage=text)
    await message.answer(make_mess['enter_cur'])
    await state.set_state(makeImg.currency)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.currency)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(currency=text)
    await message.answer(make_mess['enter_profit'])
    await state.set_state(makeImg.profit)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.profit)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(profit=text)
    await message.answer(make_mess['enter_fprice'])
    await state.set_state(makeImg.fprice)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.fprice)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(fprice=text)
    await message.answer(make_mess['enter_sprice'])
    await state.set_state(makeImg.sprice)


@img_gen_router.message(content_types=types.ContentType.TEXT, state=makeImg.sprice)
async def user_start(message: Message, state=FSMContext):
    text = message.text.upper()
    await state.update_data(sprice=text)
    user_data = await state.get_data()
    await state.clear()
    await generate(user_data)

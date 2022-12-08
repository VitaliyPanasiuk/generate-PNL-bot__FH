from aiogram import Router, Bot, types
from aiogram.types import Message, FSInputFile
from aiogram.dispatcher.filters.content_types import ContentTypesFilter

from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from tgbot.misc.texts import mess, make_mess
from tgbot.misc.states import makeImg
from tgbot.misc.generate import generate
from tgbot.filters.admin import AdminFilter
from tgbot.config import load_config

img_gen_router = Router()
img_gen_router.message.filter(AdminFilter())

config = load_config(".env")
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')


@img_gen_router.message(commands=["make"])
async def user_start(message: Message, state=FSMContext):
    # await message.reply(make_mess['start'])
    # await message.answer(make_mess['enter_way'])
    # await state.set_state(makeImg.way)
    ex_data = {
        'way': 'long',
        'lavarage' : '20',
        'currency' : 'btcusdt',
        'profit' : '1234567890',
        'fprice' : '1234567890',
        'sprice' : '1234567890',
    }
    await generate(ex_data)
    photo = FSInputFile('tgbot/img/output.png')
    await bot.send_photo(message.from_user.id, photo,)


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
    userid = message.from_user.id
    await state.update_data(sprice=text)
    user_data = await state.get_data()
    await state.clear()
    print(type(user_data))
    await generate(user_data)
    photo = FSInputFile('tgbot/img/output.png')
    await bot.send_photo(userid, photo, )

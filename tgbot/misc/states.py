import profile
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.fsm.state import State, StatesGroup
from environs import ParserConflictError


class makeImg(StatesGroup):
    way = State()
    lavarage = State()
    currency = State()
    profit = State()
    fprice = State()
    sprice = State()

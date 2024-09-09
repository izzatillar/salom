from loader import dp
from aiogram import types


@dp.message_handler(content_types='location', state='*')
async def echo(message: types.Message):
    print(message.location)
    await message.answer(text='echo ishga tushdi')

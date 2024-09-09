from aiogram import types
from states.state import Info, MainMenu
from keyboards.default.markups import back_uz, get_branches, menu, back_ru
from loader import dp, db


@dp.message_handler(lambda x: x.text in db.get_branches(x.from_user.id, 'ru') and x.text != back_ru,
                    state=Info.step_one_ru)
async def get_branches_uz(message: types.Message):
    sql = 'select lat, lon from filials where name = ?'
    lat, lon = db.execute(sql=sql, parameters=(message.text,), fetchone=True)
    await message.answer_location(latitude=lat, longitude=lon,
                                  reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_ru))
    await Info.step_two_ru.set()


@dp.message_handler(lambda x: x.text not in db.get_branches(x.from_user.id, 'ru') and x.text != back_ru,
                    state=Info.step_one_ru)
async def err_get_branches_uz(message: types.Message):
    await message.answer(text='Какой филиал Вас интересует?',
                         reply_markup=get_branches('ru', message.from_user.id))


@dp.message_handler(text=back_ru, state=Info.step_one_ru)
async def back_menu(message: types.Message):
    await message.answer(text='Главное меню', reply_markup=menu['ru'])
    await MainMenu.step_one_ru.set()


@dp.message_handler(text=back_ru, state=Info.step_two_ru)
async def back_branches(message: types.Message):
    await message.answer(text='Какой филиал Вас интересует?',
                         reply_markup=get_branches('ru', message.from_user.id))
    await Info.step_one_ru.set()

from aiogram import types
from states.state import Info, MainMenu
from keyboards.default.markups import back_uz, get_branches, menu, back_ru, back_eng
from loader import dp, db


@dp.message_handler(lambda x: x.text in db.get_branches(x.from_user.id, 'eng') and x.text != back_eng,
                    state=Info.step_one_eng)
async def get_branches_uz(message: types.Message):
    sql = 'select lat, lon from filials where name = ?'
    lat, lon = db.execute(sql=sql, parameters=(message.text,), fetchone=True)
    await message.answer_location(latitude=lat, longitude=lon,
                                  reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_eng))
    await Info.step_two_eng.set()


@dp.message_handler(lambda x: x.text not in db.get_branches(x.from_user.id, 'eng') and x.text != back_eng,
                    state=Info.step_one_ru)
async def err_get_branches_uz(message: types.Message):
    await message.answer(text='Which branch are you interested in?',
                         reply_markup=get_branches('eng', message.from_user.id))


@dp.message_handler(text=back_eng, state=Info.step_one_eng)
async def back_menu(message: types.Message):
    await message.answer(text='Main menu', reply_markup=menu['eng'])
    await MainMenu.step_one_eng.set()


@dp.message_handler(text=back_eng, state=Info.step_two_eng)
async def back_branches(message: types.Message):
    await message.answer(text='Which branch are you interested in?',
                         reply_markup=get_branches('eng', message.from_user.id))
    await Info.step_one_eng.set()

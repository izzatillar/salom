from aiogram import types
from states.state import Info, MainMenu
from keyboards.default.markups import back_uz, get_branches, menu
from loader import dp, db


@dp.message_handler(lambda x: x.text in db.get_branches(x.from_user.id, 'uz') and x.text != back_uz,
                    state=Info.step_one_uz)
async def get_branches_uz(message: types.Message):
    sql = 'select lat, lon from filials where name = ?'
    lat, lon = db.execute(sql=sql, parameters=(message.text,), fetchone=True)
    await message.answer_location(latitude=lat, longitude=lon,
                                  reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_uz))
    await Info.step_two_uz.set()


@dp.message_handler(lambda x: x.text not in db.get_branches(x.from_user.id, 'uz') and x.text != back_uz,
                    state=Info.step_one_uz)
async def err_get_branches_uz(message: types.Message):
    await message.answer(text='Sizni qaysi filial qiziqtiryapti?',
                         reply_markup=get_branches('uz', message.from_user.id))


@dp.message_handler(text=back_uz, state=Info.step_one_uz)
async def back_menu(message: types.Message):
    await message.answer(text='Bosh menu', reply_markup=menu['uz'])
    await MainMenu.step_one_uz.set()


@dp.message_handler(text=back_uz, state=Info.step_two_uz)
async def back_branches(message: types.Message):
    await message.answer(text='Sizni qaysi filial qiziqtiryapti?',
                         reply_markup=get_branches('uz', message.from_user.id))
    await Info.step_one_uz.set()

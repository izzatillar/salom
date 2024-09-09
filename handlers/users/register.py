from aiogram import types
from loader import db, dp
from states.state import Register, MainMenu
from aiogram.dispatcher import FSMContext
from keyboards.default.markups import uz, ru, eng, city, menu


@dp.message_handler(text=uz, state=Register.lang)
async def lang_uz(message: types.Message, state: FSMContext):
    await state.update_data(lang=uz)
    await message.answer(text='Shahar tanlang', reply_markup=city['uz'])
    await Register.city_uz.set()


@dp.message_handler(lambda x: x.text in ['Toshkent', 'Andijon', 'Samarqand'], state=Register.city_uz)
async def city_uz(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text='Menu', reply_markup=menu['uz'])
    data = await state.get_data()
    await state.finish()
    await MainMenu.step_one_uz.set()
    sql = """
INSERT into Users(chat_id, lang, city)
VALUES(?, ?, ?)
"""
    db.execute(sql=sql, parameters=(message.from_user.id, data['lang'], data['city']), commit=True)


@dp.message_handler(lambda x: x.text not in ['Toshkent', 'Andijon', 'Samarqand'], state=Register.city_uz)
async def err_city_uz(message: types.Message):
    await message.answer(text='Shahar tanlang', reply_markup=city['uz'])


@dp.message_handler(text=ru, state=Register.lang)
async def lang_uz(message: types.Message, state: FSMContext):
    await state.update_data(lang=ru)
    await message.answer(text='Выберите город', reply_markup=city['ru'])
    await Register.city_ru.set()


@dp.message_handler(lambda x: x.text in ['Ташкент', 'Андижан', 'Самарканд'], state=Register.city_ru)
async def city_uz(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text='Menu', reply_markup=menu['ru'])
    data = await state.get_data()
    await state.finish()
    await MainMenu.step_one_ru.set()
    sql = """
    INSERT into Users(chat_id, lang, city)
    VALUES(?, ?, ?)
    """

    db.execute(sql=sql, parameters=(message.from_user.id, data['lang'], data['city']), commit=True)


@dp.message_handler(lambda x: x.text not in ['Ташкент', 'Андижан', 'Самарканд'], state=Register.city_ru)
async def err_city_ru(message: types.Message):
    await message.answer(text='Shahar tanlang', reply_markup=city['ru'])


@dp.message_handler(text=eng, state=Register.lang)
async def lang_uz(message: types.Message, state: FSMContext):
    await state.update_data(lang=eng)
    await message.answer(text='Select a city', reply_markup=city['eng'])
    await Register.city_eng.set()


@dp.message_handler(lambda x: x.text in ['Tashkent', 'Andijan', 'Samarkand'], state=Register.city_eng)
async def city_uz(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    await message.answer(text='Menu', reply_markup=menu['eng'])
    await state.finish()
    await MainMenu.step_one_eng.set()
    sql = """
    INSERT into Users(chat_id, lang, city)
    VALUES(?, ?, ?)
    """

    db.execute(sql=sql, parameters=(message.from_user.id, data['lang'], data['city']), commit=True)


@dp.message_handler(lambda x: x.text not in ['Tashkent', 'Andijan', 'Samarkand'], state=Register.city_eng)
async def err_city_eng(message: types.Message):
    await message.answer(text='Shahar tanlang', reply_markup=city['eng'])

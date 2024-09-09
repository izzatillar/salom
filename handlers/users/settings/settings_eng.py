from aiogram import types
from states.state import Settings, MainMenu
from keyboards.default.markups import back_uz, settings, menu, city, back_ru, back_eng, uz, ru, eng
from loader import dp, db


# name
@dp.message_handler(text='Change name', state=Settings.step_one)
async def settings_uz(message: types.Message):
    await message.answer(text='Enter your full name',
                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_eng))
    await Settings.set_name_eng.set()


@dp.message_handler(lambda x: x.text != back_eng, state=Settings.set_name_eng)
async def set_name_uz(message: types.Message):
    sql = 'UPDATE users SET name = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])
    await Settings.step_one.set()


@dp.message_handler(text=back_eng, state=Settings.set_name_eng)
async def back_setting_uz(message: types.Message):
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])
    await Settings.step_one.set()


@dp.message_handler(text=back_eng, state=Settings.step_one)
async def back_menu(message: types.Message):
    await message.answer(text='Main menu', reply_markup=menu['eng'])
    await MainMenu.step_one_eng.set()


# contact

@dp.message_handler(text='📱 Change number', state=Settings.step_one)
async def set_contact_uz(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text='📱 My number', request_contact=True))
    markup.add(back_eng)
    await message.answer(text=f"""
📱 What is your number Send or enter your phone number as: 
+998 ** *** ****
""",
                         reply_markup=markup)
    await Settings.set_contact_eng.set()


@dp.message_handler(content_types=['contact'], state=Settings.set_contact_eng)
async def update_contact_uz(message: types.Message):
    sql = 'UPDATE users SET contact = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.contact.phone_number, message.from_user.id), commit=True)
    await message.answer(text='✅ Done')
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.content_type != ['contact'] and x.text != back_eng, state=Settings.set_contact_eng)
async def err_contact_uz(message: types.Message):
    await set_contact_uz(message)


@dp.message_handler(text=back_eng, state=Settings.set_contact_eng)
async def back_settings(message: types.Message):
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])
    await Settings.step_one.set()


# city

@dp.message_handler(text="🏙 Change city", state=Settings.step_one)
async def set_city_uz(message: types.Message):
    await message.answer(text="""
What city do you live in?
Please select a city:
""", reply_markup=city['eng'])
    await Settings.set_city_eng.set()


@dp.message_handler(lambda x: x.text in ['Tashkent', 'Andijan', 'Samarkand'], state=Settings.set_city_eng)
async def update_city_uz(message: types.Message):
    sql = 'UPDATE users SET city = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='✅ Done')
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.text not in ['Tashkent', 'Andijan', 'Samarkand'], state=Settings.set_city_eng)
async def err_update_city_uz(message: types.Message):
    await message.answer(text="""
What city do you live in?
Please select a city:
    """, reply_markup=city['eng'])
    await Settings.set_city_eng.set()


@dp.message_handler(text='🇬🇧 Change language', state=Settings.step_one)
async def set_lang(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(ru), types.KeyboardButton(uz)],
        [types.KeyboardButton(eng)],
        [back_eng]
    ])
    await message.answer(text='Choose language:', reply_markup=markup)
    await Settings.set_lang_eng.set()


@dp.message_handler(lambda x: x.text in [uz, ru, eng] and x.text != back_eng, state=Settings.set_lang_eng)
async def update_lang(message: types.Message):
    if message.text == uz:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        uz_city = db.execute(sql=
                             """select name_uz from city
                             where name_eng = ? """, parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(uz, uz_city, message.from_user.id), commit=True)
        await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
        await Settings.step_one.set()
    elif message.text == ru:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        ru_city = db.execute(sql=
                             """select name_ru from city
                             where name_eng = ?""", parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(ru, ru_city, message.from_user.id), commit=True)
        await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
        await Settings.step_one.set()
    else:

        await message.answer(text='Choose an action:', reply_markup=settings['eng'])
        await Settings.step_one.set()


@dp.message_handler(text=back_eng, state=Settings.set_lang_eng)
async def back_setting_menu(message: types.Message):
    await message.answer(text='Choose an action:', reply_markup=settings['eng'])
    await Settings.step_one.set()

from aiogram import types
from states.state import Settings, MainMenu
from keyboards.default.markups import back_uz, settings, menu, city, uz, ru, eng
from loader import dp, db


# name
@dp.message_handler(text='Ismni o’zgartirish', state=Settings.step_one)
async def settings_uz(message: types.Message):
    await message.answer(text='Ismingizni kiriting:',
                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_uz))
    await Settings.set_name_uz.set()


@dp.message_handler(lambda x: x.text != back_uz, state=Settings.set_name_uz)
async def set_name_uz(message: types.Message):
    sql = 'UPDATE users SET name = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
    await Settings.step_one.set()


@dp.message_handler(text=back_uz, state=Settings.set_name_uz)
async def back_setting_uz(message: types.Message):
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
    await Settings.step_one.set()


@dp.message_handler(text=back_uz, state=Settings.step_one)
async def back_menu(message: types.Message):
    await message.answer(text='Bosh menyu', reply_markup=menu['uz'])
    await MainMenu.step_one_uz.set()


# contact

@dp.message_handler(text='📱 Raqamni o’zgartirish', state=Settings.step_one)
async def set_contact_uz(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text='📱 Mening raqamim', request_contact=True))
    markup.add(back_uz)
    await message.answer(text='Raqamni +998 ** *** **** shaklida kiriting yoki yuboring.',
                         reply_markup=markup)
    await Settings.set_contact_uz.set()


@dp.message_handler(content_types=['contact'], state=Settings.set_contact_uz)
async def update_contact_uz(message: types.Message):
    sql = 'UPDATE users SET contact = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.contact.phone_number, message.from_user.id), commit=True)
    await message.answer(text='✅ Tayyor')
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.content_type != ['contact'] and x.text != back_uz, state=Settings.set_contact_uz)
async def err_contact_uz(message: types.Message):
    await set_contact_uz(message)


@dp.message_handler(text=back_uz, state=Settings.set_contact_uz)
async def back_settings(message: types.Message):
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
    await Settings.step_one.set()


# city

@dp.message_handler(text="🏙 Shaharni o'zgartirish", state=Settings.step_one)
async def set_city_uz(message: types.Message):
    await message.answer(text="""
Siz qaysi shaharda istiqomat qilasiz?
Iltimos, shaharni tanlang:
""", reply_markup=city['uz'])
    await Settings.set_city_uz.set()


@dp.message_handler(lambda x: x.text in ['Toshkent', 'Andijon', 'Samarqand'], state=Settings.set_city_uz)
async def update_city_uz(message: types.Message):
    sql = 'UPDATE users SET city = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='✅ Tayyor')
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.text not in ['Toshkent', 'Andijon', 'Samarqand'], state=Settings.set_city_uz)
async def err_update_city_uz(message: types.Message):
    await message.answer(text="""
Siz qaysi shaharda istiqomat qilasiz?
Iltimos, shaharni tanlang:
    """, reply_markup=city['uz'])
    await Settings.set_city_uz.set()


@dp.message_handler(text="🇺🇿 Tilni o'zgartirish", state=Settings.step_one)
async def set_lang(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(ru), types.KeyboardButton(uz)],
        [types.KeyboardButton(eng)],
        [back_uz]
    ])
    await message.answer(text='Tilni tanlang:', reply_markup=markup)
    await Settings.set_lang_uz.set()


@dp.message_handler(lambda x: x.text in [uz, ru, eng] and x.text != back_uz, state=Settings.set_lang_uz)
async def update_lang(message: types.Message):
    if message.text == ru:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        uz_city = db.execute(sql=
                             """select name_ru from city
                             where name_uz = ? """, parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(ru, uz_city, message.from_user.id), commit=True)
        await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
        await Settings.step_one.set()
    elif message.text == eng:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        ru_city = db.execute(sql=
                             """select name_eng from city
                             where name_uz = ?""", parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(eng, ru_city, message.from_user.id), commit=True)
        await message.answer(text='Choose an action:', reply_markup=settings['eng'])
        await Settings.step_one.set()
    else:
        await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
        await Settings.step_one.set()


@dp.message_handler(text=back_uz, state=Settings.set_lang_ru)
async def back_setting_menu(message: types.Message):
    await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
    await Settings.step_one.set()


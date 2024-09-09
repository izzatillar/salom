from aiogram import types
from states.state import Settings, MainMenu
from keyboards.default.markups import back_uz, settings, menu, city, back_ru, ru, eng, uz
from loader import dp, db


# name
@dp.message_handler(text='Сменить имя', state=Settings.step_one)
async def settings_uz(message: types.Message):
    await message.answer(text='Введите Ф.И.О',
                         reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(back_ru))
    await Settings.set_name_ru.set()


@dp.message_handler(lambda x: x.text != back_ru, state=Settings.set_name_ru)
async def set_name_uz(message: types.Message):
    sql = 'UPDATE users SET name = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
    await Settings.step_one.set()


@dp.message_handler(text=back_ru, state=Settings.set_name_ru)
async def back_setting_uz(message: types.Message):
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
    await Settings.step_one.set()


@dp.message_handler(text=back_ru, state=Settings.step_one)
async def back_menu(message: types.Message):
    await message.answer(text='Главное меню', reply_markup=menu['ru'])
    await MainMenu.step_one_ru.set()


# contact

@dp.message_handler(text='📱 Сменить номер', state=Settings.step_one)
async def set_contact_uz(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(text='📱 Мой номер', request_contact=True))
    markup.add(back_uz)
    await message.answer(text=f"""
📱 Какой у Вас номер. Отправьте или введите ваш номер телефона в виде: 
+998 ** *** ****
""",
                         reply_markup=markup)
    await Settings.set_contact_ru.set()


@dp.message_handler(content_types=['contact'], state=Settings.set_contact_ru)
async def update_contact_uz(message: types.Message):
    sql = 'UPDATE users SET contact = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.contact.phone_number, message.from_user.id), commit=True)
    await message.answer(text='✅ Готово')
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.content_type != ['contact'] and x.text != back_ru, state=Settings.set_contact_ru)
async def err_contact_uz(message: types.Message):
    await set_contact_uz(message)


@dp.message_handler(text=back_ru, state=Settings.set_contact_ru)
async def back_settings(message: types.Message):
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
    await Settings.step_one.set()


# city

@dp.message_handler(text="🏙 Изменить город", state=Settings.step_one)
async def set_city_uz(message: types.Message):
    await message.answer(text="""
В каком городе Вы живёте?
Пожалуйста выберите город:
""", reply_markup=city['ru'])
    await Settings.set_city_ru.set()


@dp.message_handler(lambda x: x.text in ['Ташкент', 'Андижан', 'Самарканд'], state=Settings.set_city_ru)
async def update_city_uz(message: types.Message):
    sql = 'UPDATE users SET city = ? WHERE chat_id = ?'
    db.execute(sql=sql, parameters=(message.text, message.from_user.id), commit=True)
    await message.answer(text='✅ Готово')
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])

    await Settings.step_one.set()


@dp.message_handler(lambda x: x.text not in ['Ташкент', 'Андижан', 'Самарканд'], state=Settings.set_city_ru)
async def err_update_city_uz(message: types.Message):
    await message.answer(text="""
В каком городе Вы живёте?
Пожалуйста выберите город:
    """, reply_markup=city['ru'])
    await Settings.set_city_ru.set()


@dp.message_handler(text='🇷🇺 Изменить язык', state=Settings.step_one)
async def set_lang(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [types.KeyboardButton(ru), types.KeyboardButton(uz)],
        [types.KeyboardButton(eng)],
        [back_ru]
    ])
    await message.answer(text='Выберите язык:', reply_markup=markup)
    await Settings.set_lang_ru.set()


@dp.message_handler(lambda x: x.text in [uz, ru, eng] and x.text != back_ru, state=Settings.set_lang_ru)
async def update_lang(message: types.Message):
    if message.text == uz:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        uz_city = db.execute(sql=
                             """select name_uz from city
                             where name_ru = ? """, parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(uz, uz_city, message.from_user.id), commit=True)
        await message.answer(text='Harakat tanlang:', reply_markup=settings['uz'])
        await Settings.step_one.set()
    elif message.text == eng:
        sql = 'select city from users where chat_id = ?'
        city = db.execute(sql=sql, parameters=(message.from_user.id,), fetchone=True)[0]
        ru_city = db.execute(sql=
                             """select name_eng from city
                             where name_ru = ?""", parameters=(city,), fetchone=True)[0]
        sql = 'UPDATE users SET lang = ?, city = ? WHERE chat_id = ?'
        db.execute(sql=sql, parameters=(eng, ru_city, message.from_user.id), commit=True)
        await message.answer(text='Choose an action:', reply_markup=settings['eng'])
        await Settings.step_one.set()
    else:

        await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
        await Settings.step_one.set()


@dp.message_handler(text=back_ru, state=Settings.set_lang_ru)
async def back_setting_menu(message: types.Message):
    await message.answer(text='Выберите действие:', reply_markup=settings['ru'])
    await Settings.step_one.set()
